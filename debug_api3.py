import requests, json, os

s = requests.Session()
s.cookies.set("LEETCODE_SESSION", os.environ["LEETCODE_SESSION"], domain=".leetcode.com")
s.cookies.set("csrftoken", os.environ["LEETCODE_CSRF_TOKEN"], domain=".leetcode.com")
csrf = os.environ["LEETCODE_CSRF_TOKEN"]
headers = {"Content-Type": "application/json", "Referer": "https://leetcode.com", "x-csrftoken": csrf}

q = """query {
    userProgressQuestionList {
        questions {
            titleSlug title frontendId questionStatus lastSubmittedAt
        }
    }
}"""
r = s.post("https://leetcode.com/graphql", json={"query": q, "variables": {}}, headers=headers)
resp = r.json()
questions = resp.get("data", {}).get("userProgressQuestionList", {}).get("questions", [])
print(f"Total: {len(questions)}")
statuses = {}
for q in questions:
    st = q.get("questionStatus", "NONE")
    statuses[st] = statuses.get(st, 0) + 1
    print(f"  #{q.get('frontendId')} {q.get('title')} status={q.get('questionStatus')}")
print(f"\nStatuses: {statuses}")

# Also check: maybe the query accepts filter params
print("\n\n=== Try with profileUserSlug ===")
q2 = """query($slug: String!) {
    userProgressQuestionList(profileUserSlug: $slug) {
        questions {
            titleSlug title frontendId questionStatus
        }
    }
}"""
r2 = s.post("https://leetcode.com/graphql", json={"query": q2, "variables": {"slug": "user4896Gh"}}, headers=headers)
resp2 = r2.json()
if "errors" in resp2:
    print(f"Errors: {json.dumps(resp2['errors'], indent=2)[:500]}")
else:
    qs2 = resp2.get("data", {}).get("userProgressQuestionList", {}).get("questions", [])
    print(f"Total with slug: {len(qs2)}")
    acc2 = [q for q in qs2 if q.get("questionStatus") == "ACCEPTED"]
    print(f"Accepted: {len(acc2)}")
    for q in acc2[:5]:
        print(f"  #{q.get('frontendId')} {q.get('title')}")
