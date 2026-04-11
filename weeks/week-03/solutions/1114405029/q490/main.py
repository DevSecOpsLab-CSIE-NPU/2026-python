import sys

# 進階實作版：利用巢狀迴圈處理不等長字串矩陣
# 核心邏輯：將字串列表視為二維陣列，進行坐標轉換 (r, c) -> (c, n-1-r)
def solve():
    # 讀取所有輸入行
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # 找出所有行當中的最大長度
    max_len = 0
    for line in lines:
        if len(line) > max_len:
            max_len = len(line)

    # 旋轉後的總行數由 max_len 決定
    for j in range(max_len):
        # 每一列的字元來自輸入行的由後往前掃描
        output_line = []
        for i in range(len(lines) - 1, -1, -1):
            # 如果目前的輸入行長度足夠，就取該字元
            if j < len(lines[i]):
                output_line.append(lines[i][j])
            else:
                # 若長度不足，補空格以維持矩形結構
                output_line.append(' ')
        
        # 輸出處理好的這一行並換行
        print("".join(output_line))

if __name__ == "__main__":
    solve()