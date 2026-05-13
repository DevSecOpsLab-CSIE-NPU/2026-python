"""
UVA 10931 — Parity (Easy Version)

========== 題目說明 ==========
整數的「奇偶性（Parity）」定義為其二進位表示中 1 的個數。

給定整數 I（1 ≤ I ≤ 2,147,483,647），需要：
1. 轉換為二進位字串（不含前導零）
2. 計算二進位中 1 的個數
3. 按指定格式輸出結果

========== 核心演算法 ==========
直接使用 Python 內建函式：
- bin(number)：將整數轉為二進位字串（含 '0b' 前綴）
- [2:]：移除 '0b' 前綴，得到純二進位字串
- count('1')：計算字串中 '1' 的個數（即 parity）

========== 例子 ==========
I = 1    → 二進位 "1"        → 1 個 1 → 輸出 "The parity of 1 is 1 (mod 2)."
I = 2    → 二進位 "10"       → 1 個 1 → 輸出 "The parity of 10 is 1 (mod 2)."
I = 10   → 二進位 "1010"     → 2 個 1 → 輸出 "The parity of 1010 is 2 (mod 2)."
I = 21   → 二進位 "10101"    → 3 個 1 → 輸出 "The parity of 10101 is 3 (mod 2)."
"""


def get_parity_output(number):
    """
    計算並返回格式化的 parity 結果。
    
    參數：
        number: 正整數（1 ≤ number ≤ 2,147,483,647）
    
    回傳值：
        格式化後的字串，包含二進位表示、1 的個數，以及最後的 (mod 2)
        格式：「The parity of {二進位} is {個數} (mod 2).」
    
    演算法步驟：
    1. 使用 bin() 將整數轉為二進位字串（會包含 '0b' 前綴）
    2. 用 [2:] 切片移除 '0b'，得到純二進位字串
    3. 使用 count('1') 計算字串中 '1' 的個數
    4. 用 f-string 格式化輸出
    """
    # 步驟 1-2：轉換為二進位並移除 '0b' 前綴
    # bin(5) 會返回 '0b101'，[2:] 後得到 '101'
    binary = bin(number)[2:]
    
    # 步驟 3：計算二進位字串中 '1' 的個數
    # '101'.count('1') 返回 2
    ones = binary.count('1')
    
    # 步驟 4：按題目要求的格式返回結果字串
    # f-string 會替換 {binary} 和 {ones} 為實際值
    return f"The parity of {binary} is {ones} (mod 2)."


def main():
    """
    主程式：讀取整數、計算 parity、輸出結果。
    
    流程：
    1. 無限迴圈讀取使用者輸入
    2. 若輸入為 "0"，則結束程式
    3. 否則轉為整數，計算 parity 並輸出
    """
    while True:
        # 讀入一行輸入，並移除前後的空白字元
        n = input().strip()
        
        # 題目規定輸入 0 表示結束程式
        if n == "0":
            break
        
        # 將字串轉為整數，呼叫 get_parity_output() 計算結果，並直接輸出
        print(get_parity_output(int(n)))


if __name__ == "__main__":
    # 程式進入點
    # 當此檔案被直接執行時（而不是被 import），執行 main() 函式
    main()
