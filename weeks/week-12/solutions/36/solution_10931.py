# UVA 10931 - Parity
# 解題思路：
# 1. 將十進位數轉換為二進位
# 2. 計算二進位表示中 1 的個數（稱為奇偶性/Parity）
# 3. 輸出二進位表示和 1 的個數

def get_parity(num):
    """
    計算數字的奇偶性（二進位中 1 的個數）
    返回 (二進位字符串, 1的個數)
    """
    # 轉換為二進位（移除 '0b' 前綴）
    binary = bin(num)[2:]
    
    # 計算 1 的個數
    parity = binary.count('1')
    
    return binary, parity

def solve_parity():
    """
    求解 Parity 問題
    """
    while True:
        I = int(input())
        
        if I == 0:
            break
        
        binary, parity = get_parity(I)
        
        # 輸出格式：The parity of B is P (mod 2).
        print(f"The parity of {binary} is {parity} (mod 2).")

if __name__ == "__main__":
    solve_parity()
