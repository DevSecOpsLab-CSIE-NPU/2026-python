# AI 教你的簡單版本 - UVA 11063 RGB to XYZ Color Space
# 題目概念：將RGB顏色空間轉換至XYZ顏色空間，計算平均亮度

def rgb_to_xyz(r, g, b):
    """
    將 RGB 顏色轉換為 XYZ 顏色空間
    使用以下轉換公式：
    X = 0.5149 * R + 0.3244 * G + 0.1607 * B
    Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
    Z = 0.0248 * R + 0.1248 * G + 0.8504 * B
    """
    X = 0.5149 * r + 0.3244 * g + 0.1607 * b
    Y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    Z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    
    return X, Y, Z


def solve():
    # 讀取影像大小
    n = int(input())
    
    # 用來存儲所有像素的XYZ值和亮度
    pixels_xyz = []
    total_y = 0  # 累計亮度（Y值）
    
    # 讀取 n*n 個像素
    for i in range(n):
        row = list(map(int, input().split()))
        
        # 每行有 n 個像素，每個像素 3 個值（R, G, B）
        for j in range(n):
            r = row[j * 3]
            g = row[j * 3 + 1]
            b = row[j * 3 + 2]
            
            # 轉換 RGB 到 XYZ
            x, y, z = rgb_to_xyz(r, g, b)
            pixels_xyz.append((x, y, z))
            total_y += y
    
    # 输出每個像素的 XYZ 值
    for x, y, z in pixels_xyz:
        # 四捨五入到小數點後4位
        print(f"{x:.4f} {y:.4f} {z:.4f}")
    
    # 計算平均亮度
    average_y = total_y / (n * n)
    print(f"The average of Y is {average_y:.4f}")


# 執行
if __name__ == "__main__":
    solve()
