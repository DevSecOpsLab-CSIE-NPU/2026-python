"""
UVA 100 手打版（簡單好記）

這份是依照 easy 邏輯手動重打一遍。
重點：
1. collatz 長度用遞迴 + 快取
2. 區間取最大值
3. 輸出保留原始 i, j 順序
"""

memo = {1: 1}


def collatz_len(n: int) -> int:
    """計算 n 的 cycle length（含 n 與 1）。"""
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


def range_max(i: int, j: int) -> int:
    """計算 [min(i,j), max(i,j)] 範圍的最大 cycle length。"""
    if i <= 0 or j <= 0:
        raise ValueError("i, j 必須是正整數")

    a, b = min(i, j), max(i, j)
    best = 0
    for x in range(a, b + 1):
        best = max(best, collatz_len(x))
    return best


def solve_line(i: int, j: int) -> str:
    """輸出單筆答案：i j max_cycle。"""
    return f"{i} {j} {range_max(i, j)}"


def solve_all(text: str) -> str:
    """處理多行輸入。"""
    out = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        i_str, j_str = line.split()
        out.append(solve_line(int(i_str), int(j_str)))
    return "\n".join(out)


def reset_memo_hand() -> None:
    """測試用：重設快取。"""
    memo.clear()
    memo[1] = 1


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data.strip():
        print(solve_all(data))
