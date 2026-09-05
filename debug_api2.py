import requests, json, os

s = requests.Session()
s.cookies.set("LEETCODE_SESSION", os.environ["LEETCODE_SESSION"], domain=".leetcode.com")
s.cookies.set("csrftoken", os.environ["LEETCODE_CSRF_TOKEN"], domain=".leetcode.com")
csrf = os.environ["LEETCODE_CSRF_TOKEN"]
headers = {"Content-Type": "application/json", "Referer": "https://leetcode.com", "x-csrftoken": csrf}

# Test: Try to get ALL accepted problems from profile
queries = [
    ("userProfileUserQuestionProgress", """query($slug: String!) {
        userProfileUserQuestionProgress(userSlug: $slug) {
            numAcceptedQuestions { difficulty count }
            numFailedAttempts { difficulty count }
        }
    }""", {"slug": "user4896Gh"}),

    ("userProfile", """query {
        userProfile {
            submissionProgress {
                totalSubmissions
                waSubmissions
            }
        }
    }""", {}),

    ("userProfileUserQuestionSubmitStats", """query($slug: String!) {
        userProfileUserQuestionSubmitStats(userSlug: $slug) {
            acSubmissionNum { difficulty count submissions }
        }
    }""", {"slug": "user4896Gh"}),
]

for name, q, vars in queries:
    print(f"=== {name} ===")
    r = s.post("https://leetcode.com/graphql", json={"query": q, "variables": vars}, headers=headers)
    print(f"Status: {r.status_code}")
    resp = r.json()
    if "errors" in resp:
        print(f"Errors: {json.dumps(resp['errors'], indent=2)[:300]}")
    else:
        print(f"Data: {json.dumps(resp.get('data', {}), indent=2)[:500]}")
    print()
