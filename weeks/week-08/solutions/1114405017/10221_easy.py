import math, sys

# 地球半徑常數
R = 6440

for line in sys.stdin:
    if not line.strip(): continue
    
    # 讀取輸入並轉換型態
    s_val, a_val, unit = line.split()
    s, a = float(s_val), float(a_val)
    
    # 簡化邏輯：如果是分(min)就除以60，否則保持不變
    deg = a / 60 if unit == 'min' else a
    
    # 處理優化角度（取最短路徑），限制在 180 度內
    deg = min(deg, 360 - deg) if deg > 180 else deg
    
    # 計算半徑與弧度
    r = R + s
    rad = deg * math.pi / 180
    
    # 輸出結果 (使用 f-string 控制精度)
    print(f"{r * rad:.6f} {2 * r * math.sin(rad / 2):.6f}")