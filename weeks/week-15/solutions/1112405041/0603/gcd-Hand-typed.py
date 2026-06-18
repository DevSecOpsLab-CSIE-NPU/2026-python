import math

# 手打練習版：確保不依賴 AI 生成，強化記憶
def sum_of_gcd(n):
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total
