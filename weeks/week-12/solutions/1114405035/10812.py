import sys

# 手打程式版本 - 10812 Beat the Spread!
# 繁體中文註解說明

def get_scores(s, d):
    """
    依據總和 S 與差值 D 計算兩隊各自的得分。
    若無非負整數解則回傳 None。
    """
    # 差值絕對值不可能大於總和，且兩數相加必須能被 2 整除以獲得整數
    if s < d or (s + d) % 2 != 0:
        return None
    a = (s + d) // 2
    b = (s - d) // 2
    return a, b

def solve():
    # 讀取標準輸入並以行拆分
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    try:
        # 第一行代表測試資料組數
        n = int(lines[0].strip())
    except ValueError:
        return

    # 依序處理每一組測資
    for i in range(1, n + 1):
        if i >= len(lines):
            break
        parts = lines[i].split()
        if not parts:
            continue
        s = int(parts[0])
        d = int(parts[1])
        
        result = get_scores(s, d)
        if result is not None:
            print(f"{result[0]} {result[1]}")
        else:
            print("impossible")

if __name__ == "__main__":
    solve()
