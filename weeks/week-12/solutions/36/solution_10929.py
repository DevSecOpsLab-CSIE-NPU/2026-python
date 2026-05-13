# UVA 10929 - Multiple of 11
# 解題思路：
# 判斷一個大整數是否為 11 的倍數
# 使用奇偶位差法：
# 設數字從右到左位置為 1, 2, 3, 4, ...
# 奇數位數字之和 - 偶數位數字之和 若為 11 的倍數，原數則為 11 的倍數

def is_multiple_of_11(num_str):
    """
    使用奇偶位差法判斷是否為 11 的倍數
    返回 True 如果是 11 的倍數，否則 False
    """
    total = 0
    
    # 從右到左遍歷，位置從 1 開始計算
    for i, digit in enumerate(reversed(num_str)):
        digit_val = int(digit)
        
        # i=0 對應位置 1（奇數位），加上
        # i=1 對應位置 2（偶數位），減去
        if i % 2 == 0:  # 奇數位（1, 3, 5, ...）
            total += digit_val
        else:  # 偶數位（2, 4, 6, ...）
            total -= digit_val
    
    return total % 11 == 0

def solve_multiple_of_11():
    """
    求解 Multiple of 11 問題
    """
    while True:
        num_str = input().strip()
        
        if num_str == "0":
            break
        
        if is_multiple_of_11(num_str):
            print(f"{num_str} is a multiple of 11.")
        else:
            print(f"{num_str} is not a multiple of 11.")

if __name__ == "__main__":
    solve_multiple_of_11()
