import unittest
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
    for sx, sy, ex, ey in mirrors:
        endpoints.append(math.atan2(sy, sx))
        endpoints.append(math.atan2(ey, ex))
        
    # 將所有端點的極角 (角度) 排序
    endpoints.sort()
    
    # 建立所有需要測試的射線角度
    # 為了找出「能見到該鏡子中一小段區域」，我們不僅測試剛好射向端點的射線，
    # 還要測試相鄰兩端點之間的中間角度。這樣可以保證任何未被完全遮擋的區域都會被掃描到。
    test_angles = []
    for i in range(len(endpoints)):
        test_angles.append(endpoints[i])
        next_i = (i + 1) % len(endpoints)
        diff = endpoints[next_i] - endpoints[i]
        if diff < 0:
            diff += 2 * math.pi
        test_angles.append(endpoints[i] + diff / 2.0)
        
    visible = [0] * n
    
    # 朝每個測試角度發射射線，找出最先碰到的鏡子
    for angle in test_angles:
        dx = math.cos(angle)
        dy = math.sin(angle)
        
        min_dist = float('inf')
        best_i = -1
        
        # 檢查該射線與每一面鏡子的交點
        for i, (sx, sy, ex, ey) in enumerate(mirrors):
            den = (ex - sx) * dy - (ey - sy) * dx
            if abs(den) < 1e-9:
                continue # 射線與鏡子幾乎平行，無交點
                
            # 計算交點在鏡子線段上的比例 u
            u = -(sx * dy - sy * dx) / den
            
            # 若 u 介於 0 到 1 之間，代表射線確實打中鏡子實體
            if -1e-7 <= u <= 1 + 1e-7:
                ix = sx + u * (ex - sx)
                iy = sy + u * (ey - sy)
                # 計算交點距離原點的長度 t (內積)
                t = ix * dx + iy * dy
                
                # t > 0 代表交點在射線的正前方
                if t > 1e-7:
                    if t < min_dist:
                        min_dist = t
                        best_i = i
                        
        if best_i != -1:
            visible[best_i] = 1 # 最先碰到的鏡子就是可見的
            
    return visible

class TestUVA11332(unittest.TestCase):
    def test_basic_visibility(self):
        # 測試案例 1：基本的遮擋測試
        # 鏡子 1 在前方
        # 鏡子 2 被鏡子 1 完全遮擋
        # 鏡子 3 在旁邊沒被遮擋
        mirrors = [
            (1, 1, 1, -1),     # 鏡子 1
            (2, 0.5, 2, -0.5), # 鏡子 2 (被遮擋)
            (-1, 1, -1, -1)    # 鏡子 3
        ]
        result = solve_mirrors(3, mirrors)
        self.assertEqual(result, [1, 0, 1], "鏡子 2 應該被完全遮擋，其餘應可見")

    def test_partial_visibility(self):
        # 測試案例 2：部分遮擋測試
        # 鏡子 1 在前方
        # 鏡子 2 比較長，雖然中間被鏡子 1 遮擋，但兩端仍然可見
        mirrors = [
            (1, 1, 1, -1),
            (2, 2, 2, -2)
        ]
        result = solve_mirrors(2, mirrors)
        self.assertEqual(result, [1, 1], "鏡子 2 的兩端較長，應該仍然可見")

if __name__ == '__main__':
    unittest.main()