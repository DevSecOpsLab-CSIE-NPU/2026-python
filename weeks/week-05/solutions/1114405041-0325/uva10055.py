"""UVA 10055 - Hashmat the Brave Warrior（主解法）。

題意：每行輸入兩個整數，輸出兩者絕對差。
輸入直到 EOF 結束。
"""

from __future__ import annotations


def absolute_difference(a: int, b: int) -> int:
    """回傳兩數的絕對差。"""
    return abs(a - b)


def solve_io(data: str) -> str:
    tokens = data.split()
    answers: list[str] = []

    # 每兩個 token 為一組資料。
    for i in range(0, len(tokens), 2):
        a = int(tokens[i])
        b = int(tokens[i + 1])
        answers.append(str(absolute_difference(a, b)))

    return "\n".join(answers)


def main() -> None:
    import sys

    output = solve_io(sys.stdin.read())
    if output:
        print(output)


if __name__ == "__main__":
    main()
