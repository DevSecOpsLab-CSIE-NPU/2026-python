import math

# CPE 易記版：使用數學公式 O(1) 達成
def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")
    
    # 邏輯：floor(sqrt(b)) - ceil(sqrt(a)) + 1
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    
    if start > end:
        return 0
    return end - start + 1
