import sys

# 優化版：使用迭代而非遞迴計算各位數之和，減少函數呼叫開銷
def solve():
    for line in sys.stdin:
        n_str = line.strip()
        if n_str == "0": break
        if not n_str: continue
        
        # 初始檢查：如果各位數之和不能被 9 整除，則原數也不是
        current_str = n_str
        current_sum = sum(int(d) for d in current_str)
        
        if current_sum % 9 != 0:
            print(f"{n_str} is not a multiple of 9.")
            continue
            
        degree = 1
        # 若總和仍大於 9，繼續加總
        while current_sum > 9:
            current_sum = sum(int(d) for d in str(current_sum))
            degree += 1
            
        print(f"9-degree of {n_str} is {degree}.")

if __name__ == "__main__":
    solve()
