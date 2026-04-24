import sys

def solve_password(numbers):
    """
    計算 UVA 10057 規定的三個輸出值：
    1. 能得到距離總和最小值的最小整數 A。
    2. 輸入陣列中，有多少個元素落在「能給出最小值 A」的範圍內。
    3. 總共有幾種可能的整數 A 能給出最小值。
    """
    n = len(numbers)
    # 找中位數前務必先排序
    numbers.sort()
    
    if n % 2 == 1:
        # 奇數個數字：最佳 A 只有一個，就是最中間的那個數字
        median = numbers[n // 2]
        min_a = median
        count_in_input = numbers.count(median)
        possible_a_count = 1
    else:
        # 偶數個數字：最佳 A 是一個連續區間 [左中位數, 右中位數]
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        min_a = mid1
        # 計算原始輸入中有多少個數字落在這個最佳解的區間內
        count_in_input = sum(1 for x in numbers if mid1 <= x <= mid2)
        # 這個區間內包含了多少個整數，就是可能值的總數
        possible_a_count = mid2 - mid1 + 1
        
    return (min_a, count_in_input, possible_a_count)

if __name__ == '__main__':
    # 讀取標準輸入，將所有輸入用空白/換行切分成一個一維陣列
    input_data = sys.stdin.read().split()
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        numbers = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        
        ans = solve_password(numbers)
        print(f"{ans[0]} {ans[1]} {ans[2]}")