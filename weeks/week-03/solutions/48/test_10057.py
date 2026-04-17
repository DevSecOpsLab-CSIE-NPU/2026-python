import subprocess
from pathlib import Path


BASE = Path(__file__).resolve().parent
PY = "c:/Users/User/Desktop/python/.venv/Scripts/python.exe"
TARGET = BASE / "10057-easy-zh.py"


def main() -> None:
    given_input = "4\n1\n2\n2\n4\n2\n10\n20\n"
    expected = "2 2 1\n10 2 11"

    proc = subprocess.run(
        [PY, str(TARGET)],
        input=given_input,
        text=True,
        capture_output=True,
        check=False,
    )

    got = proc.stdout.strip()
    assert proc.returncode == 0, proc.stderr
    assert got == expected, f"expected={expected!r}, got={got!r}"
    print("PASS test_10057")


if __name__ == "__main__":
    main()
