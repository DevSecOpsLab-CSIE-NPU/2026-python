"""
UVA 11349 — Symmetric Matrix 的簡單版。

這一版的目標是把題目規則濃縮成最容易記憶的形式：
1. 先檢查每個數字是不是都 >= 0。
2. 再檢查矩陣是否關於中心點完全對稱。

如果兩個條件都成立，就輸出 Symmetric，否則輸出 Non-symmetric。
"""


def is_symmetric(matrix):
    """檢查矩陣是否符合題目的對稱規則。"""
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            # 規則 1：只要出現負數，就直接判定失敗。
            if matrix[i][j] < 0:
                return False
            # 規則 2：左上角與右下角、左下角與右上角要一一對應。
            if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                return False
    return True


def solve():
    import sys

    # 先把所有非空白行讀進來，後面就可以用索引逐行處理。
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    # 第一行是測資筆數 T。
    t = int(lines[0])
    idx = 1
    ans = []

    # 一次處理一組測資。
    for case_no in range(1, t + 1):
        header = lines[idx]
        idx += 1

        # 題目有些輸入會寫成 N = 3，也有人會直接寫 3，這裡兩種都接受。
        if '=' in header:
            n = int(header.split('=')[1].strip())
        else:
            n = int(header)

        # 依照 n 讀入 n 行矩陣資料。
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, lines[idx].split())))
            idx += 1

        # 根據檢查結果輸出題目指定格式。
        if is_symmetric(matrix):
            ans.append(f"Test #{case_no}: Symmetric.")
        else:
            ans.append(f"Test #{case_no}: Non-symmetric.")

    # 一次印出所有結果，格式與題目一致。
    print('\n'.join(ans))


if __name__ == '__main__':
    solve()
