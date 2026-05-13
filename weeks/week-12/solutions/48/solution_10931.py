"""
UVA 10931 — Parity 解決方案
計算整數二進位表示中1的個數（奇偶性）

算法解析：
- 奇偶性（Parity）定義為二進位中1的個數
- 二進位轉換：使用 bin(n) 或位運算
- 輸出格式：The parity of {二進位} is {1的個數} (mod 2).
"""


def calculate_parity(num):
    """
    計算整數的奇偶性（二進位中1的個數）
    
    參數：
        num (int): 整數
    
    返回：
        str: 格式化的輸出結果
    """
    # 轉換為二進位字串（去掉 '0b' 前綴）
    binary_str = bin(num)[2:]
    
    # 計算1的個數
    count_ones = binary_str.count('1')
    
    # 格式化輸出
    return f"The parity of {binary_str} is {count_ones} (mod 2)."


def main():
    """主程式：讀取輸入並輸出結果"""
    while True:
        num = int(input().strip())
        if num == 0:
            break
        
        print(calculate_parity(num))


if __name__ == "__main__":
    main()
