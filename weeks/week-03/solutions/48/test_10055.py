import subprocess
from pathlib import Path


BASE = Path(__file__).resolve().parent
PY = "c:/Users/User/Desktop/python/.venv/Scripts/python.exe"
TARGET = BASE / "10055-easy-zh.py"


def main() -> None:
    given_input = "5 6\n2 1 5\n1 2\n2 1 3\n1 4\n2 1 5\n2 4 4\n"
    expected = "0\n1\n0\n1"

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
    print("PASS test_10055")


if __name__ == "__main__":
    main()
