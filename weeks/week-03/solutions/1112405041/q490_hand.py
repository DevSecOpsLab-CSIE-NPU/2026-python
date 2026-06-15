# 490.py
import sys

def solve():
    # 讀取所有輸入行，保留原始內容
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # 1. 找出最長行的長度
    max_len = 0
    for line in lines:
        max_len = max(max_len, len(line))

    # 2. 旋轉邏輯：
    # 目標是最後一行變第一列，第一行變最後一列。
    # 遍歷每一列 (j 從 0 到 max_len-1)
    for j in range(max_len):
        output_row = []
        # 遍歷每一行 (i 從最後一行往第一行)
        for i in range(len(lines) - 1, -1, -1):
            # UVA 490 地雷：如果這行不夠長，必須補空格，不能直接略過
            if j < len(lines[i]):
                output_row.append(lines[i][j])
            else:
                output_row.append(' ')

        # 直接印出結果
        print("".join(output_row))

if __name__ == "__main__":
    solve()
