import subprocess
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent

TEST_INPUT = """4
10
10
20
40
3
1
2
3
3
2
2
2
"""

EXPECTED = """10 3 11
2 1 1
2 3 1
""".strip()


def run_case(target: str) -> str:
    proc = subprocess.run(
        [sys.executable, str(BASE / target)],
        input=TEST_INPUT,
        text=True,
        capture_output=True,
        check=True,
    )
    return proc.stdout.strip()


def main() -> None:
    easy_out = run_case("QUESTION-10057-easy.py")
    hand_out = run_case("QUESTION-10057-hand.py")

    print("QUESTION-10057 測試紀錄")
    print("========================")
    print("[輸入]")
    print(TEST_INPUT.strip())
    print()
    print("[預期輸出]")
    print(EXPECTED)
    print()
    print("[Easy 版輸出 QUESTION-10057-easy.py]")
    print(easy_out)
    print()
    print("[手打版輸出 QUESTION-10057-hand.py]")
    print(hand_out)
    print()
    print("[比對結果]")
    print(f"Easy版: {'PASS' if easy_out == EXPECTED else 'FAIL'}")
    print(f"手打版: {'PASS' if hand_out == EXPECTED else 'FAIL'}")


if __name__ == "__main__":
    main()
