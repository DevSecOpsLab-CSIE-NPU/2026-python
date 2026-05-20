import sys

def solve():
    # 讀取標準輸入中的所有資料，並自動忽略多餘的空白與換行
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # 第一個數字為 n
    n = int(input_data[0])
    total_pixels = n * n
    
    # 用來記錄所有像素 Y 值的總和，以便後續計算平均亮度
    sum_y = 0.0
    
    # 像素資料從索引 1 開始
    idx = 1
    
    # 依序處理 n*n 個像素
    for _ in range(total_pixels):
        # 讀取當前像素的 R, G, B 值
        r = float(input_data[idx])
        g = float(input_data[idx+1])
        b = float(input_data[idx+2])
        idx += 3
        
        # 根據題目公式計算 X, Y, Z
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        
        # 累加 Y 值
        sum_y += y
        
        # 輸出當前像素轉換後的 XYZ 值，格式化至小數點後第 4 位
        print(f"{x:.4f} {y:.4f} {z:.4f}")
        
    # 計算平均 Y 值
    avg_y = sum_y / total_pixels
    
    # 輸出最終的平均亮度
    print(f"The average of Y is {avg_y:.4f}")

if __name__ == "__main__":
    solve()