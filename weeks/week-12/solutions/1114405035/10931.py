import sys

# 手打程式版本 - 10931 Parity
# 繁體中文註解說明

def to_binary_and_parity(n):
    """
    手動將正整數轉換為二進位字串並計算 1 的個數（即 Parity）。
    """
    bits = []
    parity = 0
    temp = n
    
    # 透過除以 2 取餘數的方式手動做進位制轉換
    while temp > 0:
        bit = temp % 2
        bits.append(str(bit))
        if bit == 1:
            parity += 1
        temp //= 2
        
    # 因為是由低位到高位取出，所以要反轉字串
    bits.reverse()
    return "".join(bits), parity

def solve():
    # 讀取標準輸入
    for line in sys.stdin:
        line = line.strip()
        
        # 結束條件
        if not line or line == '0':
            break
            
        try:
            n = int(line)
        except ValueError:
            continue
            
        # 計算二進位與 Parity 數值
        b_str, p = to_binary_and_parity(n)
        
        # 輸出結果
        print(f"The parity of {b_str} is {p} (mod 2).")

if __name__ == "__main__":
    solve()
