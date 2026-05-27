"""
題目 11417 - GCD (最大公因數總和) - 手打版本
學生自己手動編寫的解題程式
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

while True:
    n = int(input())
    if n == 0:
        break
    
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    
    print(total)
