"""
UVA 10055 - Hashmat the Brave Warrior
"""

from __future__ import annotations


def absolute_difference(first: int, second: int) -> int:
    """回傳兩個整數的絕對差。"""
    return abs(first - second)


def solve(text: str) -> str:
    """讀到 EOF 為止，每行輸出一個絕對差。"""
    tokens = [int(token) for token in text.split()]
    results = [
        str(absolute_difference(tokens[index], tokens[index + 1]))
        for index in range(0, len(tokens), 2)
    ]
    return "\n".join(results)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
