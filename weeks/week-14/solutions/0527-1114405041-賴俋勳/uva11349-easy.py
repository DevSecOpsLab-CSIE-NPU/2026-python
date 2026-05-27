# UVA 11349（好記版）
# 核心口訣：
# 1) 不能有負數
# 2) 每個位置要等於「中心對面」的位置

import sys


def is_ok(mat):
    # 用雙層迴圈檢查每一格
    n = len(mat)
    for i in range(n):
        for j in range(n):
            # 條件一：元素不可為負
            if mat[i][j] < 0:
                return False
            # 條件二：中心對稱
            if mat[i][j] != mat[n - 1 - i][n - 1 - j]:
                return False
    return True


def solve(text):
    # 先把空行去掉，方便逐行讀
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    t = int(lines[0])
    p = 1
    ans = []

    for case_id in range(1, t + 1):
        # 讀取 "N = n"
        n = int(lines[p].split('=')[1].strip())
        p += 1

        # 讀矩陣
        mat = []
        for _ in range(n):
            mat.append(list(map(int, lines[p].split())))
            p += 1

        # 判斷結果
        if is_ok(mat):
            ans.append(f"Test #{case_id}: Symmetric.")
        else:
            ans.append(f"Test #{case_id}: Non-symmetric.")

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
