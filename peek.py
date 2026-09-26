import os
import sqlite3
import shutil
import tempfile

DB = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Network\Cookies")
tmp = os.path.join(tempfile.gettempdir(), "lc_cookies_read.db")

rows = []
err = None
# try a direct read-only open first (Chrome keeps the file locked for writes only)
try:
    uri = "file:" + DB.replace("\\", "/") + "?mode=ro"
    c = sqlite3.connect(uri, uri=True)
    rows = c.execute(
        "select name, value, hex(substr(encrypted_value,1,3)), length(encrypted_value) "
        "from cookies where host_key like '%leetcode%'").fetchall()
    c.close()
except Exception as e:
    err = e

if not rows and err:
    # fall back to whatever copy we can get
    try:
        shutil.copyfile(DB, tmp)
        c = sqlite3.connect(tmp)
        rows = c.execute(
            "select name, value, hex(substr(encrypted_value,1,3)), length(encrypted_value) "
            "from cookies where host_key like '%leetcode%'").fetchall()
        c.close()
    except Exception as e2:
        print("read failed:", err, "|", e2)

print(f"leetcode cookies: {len(rows)}")
for n, v, pre, l in rows:
    print(f"  {n:22} plaintext={bool(v)} prefix={pre} enc_len={l}")

if rows:
    print("\nverdict:", "v10 (DPAPI, readable without admin)" if rows[0][2] == "763130" else f"prefix {rows[0][2]} (not plain DPAPI)")
