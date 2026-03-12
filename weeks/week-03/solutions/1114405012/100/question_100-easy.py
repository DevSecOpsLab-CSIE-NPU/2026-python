"""
UVA 100 - The 3n+1 Problem（easy 版本）

這份程式刻意寫得「好背、好記、好教學」：
- 函式名稱短而直覺
- 邏輯分成三步：算一個、算區間、格式輸出
- 保留必要快取，速度夠用又不難懂
"""

from __future__ import annotations

# 快取：記住算過的答案（1 的答案固定是 1）
memo = {1: 1}


def collatz_len(n: int) -> int:
    """
    回傳 n 的 Collatz 長度（含 n 與 1）。

    易記口訣：
    奇數變 3n+1，偶數除以 2，直到變成 1。
    """
    if n <= 0:
        raise ValueError("n 必須是正整數")

    if n in memo:
        return memo[n]

    if n % 2 == 1:
        ans = 1 + collatz_len(3 * n + 1)
    else:
        ans = 1 + collatz_len(n // 2)

    memo[n] = ans
    return ans


def max_len(i: int, j: int) -> int:
    """回傳 [min(i,j), max(i,j)] 內的最大 Collatz 長度。"""
    if i <= 0 or j <= 0:
        raise ValueError("i, j 必須是正整數")

    a, b = min(i, j), max(i, j)
    best = 0
    for x in range(a, b + 1):
        best = max(best, collatz_len(x))
    return best


def solve_line(i: int, j: int) -> str:
    """把單筆查詢轉成題目要求字串。"""
    return f"{i} {j} {max_len(i, j)}"


def solve_all(text: str) -> str:
    """處理多行輸入，回傳多行輸出。"""
    out = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        i_str, j_str = line.split()
        out.append(solve_line(int(i_str), int(j_str)))
    return "\n".join(out)


def reset_memo_easy() -> None:
    """測試前可呼叫此函式重設快取。"""
    memo.clear()
    memo[1] = 1


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data.strip():
        print(solve_all(data))
