#!/usr/bin/env python3
"""
service_test.py — Functional tests for Bee-Path.

Tests that:
1. The HTTP service responds on port 80.
2. The index page is reachable.
3. The /cgi-bin/ path exists (returns something other than connection refused).

Exit codes:
    0 = all tests passed
    1 = one or more tests failed
"""

import os
import sys
import urllib.request
import urllib.error

TARGET = os.environ.get("TARGET_IP", "192.168.56.10")
PORT   = os.environ.get("TARGET_PORT", "80")
BASE   = f"http://{TARGET}:{PORT}"

passed = 0
failed = 0


def check(label: str, url: str, expected_codes: list[int]) -> None:
    global passed, failed
    try:
        req  = urllib.request.Request(url)
        resp = urllib.request.urlopen(req, timeout=5)
        code = resp.getcode()
    except urllib.error.HTTPError as e:
        code = e.code
    except Exception as e:
        print(f"  [FAIL] {label} — connection error: {e}")
        failed += 1
        return

    if code in expected_codes:
        print(f"  [PASS] {label} — HTTP {code}")
        passed += 1
    else:
        print(f"  [FAIL] {label} — expected {expected_codes}, got {code}")
        failed += 1


print(f"[*] Running service tests against {BASE}\n")

check("Index page reachable",    f"{BASE}/",         [200, 403])
check("CGI-bin path accessible", f"{BASE}/cgi-bin/", [200, 403, 404])

print(f"\nResults: {passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
