import subprocess
from pathlib import Path


BASE = Path(__file__).resolve().parent
PY = "c:/Users/User/Desktop/python/.venv/Scripts/python.exe"
TARGET = BASE / "10056-easy-zh.py"


def main() -> None:
    given_input = "2\n3 0.1666666667 1\n3 0.1666666667 2\n"
    expected = "0.3956\n0.3297"

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
    print("PASS test_10056")


if __name__ == "__main__":
    main()
