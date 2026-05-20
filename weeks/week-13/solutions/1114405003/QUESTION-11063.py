"""
題目：UVA 11063 - RGB轉換到XYZ色彩系統
"""

# 讀取輸入
n = int(input())
y_values = []

for row in range(n):
    pixels = list(map(int, input().split()))
    for col in range(n):
        r, g, b = pixels[col * 3], pixels[col * 3 + 1], pixels[col * 3 + 2]
        
        # 根據公式轉換RGB到XYZ
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        
        # 保存Y值用於計算平均
        y_values.append(y)
        
        # 輸出X, Y, Z（保留4位小數）
        print(f"{x:.4f} {y:.4f} {z:.4f}")

# 計算並輸出平均亮度
if y_values:
    average_y = sum(y_values) / len(y_values)
    print(f"The average of Y is {average_y:.4f}")
