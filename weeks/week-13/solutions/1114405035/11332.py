# -*- coding: utf-8 -*-
import sys
import math

def solve():
    """
    UVA 11332 (ZJ b325) 平面鏡子可見性解題主程式
    """
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
            
            # 儲存鏡子線段與對應的端點極角
            theta_s = math.atan2(sy, sx)
            theta_e = math.atan2(ey, ex)
            
            # 確保 theta_s <= theta_e
            if theta_s > theta_e:
                theta_s, theta_e = theta_e, theta_s
                sx, sy, ex, ey = ex, ey, sx, sy
                
            segments.append(((sx, sy), (ex, ey), theta_s, theta_e, i))
            angles.append(theta_s)
            angles.append(theta_e)
            
        # 取得所有端點的唯一極角並排序
        angles = sorted(list(set(angles)))
        
        # 用來記錄哪些鏡子是可見的
        visible = [0] * n
        
        # 如果只有 1 個鏡子，它一定是可見的
        if n == 1:
            print("1")
            continue
            
        # 建立極角區間並在每個區間的中點投射射線
        midpoints = []
        for i in range(len(angles) - 1):
            midpoints.append((angles[i] + angles[i+1]) / 2.0)
        # 跨越 -pi/pi 邊界的最後一個區間
        midpoints.append((angles[-1] + angles[0] + 2 * math.pi) / 2.0)
        
        for alpha in midpoints:
            cos_a = math.cos(alpha)
            sin_a = math.sin(alpha)
            
            # 標準化 alpha 到 [-pi, pi] 範圍以進行跨邊界判定
            norm_alpha = alpha
            while norm_alpha > math.pi:
                norm_alpha -= 2 * math.pi
            while norm_alpha < -math.pi:
                norm_alpha += 2 * math.pi
                
            min_dist_sq = float('inf')
            best_seg_idx = -1
            
            for (A, B, theta_s, theta_e, seg_id) in segments:
                # 檢查 norm_alpha 是否在該線段的角度跨度內
                in_span = False
                if theta_e - theta_s <= math.pi:
                    if theta_s <= norm_alpha <= theta_e:
                        in_span = True
                else:
                    if norm_alpha >= theta_e or norm_alpha <= theta_s:
                        in_span = True
                        
                if in_span:
                    # 計算射線與線段的交點
                    # 射線方向為 V = (cos_a, sin_a)
                    # A = (ax, ay), B = (bx, by)
                    ax, ay = A
                    bx, by = B
                    
                    # 叉積計算
                    cr_A = cos_a * ay - sin_a * ax
                    cr_B = cos_a * by - sin_a * bx
                    
                    denom = cr_A - cr_B
                    if abs(denom) > 1e-11:
                        u = cr_A / denom
                        ix = ax + u * (bx - ax)
                        iy = ay + u * (by - ay)
                        
                        dist_sq = ix * ix + iy * iy
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            best_seg_idx = seg_id
                            
            if best_seg_idx != -1:
                visible[best_seg_idx] = 1
                
        # 輸出結果
        print(" ".join(map(str, visible)))

if __name__ == "__main__":
    solve()
