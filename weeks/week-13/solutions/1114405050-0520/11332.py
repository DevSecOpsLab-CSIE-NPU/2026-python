import sys
import math

def solve_mirrors(n, mirrors):
    """
    計算每面鏡子是否可見。
    
    參數:
    n (int): 鏡子的數量
    mirrors (list): 包含鏡子座標 (sx, sy, ex, ey) 的列表
    
    回傳:
    list: 每個鏡子是否可見的 0/1 列表
    """
    if n == 0:
        return []
        
    endpoints = []
    # 收集每面鏡子的兩個端點與原點連線的極角 (polar angle)
    for sx, sy, ex, ey in mirrors:
        endpoints.append(math.atan2(sy, sx))
        endpoints.append(math.atan2(ey, ex))
        
    # 將所有端點的極角由小到大排序
    endpoints.sort()
    
    # 建立所有需要測試的射線角度
    # 為了確保不會遺漏任何未被完全遮擋的區域，
    # 必須測試「每個端點的角度」以及「相鄰兩個端點角度之間的中間角度」。
    test_angles = []
    for i in range(len(endpoints)):
        test_angles.append(endpoints[i])
        next_i = (i + 1) % len(endpoints)
        diff = endpoints[next_i] - endpoints[i]
        if diff < 0:
            diff += 2 * math.pi
        test_angles.append(endpoints[i] + diff / 2.0)
        
    visible = [0] * n
    
    # 沿著每個測試角度發射一條射線，找出最先碰觸到的鏡子
    for angle in test_angles:
        dx = math.cos(angle)
        dy = math.sin(angle)
        
        min_dist = float('inf')
        best_i = -1
        
        # 檢查該射線與每一面鏡子的交點
        for i, (sx, sy, ex, ey) in enumerate(mirrors):
            # 使用二維外積來判斷射線與鏡子是否平行
            den = (ex - sx) * dy - (ey - sy) * dx
            if abs(den) < 1e-9:
                continue # 射線與鏡子幾乎平行，無交點
                
            # 計算交點在鏡子線段上的比例 u
            u = -(sx * dy - sy * dx) / den
            
            # 若 u 介於 0 到 1 之間，代表交點確實落在鏡子的實體長度上
            if -1e-7 <= u <= 1 + 1e-7:
                ix = sx + u * (ex - sx)
                iy = sy + u * (ey - sy)
                # 計算交點到原點的距離 (利用內積概念)
                t = ix * dx + iy * dy
                
                # t > 0 代表交點位於射線的正前進方向
                if t > 1e-7:
                    # 更新最靠近原點的那面鏡子
                    if t < min_dist:
                        min_dist = t
                        best_i = i
                        
        # 標記最先碰觸到的鏡子為「可見」 (設為 1)
        if best_i != -1:
            visible[best_i] = 1 
            
    return visible

def main():
    # 讀取所有的標準輸入，並使用空白字元切割，忽略多餘換行
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    tokens = iter(input_data)
    
    while True:
        try:
            n_str = next(tokens)
        except StopIteration:
            break
            
        n = int(n_str)
        mirrors = []
        for _ in range(n):
            sx = int(next(tokens))
            sy = int(next(tokens))
            ex = int(next(tokens))
            ey = int(next(tokens))
            mirrors.append((sx, sy, ex, ey))
            
        # 呼叫判斷函式
        result = solve_mirrors(n, mirrors)
        # 將結果陣列 (0/1) 轉成字串並以空白連接輸出
        print(" ".join(map(str, result)))

if __name__ == '__main__':
    main()