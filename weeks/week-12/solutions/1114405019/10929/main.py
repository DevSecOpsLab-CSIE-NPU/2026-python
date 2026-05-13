import sys

# 題目：UVA 10929 - You can say 11
# 題目說明：判斷一個正整數 N 是否為 11 的倍數。
# N 的位數最多可達 1000 位。
# 解題邏輯：
# 一個數是否為 11 的倍數，可以用「奇數位數字之和」與「偶數位數字之和」的差來判斷。
# 若 (奇數位和 - 偶數位和) 能被 11 整除（包括 0），則該數為 11 的倍數。

def solve():
    # 逐行讀取標準輸入
    for line in sys.stdin:
        # 去除行末換行符號及前後空白
        n_str = line.strip()
        
        # 若輸入為 "0"，代表結束輸入
        if n_str == "0":
            break
        
        # 為了處理可能出現的空行
        if not n_str:
            continue
            
        odd_sum = 0   # 儲存奇數位數字之和 (索引 0, 2, 4...)
        even_sum = 0  # 儲存偶數位數字之和 (索引 1, 3, 5...)
        
        # 遍歷字串中的每個字元
        for i in range(len(n_str)):
            digit = int(n_str[i])
            if i % 2 == 0:
                odd_sum += digit
            else:
                even_sum += digit
        
        # 計算兩者之差的絕對值
        diff = abs(odd_sum - even_sum)
        
        # 判斷差值是否能被 11 整除
        if diff % 11 == 0:
            print(f"{n_str} is a multiple of 11.")
        else:
            print(f"{n_str} is not a multiple of 11.")

if __name__ == "__main__":
    solve()
