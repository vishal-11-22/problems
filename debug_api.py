import requests, json, os

s = requests.Session()
s.cookies.set("LEETCODE_SESSION", os.environ["LEETCODE_SESSION"], domain=".leetcode.com")
s.cookies.set("csrftoken", os.environ["LEETCODE_CSRF_TOKEN"], domain=".leetcode.com")
csrf = os.environ["LEETCODE_CSRF_TOKEN"]

headers = {"Content-Type": "application/json", "Referer": "https://leetcode.com", "x-csrftoken": csrf}

# Test 1: submissionList - pass lastKey as variable
print("=== Test 1: submissionList ===")
q = """query($slug: String!, $offset: Int!, $limit: Int!, $lastKey: String) {
    submissionList(offset:$offset, limit:$limit, lastKey:$lastKey, questionSlug:$slug) {
        submissions { id status statusDisplay lang runtime }
    }
}"""
r = s.post("https://leetcode.com/graphql", json={"query": q, "variables": {"slug": "two-sum", "offset": 0, "limit": 5, "lastKey": None}}, headers=headers)
print(f"Status: {r.status_code}")
resp = r.json()
if "errors" in resp:
    print(f"Errors: {resp['errors']}")
elif resp.get("data", {}).get("submissionList"):
    subs = resp["data"]["submissionList"]["submissions"]
    print(f"Got {len(subs)} submissions")
    for sub in subs[:3]:
        print(f"  {sub['lang']} - {sub['statusDisplay']} - id:{sub['id']}")
else:
    print(f"Response: {json.dumps(resp, indent=2)[:500]}")

# Test 2: recentAcSubmissionList with username
print("\n=== Test 2: recentAcSubmissionList ===")
q2 = """query($username: String!) {
    recentAcSubmissionList(username: $username) { titleSlug title id }
}"""
r2 = s.post("https://leetcode.com/graphql", json={"query": q2, "variables": {"username": "user4896Gh"}}, headers=headers)
print(f"Status: {r2.status_code}")
resp2 = r2.json()
if "errors" in resp2:
    print(f"Errors: {resp2['errors']}")
else:
    items = resp2.get("data", {}).get("recentAcSubmissionList", [])
    print(f"Got {len(items)} recent accepted")
    for item in items[:5]:
        print(f"  {item['title']} ({item['titleSlug']})")

# Test 3: submissionDetails - get code
if resp.get("data", {}).get("submissionList", {}).get("submissions"):
    sub = resp["data"]["submissionList"]["submissions"][0]
    print(f"\n=== Test 3: submissionDetails for id {sub['id']} ===")
    q3 = """query($id: Int!) {
        submissionDetails(submissionId: $id) {
            code runtimeDisplay memoryDisplay
        }
    }"""
    r3 = s.post("https://leetcode.com/graphql", json={"query": q3, "variables": {"id": int(sub["id"])}}, headers=headers)
    print(f"Status: {r3.status_code}")
    resp3 = r3.json()
    if "errors" in resp3:
        print(f"Errors: {resp3['errors']}")
    else:
        d = resp3.get("data", {}).get("submissionDetails", {})
        code = d.get("code", "")
        print(f"Got code: {len(code)} chars")
        print(f"Runtime: {d.get('runtimeDisplay')}")
        print(f"First 100 chars: {code[:100]}")
