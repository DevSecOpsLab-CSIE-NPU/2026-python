import math

# 手打練習版：手動判斷區間
def count_squares(a, b):
    if a > b:
        raise ValueError("a must be <= b")
    
    count = 0
    i = 1
    while i * i <= b:
        if i * i >= a:
            count += 1
        i += 1
    return count
