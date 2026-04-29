import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
TARGET = BASE / "QUESTION-10235.py"

INPUT_DATA = """3
1 1
0
1 1
1
2 2
11
11
"""

EXPECTED_OUTPUT = """Case 1: 1
Case 2: 0
Case 3: 1""".strip()


def main():
    proc = subprocess.run(
        [sys.executable, str(TARGET)],
        input=INPUT_DATA,
        text=True,
        capture_output=True,
    )

    if proc.returncode != 0:
        print("FAIL: program crashed")
        print(proc.stderr)
        sys.exit(1)

    actual = proc.stdout.strip()
    if actual == EXPECTED_OUTPUT:
        print("PASS")
    else:
        print("FAIL: output mismatch")
        print("--- Expected ---")
        print(EXPECTED_OUTPUT)
        print("--- Actual ---")
        print(actual)
        sys.exit(1)


if __name__ == "__main__":
    main()
