import sys

# AI 建議的簡單版本 - 10922 2 the 9s
# 繁體中文註解說明

def solve():
    """
    主要解題函數，判斷 9 的倍數與計算 9-degree
    """
    for line in sys.stdin:
        # 去除行尾換行符號
        n_str = line.strip()
        
        # 如果輸入為 "0"，則結束程式
        if n_str == '0':
            break
        
        # 計算初步的位數和
        current_sum = sum(int(d) for d in n_str)
        
        # 如果初步位數和不能被 9 整除，則原數也不是 9 的倍數
        if current_sum % 9 != 0:
            print(f"{n_str} is not a multiple of 9.")
        else:
            # 初始深度為 1
            degree = 1
            
            # 只要位數和仍是大於 9 的多位數，就繼續計算位數和
            temp_sum = current_sum
            while temp_sum > 9:
                # 將目前的和轉成字串，再計算其各位數字之和
                temp_sum = sum(int(d) for d in str(temp_sum))
                # 每計算一次，深度加 1
                degree += 1
            
            # 輸出結果
            print(f"{n_str} is a multiple of 9 and has 9-degree {degree}.")

if __name__ == "__main__":
    solve()
