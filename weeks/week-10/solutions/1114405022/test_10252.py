"""QUESTION-10252 測試程式"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGETS = [
    BASE_DIR / "10252.py",
    BASE_DIR / "10252_easy.py",
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
    test_input = "abcd dcba\naab bbb\n"
    
    tests = [("common", test_input, "abcd\nb"),]

    for target in TARGETS:
        print(f"=== 測試 {target.name} ===")
        for name, inp, expected in tests:
            actual = run_program(target, inp)
            ok = actual == expected
            print(f"[{name}] {'PASS' if ok else 'FAIL'}")


if __name__ == "__main__":
    main()
