import math
import sys

def solve():
    """
    UVA 10221 - Satellites 
    解題核心：單位換算與圓弧幾何公式。
    """
    # 從標準輸入讀取每一行數據
    for line in sys.stdin:
        # 移除行首尾空格，若為空行則跳過
        line = line.strip()
        if not line:
            continue
            
        # 將輸入分割為：高度 s, 角度 a, 單位 unit
        parts = line.split()
        if len(parts) < 3:
            continue
            
        s = float(parts[0])       # 衛星距地表的高度 (km)
        a = float(parts[1])       # 給定的角度值
        unit = parts[2].lower()   # 單位 ('deg' 或 'min')
        
        # 1. 計算衛星軌道的總半徑 (地球半徑 6440 km + 衛星高度 s)
        r = 6440 + s
        
        # 2. 統一將角度轉換為「度 (degree)」
        # 如果單位是 'min' (分)，則需要除以 60 (1度 = 60分)
        if unit == 'min':
            a /= 60.0
            
        # 3. 處理角度大於 180 度的情況
        # 根據圓的特性，兩點之間的夾角若超過 180 度，
        # 計算弧長與弦長時應取另一側較小的夾角 (360 - a)
        if a > 180:
            a = 360 - a
            
        # 4. 將「度」轉換為「弧度 (radian)」
        # 公式：弧度 = 角度 * (π / 180)
        # 使用 math.pi 以確保最高精度
        rad = a * math.pi / 180.0
        
        # 5. 計算弧長 (Arc Length)
        # 公式：L = r * θ (θ 為弧度)
        arc_length = r * rad
        
        # 6. 計算弦長 (Chord Distance)
        # 公式：d = 2 * r * sin(θ / 2)
        chord_distance = 2 * r * math.sin(rad / 2.0)
        
        # 7. 格式化輸出
        # :.6f 代表輸出浮點數並保留小數點後六位
        print(f"{arc_length:.6f} {chord_distance:.6f}")

if __name__ == "__main__":
    solve()