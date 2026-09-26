#!/usr/bin/env python3
"""Check whether the LeetCode session cookie works FROM THIS MACHINE.

Run this on your own PC (not in CI). It tells you whether the cookie is
good and whether LeetCode is rejecting it because of your IP address.
"""
import base64
import json
import os
import sys

import requests

GRAPHQL = "https://leetcode.com/graphql"


def load_env():
    env = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env):
        for line in open(env, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def token_ip(tok):
    try:
        p = tok.split(".")[1]
        p += "=" * (-len(p) % 4)
        return json.loads(base64.urlsafe_b64decode(p)).get("ip", "")
    except Exception:
        return ""


def main():
    load_env()
    tok = os.getenv("LEETCODE_SESSION", "")
    csrf = os.getenv("LEETCODE_CSRF_TOKEN", "")
    if not tok or not csrf:
        print("Set LEETCODE_SESSION and LEETCODE_CSRF_TOKEN in .env first.")
        sys.exit(1)

    try:
        import urllib.request
        with urllib.request.urlopen("https://api.ipify.org", timeout=15) as r:
            my_ip = r.read().decode()
    except Exception:
        my_ip = "unknown"

    tok_ip = token_ip(tok)
    print("your public IP :", my_ip)
    print("cookie ip claim:", tok_ip or "(none)")
    if tok_ip and my_ip != "unknown" and tok_ip != my_ip:
        print("  -> MISMATCH. LeetCode binds the session to an IP.")
        print("     This cookie only works from the network that issued it.")
    print()

    s = requests.Session()
    s.cookies.set("LEETCODE_SESSION", tok, domain=".leetcode.com")
    s.cookies.set("csrftoken", csrf, domain=".leetcode.com")
    h = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "Origin": "https://leetcode.com",
        "x-csrftoken": csrf,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0.0.0",
    }

    ok = False
    try:
        r = s.post(GRAPHQL,
                   json={"query": "query { userStatus { username isSignedIn } }", "variables": {}},
                   headers=h, timeout=20)
        st = (r.json().get("data") or {}).get("userStatus") or {}
        if st.get("isSignedIn"):
            print("AUTH OK - logged in as", st.get("username"))
            ok = True
        else:
            print("AUTH FAILED - LeetCode does not accept this cookie from this machine.")
    except Exception as e:
        print("AUTH ERROR:", e)

    try:
        j = s.get("https://leetcode.com/api/problems/all/", headers=h, timeout=30).json()
        ac = sum(1 for p in j.get("stat_status_pairs", []) if p.get("status") == "ac")
        print(f"solved problems visible: {j.get('num_solved')} (ac={ac})")
        if ac:
            ok = True
    except Exception as e:
        print("FETCH ERROR:", e)

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
