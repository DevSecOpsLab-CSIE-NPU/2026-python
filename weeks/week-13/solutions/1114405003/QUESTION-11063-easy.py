# 讀取影像尺寸
n = int(input())
y_values = []

# 逐列讀取並處理每個像素
for row in range(n):
    # 將一行的像素RGB值讀入
    pixels = list(map(int, input().split()))
    
    for col in range(n):
        # 從像素列表中取出第col個像素的RGB三個顏色值
        r = pixels[col * 3]
        g = pixels[col * 3 + 1]
        b = pixels[col * 3 + 2]
        
        # 套用轉換公式，將RGB轉為XYZ
        # 公式中的係數是固定的
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        
        # 保存Y值，用於後面計算平均亮度
        y_values.append(y)
        
        # 輸出轉換後的X, Y, Z值，保留4位小數
        print(f"{x:.4f} {y:.4f} {z:.4f}")

# 計算所有像素Y值的平均，即平均亮度
if y_values:
    average_y = sum(y_values) / len(y_values)
    # 輸出平均亮度，格式: "The average of Y is <值>"
    print(f"The average of Y is {average_y:.4f}")
