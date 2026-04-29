"""QUESTION-10235 測試程式"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGETS = [
    BASE_DIR / "10235.py",
    BASE_DIR / "10235_easy.py",
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
    # 測試用例
    case1_input = "13\n31\n37\n"
    case1_expected = "13 emirp\n31 emirp\n37 emirp"

    tests = [
        ("emirps", case1_input, case1_expected),
    ]

    all_passed = True

    for target in TARGETS:
        print(f"=== 測試 {target.name} ===")
        for name, inp, expected in tests:
            actual = run_program(target, inp)
            ok = actual == expected
            print(f"[{name}] {'PASS' if ok else 'FAIL'}")
            if not ok:
                all_passed = False
                print("預期:", expected)
                print("實際:", actual)
        print()

    if all_passed:
        print("全部測試通過")
    else:
        print("有測試失敗")
        sys.exit(1)


if __name__ == "__main__":
    main()
