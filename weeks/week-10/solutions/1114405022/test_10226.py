"""QUESTION-10226 測試程式

用途：
- 自動測試一般版 10226.py
- 自動測試簡單版 10226_easy.py
- 顯示每組測試是否通過
"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGETS = [
    BASE_DIR / "10226.py",
    BASE_DIR / "10226_easy.py",
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
        raise RuntimeError(
            f"程式 {path.name} 執行失敗，return code={completed.returncode}\n"
            f"stderr:\n{completed.stderr}"
        )
    return completed.stdout.rstrip("\n")


def main() -> None:
    # Case 1：一般多樹種統計
    case1_input = (
        "1\n"
        "\n"
        "Oak\n"
        "Pine\n"
        "Oak\n"
        "Maple\n"
        "Pine\n"
        "Oak\n"
    )
    case1_expected = "\n".join(
        [
            "Maple 16.6667",
            "Oak 50.0000",
            "Pine 33.3333",
        ]
    )

    # Case 2：單一樹種 100%
    case2_input = (
        "1\n"
        "\n"
        "Red Maple\n"
        "Red Maple\n"
        "Red Maple\n"
    )
    case2_expected = "Red Maple 100.0000"

    # Case 3：多測資 + 大小寫視為不同字串
    case3_input = (
        "2\n"
        "\n"
        "oak\n"
        "Oak\n"
        "oak\n"
        "\n"
        "Beech\n"
        "Ash\n"
        "Beech\n"
    )
    case3_expected = "\n\n".join(
        [
            "\n".join(
                [
                    "Oak 33.3333",
                    "oak 66.6667",
                ]
            ),
            "\n".join(
                [
                    "Ash 33.3333",
                    "Beech 66.6667",
                ]
            ),
        ]
    )

    tests = [
        ("case1", case1_input, case1_expected),
        ("case2", case2_input, case2_expected),
        ("case3", case3_input, case3_expected),
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
                print("--- 預期輸出 ---")
                print(expected)
                print("--- 實際輸出 ---")
                print(actual)
        print()

    if all_passed:
        print("全部測試通過")
    else:
        print("有測試失敗")
        sys.exit(1)


if __name__ == "__main__":
    main()

