#!/usr/bin/env python3
"""
LeetCode -> GitHub Auto-Sync
Fetches accepted submissions from LeetCode and pushes them to GitHub.
"""

import os
import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

try:
    from dotenv import load_dotenv
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv", "-q"])
    from dotenv import load_dotenv

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

LANG_EXT = {
    "python3": "py", "python": "py",
    "cpp": "cpp", "c": "c",
    "java": "java",
    "javascript": "js", "typescript": "ts",
    "go": "go", "rust": "rs",
    "kotlin": "kt", "scala": "scala",
    "mysql": "sql", "mssql": "sql", "oraclesql": "sql",
}

SQL_TAGS = {"database", "sql"}


def gql(query, variables, session, csrf_token):
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "Origin": "https://leetcode.com",
        "x-csrftoken": csrf_token,
    }
    resp = session.post(
        LEETCODE_GRAPHQL,
        json={"query": query, "variables": variables},
        headers=headers,
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json().get("data", {})


def get_solved_problems(session):
    """Get ALL solved problems in ONE API call using REST endpoint."""
    r = session.get("https://leetcode.com/api/problems/all/", timeout=15)
    r.raise_for_status()
    pairs = r.json().get("stat_status_pairs", [])
    solved = []
    for p in pairs:
        if p.get("status") == "ac":
            stat = p.get("stat", {})
            solved.append({
                "questionId": stat.get("question_id"),
                "frontendId": stat.get("frontend_question_id"),
                "title": stat.get("question__title"),
                "slug": stat.get("question__title_slug"),
                "difficulty": p.get("difficulty", {}).get("level"),
                "isPaidOnly": stat.get("paid_only", False),
            })
    return solved


def get_problem_details(session, csrf_token, slug):
    """Get problem metadata (tags, category) via GraphQL."""
    q = """query($slug: String!) {
        question(titleSlug: $slug) {
            questionFrontendId title titleSlug difficulty
            topicTags { name slug }
            categoryTitle
        }
    }"""
    data = gql(q, {"slug": slug}, session, csrf_token)
    return data.get("question")


def get_accepted_submissions(session, csrf_token, slug):
    q = """query($slug: String!, $offset: Int!, $limit: Int!, $lastKey: String) {
        submissionList(offset:$offset, limit:$limit, lastKey:$lastKey, questionSlug:$slug) {
            submissions { id status statusDisplay lang runtime memory timestamp }
        }
    }"""
    data = gql(q, {"slug": slug, "offset": 0, "limit": 10, "lastKey": None}, session, csrf_token)
    subs = data.get("submissionList", {}).get("submissions", [])
    return [s for s in subs if s.get("status") == 10 or s.get("statusDisplay") == "Accepted"]


def get_submission_code(session, csrf_token, sub_id):
    q = """query($id: Int!) {
        submissionDetails(submissionId: $id) {
            code runtimeDisplay memoryDisplay
        }
    }"""
    data = gql(q, {"id": int(sub_id)}, session, csrf_token)
    d = data.get("submissionDetails")
    if d and d.get("code"):
        return {"code": d["code"], "runtime": d.get("runtimeDisplay", ""), "memory": d.get("memoryDisplay", "")}
    return None


def is_sql(p):
    tags = {t["slug"].lower() for t in p.get("topicTags", [])}
    cat = p.get("categoryTitle", "").lower()
    return bool(tags & SQL_TAGS) or "database" in cat or "sql" in cat


def diff_label(level):
    return {1: "Easy", 2: "Medium", 3: "Hard"}.get(level, "Unknown")


def write_readme(fp, p, sols):
    pid = p.get("questionFrontendId", p.get("frontendId", "?"))
    title = p.get("title", "")
    slug = p.get("slug", p.get("titleSlug", ""))
    diff = p.get("difficulty", "")
    if isinstance(diff, int):
        diff = diff_label(diff)
    tags = [t["name"] for t in p.get("topicTags", [])]
    color = {"Easy": "b9d85c", "Medium": "ffb800", "Hard": "ff375f"}.get(diff, "999999")
    lines = [
        f"# {pid}. {title}", "",
        f"[{diff}](https://img.shields.io/badge/{diff}-{color})", "",
        f"**Link:** [{title}](https://leetcode.com/problems/{slug}/)", "",
        "## Tags", "",
        " | ".join(f"`{t}`" for t in tags) if tags else "_No tags_", "",
        "## Solutions", "",
        "| Language | Runtime | Memory |",
        "|----------|---------|--------|",
    ]
    for lang, d in sols.items():
        lines.append(f"| {lang} | {d.get('runtime','N/A')} | {d.get('memory','N/A')} |")
    lines.extend(["", "---", f"_Synced {datetime.now().strftime('%Y-%m-%d %H:%M')}_", ""])
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text("\n".join(lines), encoding="utf-8")


def write_root_readme(base, dsa, sql):
    total = dsa + sql
    (base / "README.md").write_text(f"""# LeetCode Solutions

Auto-synced LeetCode solutions repository.

## Progress

| Category | Solved |
|----------|--------|
| DSA | {dsa} |
| SQL | {sql} |
| **Total** | **{total}** |

## Structure

```
DSA/   <- Data Structures & Algorithms
SQL/   <- SQL / Database problems
```

Auto-synced via GitHub Actions every 6 hours.

_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_
""", encoding="utf-8")


def run_git(args, cwd):
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)


def sync(base_path, lc_session, csrf, push=False, gh_token=None, gh_repo=None):
    print("=" * 50)
    print("LeetCode -> GitHub Sync")
    print("=" * 50)

    s = requests.Session()
    s.cookies.set("LEETCODE_SESSION", lc_session, domain=".leetcode.com")
    s.cookies.set("csrftoken", csrf, domain=".leetcode.com")

    # Auth
    print("\n[1/5] Authenticating...")
    try:
        d = gql("query { userStatus { username } }", {}, s, csrf)
        user = d.get("userStatus", {}).get("username", "")
        print(f"  Logged in as: {user}")
    except:
        print("  Auth check failed, proceeding anyway...")

    # Get ALL solved problems (1 API call)
    print("\n[2/5] Fetching solved problems...")
    solved = get_solved_problems(s)
    print(f"  Found {len(solved)} solved problems")

    # Fetch details and code for each
    print("\n[3/5] Fetching solution code...")
    dsa_count = 0
    sql_count = 0
    total = len(solved)

    for i, prob in enumerate(solved):
        slug = prob["slug"]
        pid = prob["frontendId"]
        title = prob["title"]
        padded = str(pid).zfill(4)
        print(f"  [{i+1}/{total}] #{pid} {title}")

        # Get problem details (tags, category) for SQL detection
        details = get_problem_details(s, csrf, slug)
        if details:
            prob.update(details)

        # Get accepted submissions
        try:
            acc = get_accepted_submissions(s, csrf, slug)
        except Exception as e:
            print(f"    Error: {e}")
            continue

        if not acc:
            continue

        # Latest per language
        seen_lang = {}
        for sub in acc:
            lang = sub["lang"]
            if lang not in seen_lang:
                seen_lang[lang] = sub

        folder = base_path / ("SQL" if is_sql(prob) else "DSA") / f"{padded}-{slug}"
        folder.mkdir(parents=True, exist_ok=True)
        sols = {}
        for lang, sub in seen_lang.items():
            code_data = get_submission_code(s, csrf, sub["id"])
            if code_data:
                ext = LANG_EXT.get(lang, lang)
                (folder / f"solution.{ext}").write_text(code_data["code"], encoding="utf-8")
                sols[lang] = code_data
                print(f"    {lang}: OK")
            time.sleep(0.2)

        if sols:
            # Build problem dict for readme
            readme_prob = {
                "questionFrontendId": pid,
                "title": title,
                "slug": slug,
                "difficulty": prob.get("difficulty"),
                "topicTags": prob.get("topicTags", []),
            }
            write_readme(folder / "README.md", readme_prob, sols)
            if is_sql(prob):
                sql_count += 1
            else:
                dsa_count += 1

        time.sleep(0.3)

    # Update root README
    print("\n[4/5] Updating README...")
    write_root_readme(base_path, dsa_count, sql_count)

    print(f"\n[5/5] Done! DSA: {dsa_count} | SQL: {sql_count} | Total: {dsa_count + sql_count}")

    if push:
        print("\nPushing to GitHub...")
        run_git(["add", "-A"], cwd=base_path)
        if run_git(["status", "--porcelain"], cwd=base_path).stdout.strip():
            run_git(["commit", "-m", f"Sync {dsa_count + sql_count} solutions - {datetime.now().strftime('%Y-%m-%d %H:%M')}"], cwd=base_path)
            if gh_token and gh_repo:
                remote = f"https://{gh_token}@github.com/{gh_repo}.git"
                run_git(["remote", "remove", "origin"], cwd=base_path)
                run_git(["remote", "add", "origin", remote], cwd=base_path)
                r = run_git(["push", "-u", "origin", "main", "--force"], cwd=base_path)
                if r.returncode == 0:
                    print("Pushed to GitHub!")
                else:
                    print(f"Push failed: {r.stderr.strip()}")
        else:
            print("No changes to push")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--config")
    parser.add_argument("--push", action="store_true")
    parser.add_argument("--dir", default=".")
    args = parser.parse_args()

    config_path = Path(args.config) if args.config else Path(__file__).parent / ".env"
    if config_path.exists():
        load_dotenv(config_path)
    else:
        load_dotenv()

    lc = os.getenv("LEETCODE_SESSION", "")
    cr = os.getenv("LEETCODE_CSRF_TOKEN", "")
    if not lc or not cr:
        print("ERROR: Set LEETCODE_SESSION and LEETCODE_CSRF_TOKEN in .env")
        sys.exit(1)

    base = Path(args.dir).resolve()
    base.mkdir(parents=True, exist_ok=True)
    sync(base, lc, cr, args.push, os.getenv("GITHUB_TOKEN", ""), os.getenv("GITHUB_REPO", ""))
