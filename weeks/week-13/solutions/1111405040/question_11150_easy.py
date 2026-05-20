"""
UVA 11150 Cola 簡單版。
"""

from __future__ import annotations


def drink_all(start: int) -> int:
    """直接套用這題常見的化簡公式。"""
    return start + start // 2


def solve(data: str) -> str:
    """逐行處理輸入。"""
    answers = [str(drink_all(int(token))) for token in data.split()]
    return "\n".join(answers)


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
