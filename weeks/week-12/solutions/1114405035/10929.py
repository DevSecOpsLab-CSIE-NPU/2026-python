import sys

# 手打程式版本 - 10929 You can say 11
# 繁體中文註解說明

def is_multiple_of_11(n_str):
    """
    使用「奇數位數之和」與「偶數位數之和」的差值來判斷是否為 11 的倍數。
    """
    odd_sum = 0
    even_sum = 0
    
    # 遍歷字串的每個字元，並區分奇數索引與偶數索引
    for i, char in enumerate(n_str):
        if i % 2 == 0:
            odd_sum += int(char)
        else:
            even_sum += int(char)
            
    # 計算絕對值差
    diff = abs(odd_sum - even_sum)
    return diff % 11 == 0

def solve():
    # 讀取標準輸入
    for line in sys.stdin:
        n_str = line.strip()
        
        # 結束條件
        if n_str == '0':
            break
            
        if not n_str:
            continue
            
        if is_multiple_of_11(n_str):
            print(f"{n_str} is a multiple of 11.")
        else:
            print(f"{n_str} is not a multiple of 11.")

if __name__ == "__main__":
    solve()
