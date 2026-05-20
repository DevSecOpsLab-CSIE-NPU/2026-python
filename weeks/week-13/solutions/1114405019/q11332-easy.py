import sys
import math

# 這個程式解決 UVA 11332 (鏡子可見度) 題目
# 核心邏輯：極角掃描 (Polar Sweep)
# 1. 將每個鏡子的兩端點轉為極角 (atan2)
# 2. 收集所有端點的極角，並排序形成多個「角度區間」
# 3. 在每個區間的中間角度發射射線，看哪面鏡子離原點最近
# 4. 最近的那面鏡子在該區間是「可見的」

def get_dist(angle, x1, y1, x2, y2):
    # 計算從原點以角度 angle 發射的射線與線段 (x1,y1)-(x2,y2) 的交點距離
    # 這裡使用射線方程與線段方程求交點
    # 射線: x = r*cos(a), y = r*sin(a)
    # 線段: (y2-y1)x - (x2-x1)y + x2y1 - y2x1 = 0
    # 代入得 r = (y2x1 - x2y1) / ((y2-y1)cos(a) - (x2-x1)sin(a))
    
    sina = math.sin(angle)
    cosa = math.cos(angle)
    
    denom = (y2 - y1) * cosa - (x2 - x1) * sina
    if abs(denom) < 1e-9:
        return float('inf')
    
    r = (y2 * x1 - x2 * y1) / denom
    return r if r > 0 else float('inf')

def solve():
    # 使用 sys.stdin.read().split() 處理大量輸入
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    while idx < len(data):
        try:
            n = int(data[idx])
            idx += 1
        except:
            break
            
        mirrors = []
        angles = []
        for i in range(n):
            x1, y1, x2, y2 = map(float, data[idx:idx+4])
            idx += 4
            
            a1 = math.atan2(y1, x1)
            a2 = math.atan2(y2, x2)
            
            # 確保 a1 < a2，處理跨越 -PI/PI 邊界的情況
            if a1 > a2: a1, a2 = a2, a1
            
            # 如果跨越邊界，將區間拆開處理會比較簡單，
            # 但這裡我們使用一個小技巧：如果差距 > PI，表示是走「外圈」
            if a2 - a1 > math.pi:
                # 拆成 [a2, PI] 和 [-PI, a1]
                mirrors.append((a2, math.pi, x1, y1, x2, y2, i))
                mirrors.append((-math.pi, a1, x1, y1, x2, y2, i))
                angles.extend([a2, math.pi, -math.pi, a1])
            else:
                mirrors.append((a1, a2, x1, y1, x2, y2, i))
                angles.extend([a1, a2])
        
        # 排序所有關鍵角度，並去重
        angles = sorted(list(set(angles)))
        visible = [0] * n
        
        # 檢查每個角度區間
        for i in range(len(angles) - 1):
            mid_angle = (angles[i] + angles[i+1]) / 2
            min_r = float('inf')
            best_id = -1
            
            # 找出在這個角度下最近的鏡子
            for a_start, a_end, x1, y1, x2, y2, m_id in mirrors:
                if a_start <= mid_angle <= a_end:
                    r = get_dist(mid_angle, x1, y1, x2, y2)
                    if r < min_r:
                        min_r = r
                        best_id = m_id
            
            if best_id != -1:
                visible[best_id] = 1
        
        print(" ".join(map(str, visible)))

if __name__ == "__main__":
    solve()
