import requests, json, os

s = requests.Session()
s.cookies.set("LEETCODE_SESSION", os.environ["LEETCODE_SESSION"], domain=".leetcode.com")
s.cookies.set("csrftoken", os.environ["LEETCODE_CSRF_TOKEN"], domain=".leetcode.com")

# REST API - returns ALL problems with user's status in one call
r = s.get("https://leetcode.com/api/problems/all/", timeout=15)
print(f"Status: {r.status_code}")
data = r.json()
pairs = data.get("stat_status_pairs", [])
print(f"Total problems: {len(pairs)}")

# Filter solved (status == "ac")
solved = [p for p in pairs if p.get("status") == "ac"]
print(f"Solved (accepted): {len(solved)}")

# Show first 10
for p in solved[:10]:
    stat = p.get("stat", {})
    print(f"  #{stat.get('question_id')} {stat.get('question__title')} ({stat.get('question__title_slug')})")

# Show all solved slugs
slugs = [p.get("stat", {}).get("question__title_slug") for p in solved]
print(f"\nAll {len(slugs)} solved slugs:")
for slug in slugs:
    print(f"  {slug}")
