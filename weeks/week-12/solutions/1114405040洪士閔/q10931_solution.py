"""
題目 10931 - Parity

問題：計算整數的二進位表示中 1 的個數（奇偶性）

解法：
- 轉換為二進位
- 計數 '1' 的個數
"""


def calculate_parity(num):
    """
    計算一個整數的奇偶性（二進位中 1 的個數）。
    
    參數：
        num (int): 整數
    
    返回：
        tuple: (二進位表示字符串, 1 的個數)
    """
    # 轉換為二進位（移除 '0b' 前綴）
    binary = bin(num)[2:]
    
    # 計數 '1' 的個數
    parity = binary.count('1')
    
    return (binary, parity)


def main():
    """
    主程式：讀取輸入，計算奇偶性。
    """
    # 讀取輸入，直到遇到 0
    while True:
        # 讀取一個整數
        i = int(input())
        
        # 當輸入為 0 時停止
        if i == 0:
            break
        
        # 計算二進位和奇偶性
        binary, parity = calculate_parity(i)
        
        # 輸出結果
        print(f"The parity of {binary} is {parity} (mod 2).")


if __name__ == "__main__":
    main()
