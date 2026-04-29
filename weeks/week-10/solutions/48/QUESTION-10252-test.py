import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
TARGET = BASE / "QUESTION-10252.py"

INPUT_DATA = """2
3
0 0
1 1
2 2
2
0 0
2 2
"""

EXPECTED_OUTPUT = """4 1
4 9""".strip()


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
