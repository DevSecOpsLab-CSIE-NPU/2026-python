"""
UVA 10929 簡單版本
更簡單易記的寫法

核心思想：
- 從右到左遍歷數字
- 奇數位（第1、3、5位）加起來
- 偶數位（第2、4、6位）加起來
- 計算差是否能被11整除
"""


def multiple_of_11_simple(num_str):
    """
    最簡單的解法
    
    簡化概念：
    - reversed() 反轉字串
    - enumerate() 同時得到索引和值
    - 根據索引判斷奇偶位
    """
    # 計算奇偶位之和
    odd_sum = 0
    even_sum = 0
    
    # 從右往左加
    for i, digit in enumerate(reversed(num_str)):
        if i % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    
    # 檢查差是否能被11整除
    if (odd_sum - even_sum) % 11 == 0:
        return f"{num_str} is a multiple of 11."
    else:
        return f"{num_str} is not a multiple of 11."


# 測試
if __name__ == "__main__":
    print(multiple_of_11_simple("11"))    # is a multiple of 11
    print(multiple_of_11_simple("121"))   # is a multiple of 11
    print(multiple_of_11_simple("123"))   # is not a multiple of 11
