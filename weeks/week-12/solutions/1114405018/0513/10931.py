"""
UVA 10931 — Parity

題目重點：
計算一個整數的「奇偶性（Parity）」，定義為其二進位表示中 1 的個數。

演算法：
1. 將整數 I 轉換為二進位字串（不含 '0b' 前綴與前導零）
2. 計算二進位字串中 '1' 的個數
3. 按照指定格式輸出

例子：
- I = 1 → 二進位 "1" → 1 個 1 → 輸出 "The parity of 1 is 1 (mod 2)."
- I = 2 → 二進位 "10" → 1 個 1 → 輸出 "The parity of 10 is 1 (mod 2)."
- I = 10 → 二進位 "1010" → 2 個 1 → 輸出 "The parity of 1010 is 2 (mod 2)."
- I = 21 → 二進位 "10101" → 3 個 1 → 輸出 "The parity of 10101 is 3 (mod 2)."
"""


def calculate_parity(number):
    """
    計算整數的奇偶性（二進位中 1 的個數）。

    參數：
        number: 正整數

    回傳：
        (binary_str, parity_count) 的 tuple
        - binary_str: 二進位表示（不含前導零）
        - parity_count: 二進位中 1 的個數
    """
    # 使用 bin() 將整數轉為二進位字串，然後移除 '0b' 前綴
    binary_str = bin(number)[2:]
    
    # 計算二進位字串中 '1' 的個數
    parity_count = binary_str.count('1')
    
    return binary_str, parity_count


def main():
    """主程式：逐行讀入整數，遇到 0 結束。"""
    while True:
        number_input = input().strip()
        
        # 題目規定輸入 0 表示結束
        if number_input == "0":
            break
        
        number = int(number_input)
        binary_str, parity_count = calculate_parity(number)
        
        # 按照題目要求的格式輸出
        print(f"The parity of {binary_str} is {parity_count} (mod 2).")


if __name__ == "__main__":
    main()
