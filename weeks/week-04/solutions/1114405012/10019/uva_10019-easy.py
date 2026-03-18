from __future__ import annotations

import sys


def solve(data: str) -> str:
    """
    UVA 10019（依題目敘述內容）easy 版

    題目非常直接：
    每次讀兩個整數，輸出它們的差距（絕對值）。

    Python 的 int 可以處理很大的整數，
    所以直接用 abs(a - b) 就好。
    """
    tokens = data.split()
    if len(tokens) < 2:
        return ""

    ans: list[str] = []

    # 每兩個數字是一筆資料：
    # (tokens[0], tokens[1])、(tokens[2], tokens[3])...
    i = 0
    while i + 1 < len(tokens):
        a = int(tokens[i])
        b = int(tokens[i + 1])

        # 題目要輸出正差值，使用 abs() 最直觀
        ans.append(str(abs(a - b)))
        i += 2

    # 每筆答案各佔一行
    return "\n".join(ans)


def main() -> None:
    content = sys.stdin.read()
    sys.stdout.write(solve(content))


if __name__ == "__main__":
    main()
