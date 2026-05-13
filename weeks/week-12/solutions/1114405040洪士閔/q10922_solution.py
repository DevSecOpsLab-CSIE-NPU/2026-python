"""
題目 10922 - 2 the 9s

問題：判斷一個數是否為 9 的倍數，若是則計算 9 的深度

解法：
- 9 的倍數可以用「數字根」判斷
- 9 的深度 = 需要幾次數字和計算才能得到 9
"""


def calculate_digit_sum(num_str):
    """
    計算字符串表示的數字的各位數字之和。
    
    參數：
        num_str (str): 數字的字符串表示
    
    返回：
        int: 各位數字之和
    """
    return sum(int(digit) for digit in num_str)


def calculate_degree(num_str):
    """
    計算數字 9 的深度。
    
    深度定義為：需要進行幾次數字和計算才能得到一位數 9
    
    參數：
        num_str (str): 數字的字符串表示
    
    返回：
        int: 9 的深度
    """
    degree = 0
    
    # 持續計算數字和，直到結果為一位數
    while len(num_str) > 1:
        # 計算所有數字的和
        digit_sum = calculate_digit_sum(num_str)
        # 將和轉換為字符串，便於下一輪計算
        num_str = str(digit_sum)
        # 增加深度計數
        degree += 1
    
    return degree


def main():
    """
    主程式：讀取輸入，判斷 9 的倍數，計算 9 的深度。
    """
    # 讀取輸入，直到遇到 0
    while True:
        # 讀取一個數字（可能很長）
        num_str = input().strip()
        
        # 當輸入為 '0' 時停止
        if num_str == '0':
            break
        
        # 轉換為整數檢查是否為 9 的倍數
        num = int(num_str)
        
        # 判斷是否為 9 的倍數
        if num % 9 != 0:
            # 不是 9 的倍數
            print(f"{num_str} is not a multiple of 9.")
        else:
            # 是 9 的倍數，計算深度
            degree = calculate_degree(num_str)
            print(f"9-degree of {num_str} is {degree}.")


if __name__ == "__main__":
    main()
