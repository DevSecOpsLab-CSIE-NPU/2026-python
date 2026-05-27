"""
題目 11461 - Square Numbers (完全平方數計數) - 手打版本
學生自己手動編寫的解題程式
"""

import math

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    count = int(math.sqrt(b)) - int(math.sqrt(a - 1))
    print(count)
