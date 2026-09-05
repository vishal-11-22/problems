#!/usr/bin/env python3
"""
LeetCode → GitHub Auto-Sync
Fetches accepted submissions from LeetCode and pushes them to GitHub.
Organizes DSA problems in DSA/ and SQL/Database problems in SQL/.
"""

import os
import re
import sys
import json
import subprocess
import time
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("Installing requests...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

try:
    from dotenv import load_dotenv
except ImportError:
    print("Installing python-dotenv...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv", "-q"])
    from dotenv import load_dotenv


# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"
LEETCODE_API = "https://leetcode.com/api"

LANG_EXT = {
    "python3": "py", "python": "py",
    "cpp": "cpp", "c": "c",
    "java": "java",
    "javascript": "js", "typescript": "ts",
    "go": "go", "rust": "rs",
    "ruby": "rb", "swift": "swift",
    "kotlin": "kt", "scala": "scala",
    "mysql": "sql", "mssql": "sql", "oraclesql": "sql",
}

SQL_TAGS = {"database", "sql"}


# ──────────────────────────────────────────────
# LeetCode API
# ──────────────────────────────────────────────

def make_request(query, variables, session, csrf_token):
    """Make a GraphQL request to LeetCode."""
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
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        print(f"  API errors: {data['errors']}")
    return data.get("data", {})


def get_all_problems(session, csrf_token):
    """Fetch all problems with their metadata (id, title, slug, difficulty, tags, category)."""
    query = """query allQuestions {
        allQuestions {
            questionId
            questionFrontendId
            title
            titleSlug
            difficulty
            isPaidOnly
            topicTags { name slug }
            categoryTitle
        }
    }"""
    data = make_request(query, {}, session, csrf_token)
    problems = data.get("allQuestions", [])
    # Filter out paid-only problems
    return [p for p in problems if not p.get("isPaidOnly")]


def get_submissions(session, csrf_token, title_slug, limit=50):
    """Fetch recent submissions for a specific problem."""
    query = """query submissionList($offset: Int!, $limit: Int!, $questionSlug: String!) {
        submissionList(offset: $offset, limit: $limit, lastKey: null, questionSlug: $questionSlug) {
            lastKey
            hasNext
            submissions {
                id
                status
                statusDisplay
                lang
                runtime
                memory
                timestamp
            }
        }
    }"""
    data = make_request(query, {
        "offset": 0,
        "limit": limit,
        "questionSlug": title_slug,
    }, session, csrf_token)
    return data.get("submissionList", {}).get("submissions", [])


def get_latest_accepted_per_lang(submissions):
    """Return the latest accepted submission per programming language."""
    seen = {}
    for sub in submissions:
        if sub.get("status") == 10 or sub.get("statusDisplay") == "Accepted":
            lang = sub["lang"]
            if lang not in seen:
                seen[lang] = sub
    return seen


def get_submission_code(session, csrf_token, submission_id):
    """Fetch the full code + stats for a specific submission."""
    query = """query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            lang { name }
            runtime
            runtimeDisplay
            runtimePercentile
            memory
            memoryDisplay
            memoryPercentile
            timestamp
            statusCode
        }
    }"""
    data = make_request(query, {"submissionId": int(submission_id)}, session, csrf_token)
    details = data.get("submissionDetails")
    if details and details.get("code"):
        return {
            "code": details["code"],
            "runtime": details.get("runtimeDisplay", ""),
            "memory": details.get("memoryDisplay", ""),
            "runtime_percentile": details.get("runtimePercentile"),
            "memory_percentile": details.get("memoryPercentile"),
            "timestamp": details.get("timestamp"),
        }
    return None


# ──────────────────────────────────────────────
# File Operations
# ──────────────────────────────────────────────

def is_sql_problem(problem):
    """Determine if a problem is SQL/Database based on tags and category."""
    tags = {t["slug"].lower() for t in problem.get("topicTags", [])}
    category = problem.get("categoryTitle", "").lower()
    if any(t in SQL_TAGS for t in tags):
        return True
    if "database" in category or "sql" in category:
        return True
    return False


def get_ext(lang):
    """Map LeetCode language id to file extension."""
    return LANG_EXT.get(lang, lang)


def write_readme(filepath, problem, submissions_data):
    """Generate a README.md for a problem folder."""
    pid = problem.get("questionFrontendId", problem.get("questionId", "?"))
    title = problem.get("title", "Unknown")
    slug = problem.get("titleSlug", "")
    difficulty = problem.get("difficulty", "Unknown")
    tags = [t["name"] for t in problem.get("topicTags", [])]
    diff_color = {"Easy": "b9d85c", "Medium": "ffb800", "Hard": "ff375f"}.get(difficulty, "999999")

    lines = [
        f"# {pid}. {title}",
        "",
        f"[{difficulty}](https://img.shields.io/badge/{difficulty}-{diff_color})",
        "",
        f"**Link:** [{title}](https://leetcode.com/problems/{slug}/)",
        "",
        "## Tags",
        "",
        " | ".join(f"`{t}`" for t in tags) if tags else "_No tags_",
        "",
        "## Solutions",
        "",
        "| Language | Runtime | Memory |",
        "|----------|---------|--------|",
    ]

    for lang, data in submissions_data.items():
        ext = get_ext(lang)
        fname = f"solution.{ext}"
        rt = data.get("runtime", "N/A")
        mem = data.get("memory", "N/A")
        lines.append(f"| {lang} | {rt} | {mem} |")

    lines.extend(["", "---", f"_Auto-synced on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_", ""])

    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text("\n".join(lines), encoding="utf-8")


def write_solution(filepath, code):
    """Write solution code to a file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(code, encoding="utf-8")


def write_root_readme(base_path, dsa_count, sql_count):
    """Update the root README.md with progress stats."""
    total = dsa_count + sql_count
    content = f"""# LeetCode Solutions

Auto-synced LeetCode solutions repository. Solutions are pushed automatically via GitHub Actions after each Accepted submission.

## Progress

| Category | Solved |
|----------|--------|
| DSA | {dsa_count} |
| SQL | {sql_count} |
| **Total** | **{total}** |

## Structure

```
DSA/            <- Data Structures & Algorithms problems
+-- 0001-two-sum/
|   +-- README.md
|   +-- solution.py
+-- ...

SQL/            <- SQL / Database problems
+-- 0175-combine-two-tables/
|   +-- README.md
|   +-- solution.sql
+-- ...
```

## Auto-Sync

This repo uses **GitHub Actions** to sync solutions from [LeetCode](https://leetcode.com) every 6 hours.

**Setup:**
1. Fork or clone this repo
2. Add GitHub secrets: `LEETCODE_SESSION` and `LEETCODE_CSRF_TOKEN`
3. Push to your repo - Actions will run automatically

---

_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_
"""
    (base_path / "README.md").write_text(content, encoding="utf-8")


# ──────────────────────────────────────────────
# Git Operations
# ──────────────────────────────────────────────

def run_git(args, cwd):
    """Run a git command."""
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  git {' '.join(args)}: {result.stderr.strip()}")
    return result


def init_repo(base_path):
    """Initialize git repo if not already initialized."""
    git_dir = base_path / ".git"
    if not git_dir.exists():
        run_git(["init"], cwd=base_path)
        run_git(["branch", "-M", "main"], cwd=base_path)
        print("Initialized git repo")


def commit_and_push(base_path, github_token=None, github_repo=None):
    """Commit all changes and push."""
    run_git(["add", "-A"], cwd=base_path)

    status = run_git(["status", "--porcelain"], cwd=base_path)
    if not status.stdout.strip():
        print("No changes to commit")
        return

    msg = f"Sync LeetCode solutions - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    run_git(["commit", "-m", msg], cwd=base_path)

    if github_token and github_repo:
        remote_url = f"https://{github_token}@github.com/{github_repo}.git"
        run_git(["remote", "remove", "origin"], cwd=base_path)
        run_git(["remote", "add", "origin", remote_url], cwd=base_path)
        result = run_git(["push", "-u", "origin", "main", "--force"], cwd=base_path)
        if result.returncode == 0:
            print("Pushed to GitHub")
        else:
            print(f"Push failed: {result.stderr.strip()}")
    else:
        print("No GitHub credentials — skipped push (commit done locally)")


# ──────────────────────────────────────────────
# Main Sync
# ──────────────────────────────────────────────

def sync(base_path, leetcode_session, csrf_token, push=False, github_token=None, github_repo=None):
    """Main sync function."""
    print("=" * 50)
    print("LeetCode → GitHub Sync")
    print("=" * 50)

    # Setup session
    session = requests.Session()
    session.cookies.set("LEETCODE_SESSION", leetcode_session, domain=".leetcode.com")
    session.cookies.set("csrftoken", csrf_token, domain=".leetcode.com")

    # Validate auth
    print("\n[1/6] Validating authentication...")
    try:
        test_query = """query { userStatus { username } }"""
        data = make_request(test_query, {}, session, csrf_token)
        username = data.get("userStatus", {}).get("username")
        if username:
            print(f"  Logged in as: {username}")
        else:
            print("  WARNING: Could not verify login. Proceeding anyway...")
    except Exception as e:
        print(f"  Auth check failed: {e}")
        print("  Make sure LEETCODE_SESSION and csrftoken are valid.")
        return

    # Fetch all problems
    print("\n[2/6] Fetching problem list...")
    problems = get_all_problems(session, csrf_token)
    # Build lookup: questionId -> problem
    problem_map = {}
    for p in problems:
        pid = p.get("questionFrontendId") or p.get("questionId")
        if pid:
            problem_map[str(pid)] = p
    print(f"  Found {len(problems)} problems ({len(problem_map)} with IDs)")

    # Fetch recent submissions
    print("\n[3/6] Fetching recent submissions...")
    all_subs = []
    try:
        # Get recent_AC from profile
        profile_query = """query recentAcSubmissions {
            recentAcSubmissions { titleSlug title id }
        }"""
        data = make_request(profile_query, {}, session, csrf_token)
        recent = data.get("recentAcSubmissions", [])
        print(f"  Found {len(recent)} recent accepted submissions")
        # Deduplicate by titleSlug
        seen_slugs = set()
        unique_recent = []
        for r in recent:
            if r["titleSlug"] not in seen_slugs:
                seen_slugs.add(r["titleSlug"])
                unique_recent.append(r)
        all_subs = unique_recent
    except Exception as e:
        print(f"  Error fetching recent submissions: {e}")

    # For each problem, get the latest accepted submission per language
    print("\n[4/6] Fetching solution code...")
    solutions = {}  # problem_id -> {lang: {code, runtime, ...}}
    dsa_count = 0
    sql_count = 0

    for i, entry in enumerate(all_subs):
        title_slug = entry["titleSlug"]
        problem_id = str(entry.get("id", ""))

        # Find problem metadata
        problem = problem_map.get(problem_id)
        if not problem:
            # Try to find by slug
            for p in problems:
                if p.get("titleSlug") == title_slug:
                    problem = p
                    problem_id = str(p.get("questionFrontendId", p.get("questionId", "")))
                    break

        if not problem:
            print(f"  [{i+1}/{len(all_subs)}] Skipping {title_slug} (no metadata)")
            continue

        pid_display = problem.get("questionFrontendId", problem.get("questionId", "?"))
        title = problem.get("title", title_slug)
        print(f"  [{i+1}/{len(all_subs)}] #{pid_display} {title}")

        # Fetch submissions for this problem
        subs = get_submissions(session, csrf_token, title_slug)
        latest = get_latest_accepted_per_lang(subs)

        if not latest:
            print(f"    No accepted submissions found, skipping")
            continue

        # Fetch code for each language
        problem_solutions = {}
        for lang, sub in latest.items():
            details = get_submission_code(session, csrf_token, sub["id"])
            if details:
                problem_solutions[lang] = details
                print(f"    {lang}: OK ({details.get('runtime', 'N/A')})")
            else:
                print(f"    {lang}: Failed to fetch code")

        if problem_solutions:
            solutions[problem_id] = {
                "problem": problem,
                "solutions": problem_solutions,
            }
            if is_sql_problem(problem):
                sql_count += 1
            else:
                dsa_count += 1

        # Be nice to the API
        time.sleep(0.5)

    # Write files
    print("\n[5/6] Writing files...")
    for problem_id, data in solutions.items():
        problem = data["problem"]
        sols = data["solutions"]
        slug = problem.get("titleSlug", "unknown")
        pid = problem.get("questionFrontendId", problem.get("questionId", problem_id))
        padded = pid.zfill(4)

        if is_sql_problem(problem):
            folder = base_path / "SQL" / f"{padded}-{slug}"
        else:
            folder = base_path / "DSA" / f"{padded}-{slug}"

        # Write solution files
        for lang, details in sols.items():
            ext = get_ext(lang)
            solution_file = folder / f"solution.{ext}"
            write_solution(solution_file, details["code"])

        # Write problem README
        readme_file = folder / "README.md"
        write_readme(readme_file, problem, sols)

    # Update root README
    print("\n[6/6] Updating root README...")
    write_root_readme(base_path, dsa_count, sql_count)

    print(f"\nDone! DSA: {dsa_count} | SQL: {sql_count} | Total: {dsa_count + sql_count}")

    # Git operations
    if push:
        print("\nCommitting and pushing...")
        init_repo(base_path)
        commit_and_push(base_path, github_token, github_repo)
    else:
        print("\nSkipping push (use --push to enable)")

    return dsa_count + sql_count


# ──────────────────────────────────────────────
# Entry Point
# ──────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sync LeetCode solutions to GitHub")
    parser.add_argument("--config", help="Path to .env config file")
    parser.add_argument("--push", action="store_true", help="Commit and push after sync")
    parser.add_argument("--dir", default=".", help="Base directory (default: current dir)")
    args = parser.parse_args()

    # Load config
    config_path = Path(args.config) if args.config else Path(__file__).parent / ".env"
    if config_path.exists():
        load_dotenv(config_path)
        print(f"Loaded config from {config_path}")
    else:
        load_dotenv()

    # Get credentials
    leetcode_session = os.getenv("LEETCODE_SESSION", "")
    csrf_token = os.getenv("LEETCODE_CSRF_TOKEN", "")

    if not leetcode_session or not csrf_token:
        print("ERROR: Missing credentials!")
        print("Set LEETCODE_SESSION and LEETCODE_CSRF_TOKEN in .env or environment.")
        print("\nHow to get them:")
        print("  1. Log in to leetcode.com")
        print("  2. Open DevTools (F12) -> Application -> Cookies")
        print("  3. Copy LEETCODE_SESSION and csrftoken values")
        sys.exit(1)

    base_path = Path(args.dir).resolve()
    base_path.mkdir(parents=True, exist_ok=True)

    # Optional GitHub credentials
    github_token = os.getenv("GITHUB_TOKEN", "")
    github_repo = os.getenv("GITHUB_REPO", "")

    sync(
        base_path=base_path,
        leetcode_session=leetcode_session,
        csrf_token=csrf_token,
        push=args.push,
        github_token=github_token,
        github_repo=github_repo,
    )
