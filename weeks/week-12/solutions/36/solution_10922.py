# UVA 10922 - 2 the 9s
# 解題思路：
# 1. 檢查一個數是否為 9 的倍數：各位數字總和是否為 9 的倍數
# 2. 「9 的深度」是指需要重複計算各位數字總和多少次才能得到 9
# 3. 過程：一直計算數字和，直到得到個位數 9

def calculate_nine_degree(num_str):
    """
    計算數字的「9 的深度」
    返回 (是否為9的倍數, 深度)
    """
    depth = 0
    current = sum(int(d) for d in num_str)
    
    # 一直計算數字和，直到變成個位數
    while current >= 10:
        depth += 1
        current = sum(int(d) for d in str(current))
    
    # 最後檢查是否為 9
    if current == 9:
        return True, depth + 1
    else:
        return False, 0

def solve_two_the_nines():
    """
    求解 2 the 9s 問題
    """
    while True:
        num_str = input().strip()
        
        if num_str == "0":
            break
        
        is_multiple, depth = calculate_nine_degree(num_str)
        
        if is_multiple:
            print(f"9-degree of {num_str} is {depth}.")
        else:
            print(f"{num_str} is not a multiple of 9.")

if __name__ == "__main__":
    solve_two_the_nines()
