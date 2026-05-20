import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    while True:
        try:
            n = int(next(iterator))
        except StopIteration:
            break
        
        segments = []
        angles = set() # 用 set 收集所有出現過的角度，重複的會自動過濾
        
        for i in range(n):
            sx, sy, ex, ey = [int(next(iterator)) for _ in range(4)]
            segments.append((sx, sy, ex, ey, i))
            
            # 記錄兩個端點的角度
            angles.add(math.atan2(sy, sx))
            angles.add(math.atan2(ey, ex))
        
        # 排序所有角度
        sorted_angles = sorted(list(angles))
        
        # 創造「微元窗口」：包含相鄰角度的中點，以及跨越 -pi 和 pi 的外圈中點
        mid_angles = []
        for i in range(len(sorted_angles) - 1):
            mid_angles.append((sorted_angles[i] + sorted_angles[i+1]) / 2)
        # 補上跨越 -pi 到 pi 的最後一個窗口中點
        mid_angles.append((sorted_angles[-1] + sorted_angles[0] + 2 * math.pi) / 2)
        
        visible = [0] * n
        
        # 國中數學：求 (0,0) 到 (cos_a, sin_a) 的射線，與線段 (x1,y1)-(x2,y2) 的交點距離
        # 記憶法：利用克拉瑪公式（外積/交叉相乘）求聯立方程組的解
        def get_distance(ang, x1, y1, x2, y2):
            rx, ry = math.cos(ang), math.sin(ang) # 射線方向向量
            
            # 線段向量
            dx, dy = x2 - x1, y2 - y1
            
            # 分母 (判別式)
            denom = rx * dy - ry * dx
            if abs(denom) < 1e-9: 
                return float('inf') # 平行，碰不到
            
            # 分子：求射線上的比例 t 和線段上的比例 u
            # 原點出發的射線公式：t * rx = x1 + u * dx
            t = (x1 * dy - y1 * dx) / denom
            u = (x1 * ry - y1 * rx) / denom
            
            # t > 0 代表在射線正方向， 0 <= u <= 1 代表交點確實落在鏡子線段上
            if t > 0 and 0 <= u <= 1:
                return t
            return float('inf')

        # 針對每一個視線窗口的中間角度，朝外看一眼
        for ang in mid_angles:
            min_dist = float('inf')
            closest_idx = -1
            
            for sx, sy, ex, ey, idx in segments:
                dist = get_distance(ang, sx, sy, ex, ey)
                if dist < min_dist:
                    min_dist = dist
                    closest_idx = idx
            
            # 誰離原點最近，誰就可見
            if closest_idx != -1:
                visible[closest_idx] = 1
                
        print(" ".join(map(str, visible)))

if __name__ == '__main__':
    solve()