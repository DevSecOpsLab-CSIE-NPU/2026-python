"""
UVA 10922 — 2 the 9s 解決方案
判斷是否為9的倍數，並計算9的深度

算法解析：
- 9的倍數特性：一個數的各位數字之和若能被9整除，則該數也能被9整除
- 9的深度：計算該數需要多少次「各位數字之和」的操作才能得到9
- 流程：
  1. 計算各位數字之和
  2. 如果得到9，深度加1，結束
  3. 如果還是多位數，重複步驟1-2
"""


def calculate_digit_sum(s):
    """計算字串表示數字的各位數字之和"""
    return sum(int(digit) for digit in s)


def calculate_nine_degree(num_str):
    """
    計算9的深度
    
    參數：
        num_str (str): 數字字串
    
    返回：
        tuple: (輸出文字, 深度)，如果不是9的倍數則深度為0
    """
    # 先計算一次各位數字之和
    digit_sum = calculate_digit_sum(num_str)
    
    # 檢查是否能被9整除
    if digit_sum % 9 != 0:
        return (f"{num_str} is not a multiple of 9.", 0)
    
    # 計算9的深度
    depth = 0
    while digit_sum != 9:
        digit_sum = calculate_digit_sum(str(digit_sum))
        depth += 1
    
    depth += 1  # 最後到達9時的深度
    
    return (f"{num_str} is a multiple of 9.", depth)


def main():
    """主程式：讀取輸入並輸出結果"""
    while True:
        num_str = input().strip()
        if num_str == "0":
            break
        
        output, _ = calculate_nine_degree(num_str)
        print(output)


if __name__ == "__main__":
    main()
