"""
測試 q10189_handtyped.py
執行方式: python test_q10189.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SOLUTION = Path(__file__).with_name("q10189_handtyped.py")


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
            "sample-from-problem",
            """4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
""",
            """Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100""",
        ),
        (
            "single-cell-empty",
            """1 1
.
0 0
""",
            """Field #1:
0""",
        ),
        (
            "single-cell-mine",
            """1 1
*
0 0
""",
            """Field #1:
*""",
        ),
    ]

    ok = True
    pass_count = 0
    for name, inp, exp in cases:
        passed = run_case(name, inp, exp)
        ok = passed and ok
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
