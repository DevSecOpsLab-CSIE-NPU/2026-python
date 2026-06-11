import sys


# UVA 11349 - Symmetric Matrix
# 本檔案為完整版解法，從 stdin 讀取多組測資，輸出每組是否為 "中心對稱且所有元素非負" 的結果。
# 輸入範例（多組）：
# T
# N = n
# matrix row1
# ...
# 判斷條件：
# 1) 所有元素皆 >= 0
# 2) 對所有 (i,j) 有 M[i][j] == M[n-1-i][n-1-j] （注意索引為 0-based）


def solve():
    # 讀取全部輸入並逐行處理，方便處理可能會有空白行的情況
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    # 第一行為測資數量 T
    t = int(data[0].strip())
    idx = 1
    out_lines = []

    for case in range(1, t + 1):
        # 跳過可能的空白行（安全性）
        while idx < len(data) and data[idx].strip() == "":
            idx += 1

        # 讀取像是 "N = 3" 的行，或可能直接是數字
        head = data[idx].strip()
        idx += 1
        if '=' in head:
            # 以等號分割，取右側並轉為 int
            n = int(head.split('=')[1].strip())
        else:
            n = int(head)

        # 讀入矩陣 n 行，每行 n 個整數
        mat = []
        for _ in range(n):
            row = list(map(int, data[idx].split()))
            idx += 1
            mat.append(row)

        # 檢查是否符合題意（非負 + 中心對稱）
        sym = True
        for i in range(n):
            for j in range(n):
                # 若發現負數或與對稱位置不同就直接判為 Non-symmetric
                if mat[i][j] < 0 or mat[i][j] != mat[n - 1 - i][n - 1 - j]:
                    sym = False
                    break
            if not sym:
                break

        if sym:
            out_lines.append(f"Test #{case}: Symmetric.")
        else:
            out_lines.append(f"Test #{case}: Non-symmetric.")

    # 一次輸出所有結果（維持輸出格式）
    sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
    solve()
