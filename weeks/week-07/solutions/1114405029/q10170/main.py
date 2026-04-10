import sys
import math

# 進階實作版：使用一元二次方程式公式解
# 核心邏輯：利用數學公式直接求出 X，時間複雜度 O(1)
def solve():
    # 使用 sys.stdin 處理多組測試資料直到 EOF
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        
        s = int(parts[0])
        d = int(parts[1])
        
        # 根據等差級數公式：(S + X) * (X - S + 1) / 2 >= D
        # 展開整理得：X^2 + X - (S^2 - S + 2D) >= 0
        # 利用公式解：x = (-b + sqrt(b^2 - 4ac)) / 2a
        # 其中 a = 1, b = 1, c = -(S^2 - S + 2D)
        
        b = 1
        c = -(s**2 - s + 2 * d)
        
        # 判別式 D = b^2 - 4ac
        discriminant = b**2 - 4 * c
        
        # 計算 X 的最小值（取天花板整數）
        ans = math.ceil((-b + math.sqrt(discriminant)) / 2)
        
        print(ans)

if __name__ == "__main__":
    solve()