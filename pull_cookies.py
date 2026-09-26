#!/usr/bin/env python3
"""Read the LeetCode cookies straight out of your browser and verify them.

No pasting anywhere:

    python pull_cookies.py
"""
import os
import sys

import browser_cookie3

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = os.path.join(HERE, ".env")
GRAPHQL = "https://leetcode.com/graphql"
WANT = {"LEETCODE_SESSION", "csrftoken"}

LOADERS = [
    ("chrome", browser_cookie3.chrome),
    ("edge", browser_cookie3.edge),
    ("brave", browser_cookie3.brave),
    ("firefox", browser_cookie3.firefox),
]


def harvest():
    found = {}
    for name, fn in LOADERS:
        try:
            jar = fn(domain_name="leetcode.com")
        except Exception as e:
            print(f"  {name}: unavailable ({type(e).__name__}: {e})")
            continue
        for c in jar:
            if c.name in WANT and c.value and c.name not in found:
                found[c.name] = c.value
                print(f"  {name}: got {c.name} ({len(c.value)} chars)")
        if WANT <= set(found):
            break
    return found


def main():
    print("Reading browser cookie store...")
    cookies = harvest()

    missing = WANT - set(cookies)
    if missing:
        print(f"\nFAIL: could not read {sorted(missing)} from any browser.")
        print("Log into https://leetcode.com once in Chrome, then retry.")
        sys.exit(1)

    with open(ENV, "w", encoding="utf-8") as f:
        f.write(f"LEETCODE_SESSION={cookies['LEETCODE_SESSION']}\n")
        f.write(f"LEETCODE_CSRF_TOKEN={cookies['csrftoken']}\n")
    print(f"\nWrote {ENV}")

    import verify_session

    verify_session.load_env()
    os.environ["LEETCODE_SESSION"] = cookies["LEETCODE_SESSION"]
    os.environ["LEETCODE_CSRF_TOKEN"] = cookies["csrftoken"]
    verify_session.main()


if __name__ == "__main__":
    main()
