import sys

# 題目：UVA 10812 - Beat the Spread!
# 題目說明：給定兩隊分數的和 S 與差的絕對值 D，求兩隊各自的得分。
# 解題邏輯：
# 設兩隊得分分別為 a 與 b (且假設 a >= b)
# 1. a + b = S (和)
# 2. a - b = D (差)
# 將兩式相加：2a = S + D => a = (S + D) / 2
# 將兩式相減：2b = S - D => b = (S - D) / 2
# 因為得分必須是「非負整數」，所以必須滿足以下條件：
# - (S + D) 必須是偶數 (否則 a 不是整數)
# - S 必須大於等於 D (否則 b 會是負數)

def solve():
    # 使用 sys.stdin.read().split() 一次讀取所有輸入並依空白分割
    # input_data 會是一個字串列表
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    # 第一個數字是測試資料組數 n
    try:
        n = int(input_data[0])
    except (ValueError, IndexError):
        return
        
    idx = 1
    # 迴圈處理每組測試資料
    for _ in range(n):
        if idx + 1 >= len(input_data):
            break
            
        try:
            # s: 分數之和
            # d: 分數之差
            s = int(input_data[idx])
            d = int(input_data[idx+1])
            idx += 2
            
            # 判斷是否有解：
            # 1. 和必須大於等於差
            # 2. 和加差的和必須是偶數 (保證能整除 2)
            if s >= d and (s + d) % 2 == 0:
                a = (s + d) // 2
                b = (s - d) // 2
                # 較大的分數先輸出
                print(f"{a} {b}")
            else:
                # 無法得到整數得分或得分為負數
                print("impossible")
        except ValueError:
            idx += 1
            continue

if __name__ == "__main__":
    solve()
