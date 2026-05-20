import sys

# 這個程式用來解決影像顏色轉換問題 (RGB 轉 XYZ)
# 轉換公式：
# X = 0.5149 * R + 0.3244 * G + 0.1607 * B
# Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
# Z = 0.0248 * R + 0.1248 * G + 0.8504 * B

def solve():
    # 讀取所有輸入並過濾掉空白字元，轉換為數字串列
    # 這樣可以處理各種換行或多餘空白的情況
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        idx = 0
        # 第一行是影像大小 n (n * n 像素)
        n = int(input_data[idx])
        idx += 1
        
        total_y = 0.0
        # 總共會有 n * n 個像素，每個像素由 R, G, B 三個整數組成
        for _ in range(n * n):
            r = int(input_data[idx])
            g = int(input_data[idx+1])
            b = int(input_data[idx+2])
            idx += 3
            
            # 根據公式計算 X, Y, Z
            # 這裡使用浮點數計算
            x = 0.5149 * r + 0.3244 * g + 0.1607 * b
            y = 0.2654 * r + 0.6704 * g + 0.0642 * b
            z = 0.0248 * r + 0.1248 * g + 0.8504 * b
            
            # 累加 Y 用於計算平均亮度
            total_y += y
            
            # 輸出每個像素的 XYZ，格式化到小數點後 4 位
            # "{:.4f}".format(v) 會執行四捨五入到第四位
            print(f"{x:.4f} {y:.4f} {z:.4f}")
        
        # 計算平均亮度並輸出
        avg_y = total_y / (n * n)
        print(f"The average of Y is {avg_y:.4f}")
        
    except EOFError:
        pass
    except Exception:
        pass

if __name__ == "__main__":
    solve()
