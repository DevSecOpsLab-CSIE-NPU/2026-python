"""QUESTION-10268 測試程式"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGETS = [
    BASE_DIR / "10268.py",
    BASE_DIR / "10268_easy.py",
]


def run_program(path: Path, input_data: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(path)],
        input=input_data,
        text=True,
        capture_output=True,
        check=False,
    )
    return completed.stdout.rstrip("\n")


def main() -> None:
    test_input = "2 100\n2 1000000000000000000\n0 0\n"
    
    tests = [("trials", test_input, "14\nMore than 63 trials needed."),]

    for target in TARGETS:
        print(f"=== 測試 {target.name} ===")
        for name, inp, expected in tests:
            actual = run_program(target, inp)
            ok = actual == expected
            print(f"[{name}] {'PASS' if ok else 'FAIL'}")


if __name__ == "__main__":
    main()
