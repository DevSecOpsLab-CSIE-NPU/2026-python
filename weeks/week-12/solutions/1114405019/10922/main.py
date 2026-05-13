import sys

# 題目：UVA 10922 - 2 the 9s
# 題目說明：判斷一個數字是否為 9 的倍數，若是，計算其「9 的深度 (9-degree)」。
# 9 的深度定義：重複將各位數數字加總，直到結果為 9 所需的次數。

def get_nine_degree(n_str):
    """
    遞迴計算 9 的深度
    n_str: 目前數字的字串形式
    """
    # 計算各位數之和
    current_sum = sum(int(digit) for digit in n_str)
    
    # 如果總和不能被 9 整除，則原數不是 9 的倍數
    if current_sum % 9 != 0:
        return 0
    
    # 基本情況：如果總和已經是 9，則深度為 1
    if current_sum == 9:
        return 1
    
    # 遞迴情況：深度為 1 + 剩餘部分的深度
    return 1 + get_nine_degree(str(current_sum))

def solve():
    # 逐行讀取輸入
    for line in sys.stdin:
        # 去除首尾空白
        n_str = line.strip()
        
        # 輸入為 "0" 時結束程式
        if n_str == "0":
            break
        
        if not n_str:
            continue
            
        degree = get_nine_degree(n_str)
        
        if degree > 0:
            print(f"{n_str} is a multiple of 9 and has 9-degree {degree}.")
        else:
            print(f"{n_str} is not a multiple of 9.")

if __name__ == "__main__":
    solve()
