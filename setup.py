#!/usr/bin/env python3
"""Set the LeetCode cookies in .env and immediately verify they work.

Run this in your own terminal (NOT pasted into any chat):

    python setup.py "PASTE_LEETCODE_SESSION" "PASTE_CSRFTOKEN"

It writes .env, tests the session against LeetCode, and reports PASS/FAIL
plus the exact reason on failure.
"""
import base64
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = os.path.join(HERE, ".env")
GRAPHQL = "https://leetcode.com/graphql"


def write_env(sess, csrf):
    with open(ENV, "w", encoding="utf-8") as f:
        f.write(f"LEETCODE_SESSION={sess}\n")
        f.write(f"LEETCODE_CSRF_TOKEN={csrf}\n")


def claims(sess):
    try:
        p = sess.split(".")[1]
        p += "=" * (-len(p) % 4)
        return json.loads(base64.urlsafe_b64decode(p))
    except Exception as e:
        return {"__decode_error__": str(e)}


def public_ip():
    import urllib.request
    try:
        with urllib.request.urlopen("https://api64.ipify.org", timeout=15) as r:
            return r.read().decode()
    except Exception:
        return "unknown"


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)

    sess, csrf = sys.argv[1].strip(), sys.argv[2].strip()
    if not sess.startswith("eyJ"):
        print("FAIL: LEETCODE_SESSION should be a long eyJ... JWT.")
        sys.exit(2)

    write_env(sess, csrf)
    print(f"Wrote {ENV}")

    c = claims(sess)
    if "__decode_error__" in c:
        print(f"FAIL: cookie payload is not valid base64/JSON -> {c['__decode_error__']}")
        print("      The value was damaged somewhere in transit.")
        sys.exit(1)

    expected = {"_auth_user_id", "username", "email", "ip"}
    missing = expected - set(c)
    if missing:
        print(f"FAIL: cookie payload is corrupted, missing keys: {sorted(missing)}")
        print(f"      keys present: {sorted(c)}")
        sys.exit(1)

    # Single-character damage swaps/omits letters in these keys while leaving
    # the JSON parseable, so it survives a naive decode but breaks the HMAC.
    typos = {"ivatar": "avatar", "dentity": "identity",
             "usern_slug": "user_slug", "device_with_ip": "devices_with_auth_token"}
    hit = [k for k in c if k in typos]
    if hit:
        print("FAIL: cookie payload is damaged in transit.")
        for k in hit:
            print(f"      got {k!r}, expected {typos[k]!r}")
        print("      The signature can no longer match, so LeetCode rejects it.")
        print("      Re-copy the cookie and paste it straight into this terminal.")
        sys.exit(1)

    print(f"payload OK - user={c.get('username')}  cookie_ip={c.get('ip')}  my_ip={public_ip()}")

    import requests

    s = requests.Session()
    s.cookies.set("LEETCODE_SESSION", sess, domain=".leetcode.com")
    s.cookies.set("csrftoken", csrf, domain=".leetcode.com")
    h = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "Origin": "https://leetcode.com",
        "x-csrftoken": csrf,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0.0.0",
    }

    try:
        r = s.post(GRAPHQL,
                   json={"query": "query { userStatus { username isSignedIn } }", "variables": {}},
                   headers=h, timeout=25)
        st = (r.json().get("data") or {}).get("userStatus") or {}
    except Exception as e:
        print(f"FAIL: request error -> {e}")
        sys.exit(1)

    if not st.get("isSignedIn"):
        print("FAIL: LeetCode reports isSignedIn=False.")
        print("      Cookie is valid JSON but not accepted. Usual causes:")
        print("      1. Already logged out / cookie rotated since copy")
        print("      2. LeetCode rejected the source IP")
        sys.exit(1)

    print(f"AUTH OK - logged in as {st.get('username')}")

    try:
        j = s.get("https://leetcode.com/api/problems/all/", headers=h, timeout=40).json()
        ac = sum(1 for p in j.get("stat_status_pairs", []) if p.get("status") == "ac")
        print(f"solved: num_solved={j.get('num_solved')} ac={ac}")
        if ac == 0:
            print("FAIL: authenticated but 0 problems visible -> cookie not authorised for progress.")
            sys.exit(1)
    except Exception as e:
        print(f"FAIL: problems endpoint error -> {e}")
        sys.exit(1)

    print("PASS - sync will work from this machine.")
    sys.exit(0)


if __name__ == "__main__":
    main()
