"""
UVA 10929 解決方案
判斷超大整數（最多1000位）是否為11的倍數

算法解析：
- 11的倍數特性：奇數位數字之和 - 偶數位數字之和 = 11的倍數
- 位數計算方式：從右到左，第1位是奇數位，第2位是偶數位，以此類推
- 例如：1234
  - 奇數位（第1、3位）：4 + 2 = 6
  - 偶數位（第2、4位）：3 + 1 = 4
  - 差：6 - 4 = 2，不是11的倍數
"""


def is_multiple_of_11(num_str):
    """
    判斷超大數字是否為11的倍數
    
    參數：
        num_str (str): 數字字串
    
    返回：
        str: 判斷結果文字
    """
    # 計算奇數位和偶數位的數字之和
    odd_sum = 0    # 奇數位（第1、3、5...位，從右往左計算）
    even_sum = 0   # 偶數位（第2、4、6...位，從右往左計算）
    
    # 從右到左遍歷數字
    for i, digit in enumerate(reversed(num_str)):
        digit_val = int(digit)
        if i % 2 == 0:  # 奇數位（第1、3、5...位）
            odd_sum += digit_val
        else:  # 偶數位（第2、4、6...位）
            even_sum += digit_val
    
    # 檢查差是否能被11整除
    diff = odd_sum - even_sum
    if diff % 11 == 0:
        return f"{num_str} is a multiple of 11."
    else:
        return f"{num_str} is not a multiple of 11."


def main():
    """主程式：讀取輸入並輸出結果"""
    while True:
        num_str = input().strip()
        if num_str == "0":
            break
        
        print(is_multiple_of_11(num_str))


if __name__ == "__main__":
    main()
