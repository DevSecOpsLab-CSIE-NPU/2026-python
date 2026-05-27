"""
題目 11461 - Square Numbers (完全平方數計數) - 簡易版本
使用更簡潔的寫法，易於在考場快速實現
"""

import math

# 直接輸入/輸出的簡潔寫法
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    # 核心公式：count = floor(√b) - floor(√(a-1))
    count = int(math.sqrt(b)) - int(math.sqrt(a - 1))
    print(count)
