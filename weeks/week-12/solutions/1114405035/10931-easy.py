import sys

# AI 建議的簡單版本 - 10931 Parity
# 繁體中文註解說明

def solve():
    # 逐行讀取標準輸入
    for line in sys.stdin:
        # 去除前後空白與換行符號
        line = line.strip()
        
        # 若輸入為 "0"，代表結束輸入
        if not line or line == '0':
            break
            
        n = int(line)
        
        # 使用 Python 內建的 bin() 轉換為二進位字串，並切除開頭的 "0b"
        b_str = bin(n)[2:]
        
        # 計算字串中字元 '1' 的個數
        p = b_str.count('1')
        
        # 輸出結果
        print(f"The parity of {b_str} is {p} (mod 2).")

if __name__ == "__main__":
    solve()
