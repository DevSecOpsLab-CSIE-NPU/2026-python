import sys
import math

# 避免遞迴限制或浮點數誤差問題
eps = 1e-9

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        segments = []
        angles = []
        
        for i in range(n):
            sx = float(input_data[idx])
            sy = float(input_data[idx+1])
            ex = float(input_data[idx+2])
            ey = float(input_data[idx+3])
            idx += 4
            segments.append((sx, sy, ex, ey))
            
            # 收集所有端點的角度
            ang1 = math.atan2(sy, sx)
            ang2 = math.atan2(ey, ex)
            
            angles.append(ang1)
            angles.append(ang2)
            # 在端點的微小偏移處也發射射線，以確保能檢查到所有可見區段
            angles.append(ang1 - eps)
            angles.append(ang1 + eps)
            angles.append(ang2 - eps)
            angles.append(ang2 + eps)
            
        visible = [0] * n
        
        # O(N^2) 射線檢測，對每一條射線找出最近的交點
        for angle in angles:
            # 將角度轉回方向向量
            dx = math.cos(angle)
            dy = math.sin(angle)
            
            min_dist = float('inf')
            closest_segment = -1
            
            for i, (sx, sy, ex, ey) in enumerate(segments):
                # 射線與線段求交點
                # 射線： P = (0,0) + t * (dx, dy), t >= 0
                # 線段： P = (sx, sy) + u * (ex - sx, ey - sy), 0 <= u <= 1
                
                # 解聯立方程式 (Cramer's rule)
                # t * dx - u * (ex - sx) = sx
                # t * dy - u * (ey - sy) = sy
                
                A = dx
                B = -(ex - sx)
                C = dy
                D = -(ey - sy)
                
                det = A * D - B * C
                if abs(det) < eps:
                    continue  # 平行或共線
                    
                t = (sx * D - sy * B) / det
                u = (A * sy - C * sx) / det
                
                # 檢查交點是否在射線正方向且在線段內
                if t > eps and -eps <= u <= 1 + eps:
                    if t < min_dist:
                        min_dist = t
                        closest_segment = i
                        
            if closest_segment != -1:
                visible[closest_segment] = 1
                
        # 輸出結果，以空格分隔
        print(*(visible))

if __name__ == '__main__':
    solve()
