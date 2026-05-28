"""
AI 簡易版本：UVA 11349 — Symmetric Matrix

說明：
- 讀取多組測資，格式範例同題目（第一行為 T，之後每組有一行 'N = n' 或直接 n，接著 n 行矩陣）。
- 判斷矩陣是否每個元素非負且對中心 (center) 對稱。
- 輸出每組結果為 "Test #k: Symmetric." 或 "Test #k: Non-symmetric."。

此版本以簡潔易懂為主，整段程式皆以繁體中文註解。
"""

from typing import List


def is_center_symmetric(matrix: List[List[int]]) -> bool:
    """檢查矩陣所有元素是否非負，且關於中心位置對稱。"""
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            v = matrix[i][j]
            if v < 0:
                return False
            if v != matrix[n - 1 - i][n - 1 - j]:
                return False
    return True


def solve() -> None:
    import sys

    data = [line.strip() for line in sys.stdin if line.strip()]
    if not data:
        return
    t = int(data[0])
    idx = 1
    case_no = 1
    out_lines = []
    while case_no <= t and idx < len(data):
        header = data[idx]
        idx += 1
        if '=' in header:
            n = int(header.split('=')[1].strip())
        else:
            n = int(header)
        mat = []
        for _ in range(n):
            row = list(map(int, data[idx].split()))
            mat.append(row)
            idx += 1
        if is_center_symmetric(mat):
            out_lines.append(f"Test #{case_no}: Symmetric.")
        else:
            out_lines.append(f"Test #{case_no}: Non-symmetric.")
        case_no += 1

    print('\n'.join(out_lines))


if __name__ == '__main__':
    solve()
