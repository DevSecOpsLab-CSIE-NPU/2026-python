import sys
import math

def main():
    # 讀取全部資料並轉為迭代器 (Iterator)，解 CPE 首選的無腦讀取技巧
    data = iter(sys.stdin.read().split())
    
    for n_str in data:
        n = int(n_str)
        
        mirrors = []
        angles = []
        
        # 讀取所有鏡子座標，並立刻收集端點的「極角 (atan2)」
        for _ in range(n):
            sx, sy, ex, ey = float(next(data)), float(next(data)), float(next(data)), float(next(data))
            mirrors.append((sx, sy, ex, ey))
            angles.extend([math.atan2(sy, sx), math.atan2(ey, ex)])
            
        angles.sort()
        
        # 建立測試射線：發射角度包含「每個端點」與「相鄰端點的夾角中點」
        test_angles = []
        for i in range(len(angles)):
            test_angles.append(angles[i])
            # 利用 % (2*PI) 的特性，完美處理角度跨越 360 度產生負差值的問題
            diff = (angles[(i + 1) % len(angles)] - angles[i]) % (2 * math.pi)
            test_angles.append(angles[i] + diff / 2.0)
            
        ans = [0] * n
        
        # 朝每個測試角度發射一條射線
        for a in test_angles:
            dx, dy = math.cos(a), math.sin(a)
            best_t, best_i = float('inf'), -1
            
            # 檢查該射線會打到哪一面鏡子
            for i, (sx, sy, ex, ey) in enumerate(mirrors):
                # 計算兩線方向向量的外積，若為 0 代表平行、沒有交點
                den = (ex - sx) * dy - (ey - sy) * dx
                if abs(den) < 1e-9: continue
                
                # u 是交點在鏡子線段上的比例 (0 <= u <= 1 代表確實打中鏡子實體)
                u = (sy * dx - sx * dy) / den
                if -1e-7 <= u <= 1 + 1e-7:
                    # t 是交點到原點的距離 (利用內積推導)
                    t = (sx + u * (ex - sx)) * dx + (sy + u * (ey - sy)) * dy
                    
                    # t > 0 代表交點在射線正前方，我們要找距離原點「最近」的那面鏡子
                    if 1e-7 < t < best_t:
                        best_t, best_i = t, i
                        
        # 如果這條射線有打到鏡子，就把「最先打到的那面」標記為可見
        if best_i != -1:
            ans[best_i] = 1
            
        print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()