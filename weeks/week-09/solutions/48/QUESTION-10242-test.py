import subprocess
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent
TARGET = BASE / "QUESTION-10242.py"

INPUT_DATA = """6 7
1 2
2 3
3 5
2 4
4 1
4 6
6 5
10
12
8
16
1
5
1 1
5
"""

EXPECTED_OUTPUT = "47"


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
