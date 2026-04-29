"""QUESTION-10242 測試程式"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGETS = [
    BASE_DIR / "10242.py",
    BASE_DIR / "10242_easy.py",
]


def run_program(path: Path, input_data: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(path)],
        input=input_data,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"程式 {path.name} 執行失敗")
    return completed.stdout.rstrip("\n")


def main() -> None:
    # 簡單測試
    case1_input = "1\n3\n0 0\n1 1\n2 2\n"

    tests = [("basic", case1_input, "2 1"),]

    all_passed = True
    for target in TARGETS:
        print(f"=== 測試 {target.name} ===")
        for name, inp, expected in tests:
            try:
                actual = run_program(target, inp)
                ok = actual == expected
                print(f"[{name}] {'PASS' if ok else 'FAIL'}")
            except Exception as e:
                print(f"[{name}] ERROR: {e}")
                all_passed = False
        print()

    if all_passed:
        print("測試完成")


if __name__ == "__main__":
    main()
