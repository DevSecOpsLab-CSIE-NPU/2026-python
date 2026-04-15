"""
測試 q10221_handtyped.py
執行方式: python test_q10221.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SOLUTION = Path(__file__).with_name("q10221_handtyped.py")


def run_case(case_name: str, case_input: str, expected: str) -> bool:
    proc = subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=case_input,
        text=True,
        capture_output=True,
        check=False,
    )

    actual = proc.stdout.strip()
    expected = expected.strip()

    print(f"===== {case_name} =====")
    print(f"Return code: {proc.returncode}")

    if proc.stderr:
        print("stderr:")
        print(proc.stderr)

    if proc.returncode != 0:
        print("RESULT: FAIL (程式非正常結束)")
        return False

    if actual != expected:
        print("RESULT: FAIL (輸出不一致)")
        print("--- expected ---")
        print(expected)
        print("--- actual ---")
        print(actual)
        return False

    print("RESULT: PASS")
    return True


def main() -> None:
    cases = [
        (
            "problem-sample-3lines",
            """500 30 deg
700 60 min
200 45 deg
""",
            """3633.775503 3592.408346
124.616509 124.614927
5215.043805 5082.035982""",
        ),
        (
            "angle-over-180",
            """100 300 deg
""",
            "6848.671985 6540.000000",
        ),
        (
            "zero-angle",
            """0 0 deg
""",
            "0.000000 0.000000",
        ),
    ]

    ok = True
    pass_count = 0

    for name, inp, exp in cases:
        passed = run_case(name, inp, exp)
        ok = ok and passed
        if passed:
            pass_count += 1

    print("===== SUMMARY =====")
    print(f"TOTAL: {len(cases)}")
    print(f"PASS: {pass_count}")

    if ok:
        print("ALL TESTS PASSED")
        sys.exit(0)

    print("SOME TESTS FAILED")
    sys.exit(1)


if __name__ == "__main__":
    main()
