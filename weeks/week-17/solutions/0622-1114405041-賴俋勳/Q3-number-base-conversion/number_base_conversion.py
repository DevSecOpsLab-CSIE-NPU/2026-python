"""
題目：任意進位的數字轉換 - 30分

問題描述：
根據 base 位數進行數字轉換

輸入說明：
- 每行輸入一個十進位數字 n (0 ≤ n ≤ 10^9)
- 是 EOF 表示結束

輸出說明：
- 對於每個十進位數字，輸出其進位轉換結果
- base ∈ {2,3,5,6,7,8,9,11,13,16} (依據題目)

範例 (base = 8)：
Sample Input:
0
8
63

Sample Output:
0
10
77

說明：
- 8 在八進位 (base 8) 的位置是 10
- 63 在八進位的位置是 77 (63 = 7*8 + 7)
"""


def convert_to_base(number, base=8):
    """
    將十進位數字轉換為指定進位
    
    Args:
        number: 十進位數字 (0 ≤ n ≤ 10^9)
        base: 目標進位 (2-36)
    
    Returns:
        str: 轉換後的字符串
    """
    if number == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    while number > 0:
        remainder = number % base
        result.append(digits[remainder])
        number //= base
    
    return ''.join(reversed(result))


def main():
    """
    任意進位轉換主程式
    
    讀取十進位數字，轉換為指定進位並輸出
    """
    base = 8  # 預設 base = 8，可以根據題目要求改變
    
    try:
        while True:
            line = input().strip()
            if line:
                n = int(line)
                result = convert_to_base(n, base)
                print(result)
    except EOFError:
        pass


if __name__ == '__main__':
    main()
