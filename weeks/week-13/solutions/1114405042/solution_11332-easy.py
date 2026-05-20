# 題目 11332: 鏡子可見度 (簡易版 - 發射射線法)
# 這是一個最直覺的解法：從原點往四面八方發射射線，看射線先打到哪一面鏡子。
# 為了確保不錯過任何交界點，我們朝著「所有鏡子的端點」以及「端點的左右微小偏移」發射射線。

def solve():
    import sys
    import math
    
    data = sys.stdin.read().split()
    if not data: return
    
    idx = 0
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        
        segments = []
        rays = [] # 儲存要發射的射線角度
        
        for _ in range(n):
            sx, sy, ex, ey = map(float, data[idx:idx+4])
            idx += 4
            segments.append((sx, sy, ex, ey))
            
            # 計算端點與原點的連線角度
            ang1 = math.atan2(sy, sx)
            ang2 = math.atan2(ey, ex)
            
            # 為了避免邊界問題，我們對每個端點的角度，往左和往右稍微偏移一點點 (1e-9)
            # 這樣發射的射線就一定能穿過鏡子的中間或邊緣
            eps = 1e-9
            rays.extend([ang1, ang1 + eps, ang1 - eps])
            rays.extend([ang2, ang2 + eps, ang2 - eps])
            
        # 紀錄每面鏡子是否可見 (0不可見, 1可見)
        visible = [0] * n
        
        # 對每一條射線進行檢查
        for angle in rays:
            dx = math.cos(angle)
            dy = math.sin(angle)
            
            min_t = float('inf')
            closest_idx = -1
            
            # 檢查這條射線會打到哪些鏡子
            for i in range(n):
                sx, sy, ex, ey = segments[i]
                
                # 利用克拉瑪公式求射線與線段的交點
                # 射線參數式: x = t*dx, y = t*dy  (t > 0)
                # 線段參數式: x = sx + u*(ex-sx), y = sy + u*(ey-sy) (0 <= u <= 1)
                
                A = dx
                B = -(ex - sx)
                C = dy
                D = -(ey - sy)
                
                det = A * D - B * C
                if abs(det) < 1e-9: 
                    continue # 射線與線段平行
                    
                t = (sx * D - sy * B) / det
                u = (A * sy - C * sx) / det
                
                # 如果交點在射線正向 (t>0) 且落在線段上 (0<=u<=1)
                if t > 1e-9 and -1e-9 <= u <= 1 + 1e-9:
                    if t < min_t: # 找出最近的交點
                        min_t = t
                        closest_idx = i
                        
            # 如果射線有打到鏡子，把最近的鏡子標記為可見
            if closest_idx != -1:
                visible[closest_idx] = 1
                
        # 印出結果
        print(*(visible))

if __name__ == '__main__':
    solve()
