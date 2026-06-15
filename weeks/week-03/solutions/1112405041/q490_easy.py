# 490-easy.py
# UVA 490：文字旋轉 (簡單版)
# 核心邏輯：用二維陣列（矩陣）的概念來思考旋轉

import sys

def solve():
    # 1. 讀入所有行，放進一個清單裡
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # 2. 找出最長的那一行有多長，這決定了輸出的總行數
    max_len = 0
    for line in lines:
        if len(line) > max_len:
            max_len = len(line)

    # 3. 旋轉邏輯：
    # 原本的「列」索引是 i，原本的「欄」索引是 j
    # 輸出時，外層跑「欄」(j)，內層跑「列」(i)
    # 關鍵：UVA 的旋轉是最後一行變成第一列，所以 i 要從最後面往回跑
    for j in range(max_len):
        output_row = []
        for i in range(len(lines) - 1, -1, -1):
            # 如果目前這行不夠長，就補空白
            if j < len(lines[i]):
                output_row.append(lines[i][j])
            else:
                output_row.append(' ')

        # 組合成字串並印出
        print("".join(output_row))

if __name__ == "__main__":
    solve()
