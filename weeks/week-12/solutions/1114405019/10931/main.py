import sys

# 題目：UVA 10931 - Parity
# 題目說明：給定一個整數 I，將其轉換為二進位表示 B，並計算其中 1 的個數 P。
# 依照格式輸出 "The parity of B is P (mod 2)."
# 輸入範圍：1 ≤ I ≤ 2,147,483,647，當 I=0 時結束。

def solve():
    # 逐行讀取標準輸入
    for line in sys.stdin:
        # 去除前後空白並轉換為整數
        line = line.strip()
        if not line:
            continue
            
        try:
            i_val = int(line)
        except ValueError:
            continue
            
        # 如果輸入為 0，代表結束
        if i_val == 0:
            break
            
        # 使用 bin() 函數轉換為二進位，bin(5) 會得到 '0b101'
        # 我們需要去掉前導的 '0b'，所以從索引 2 開始切片
        binary_str = bin(i_val)[2:]
        
        # 使用 count('1') 計算字串中 '1' 出現的次數
        parity_count = binary_str.count('1')
        
        # 依照題目要求格式輸出結果
        print(f"The parity of {binary_str} is {parity_count} (mod 2).")

if __name__ == "__main__":
    solve()
