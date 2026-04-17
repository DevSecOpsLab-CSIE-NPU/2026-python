import subprocess
from pathlib import Path


BASE = Path(__file__).resolve().parent
PY = "c:/Users/User/Desktop/python/.venv/Scripts/python.exe"
TARGET = BASE / "10041-easy-zh.py"


def main() -> None:
    given_input = "2\n2 2 4\n3 2 4 6\n"
    expected = "2\n4"

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
    print("PASS test_10041")


if __name__ == "__main__":
    main()
