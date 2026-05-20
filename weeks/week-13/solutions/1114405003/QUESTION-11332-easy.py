"""
題目：UVA 11332 - 鏡子可見性判定 (簡化版)
判斷從原點(0,0)是否能看到各個鏡子(線段)

核心邏輯:
1. 觀察者在原點 (0, 0)
2. 鏡子是一些線段
3. 判斷鏡子是否被其他鏡子遮擋
4. 對每個鏡子輸出 1(可見) 或 0(被遮擋)

演算法:
- 對每個鏡子:
  - 計算從原點到鏡子的射線方向
  - 檢查其他鏡子是否與此射線相交
  - 如果相交,比較距離
  - 如果其他鏡子更近,則本鏡子被遮擋
"""

import math

def ray_segment_intersection(ray_start, ray_dir, seg_start, seg_end):
    """
    計算射線與線段的相交距離
    
    參數:
    - ray_start: 射線起點
    - ray_dir: 射線方向向量
    - seg_start: 線段起點
    - seg_end: 線段終點
    
    返回: 相交距離 (無相交時返回無限大)
    """
    eps = 1e-9
    
    # 線段的方向向量
    dx = seg_end[0] - seg_start[0]
    dy = seg_end[1] - seg_start[1]
    
    # 分母 = 射線方向 × 線段方向
    denom = ray_dir[0] * dy - ray_dir[1] * dx
    
    # 平行情況
    if abs(denom) < eps:
        return float('inf')
    
    # 參數 t 表示沿射線方向的距離
    px = seg_start[0] - ray_start[0]
    py = seg_start[1] - ray_start[1]
    
    t = (px * dy - py * dx) / denom
    # 參數 s 表示在線段上的位置 (0-1為線段內)
    s = (px * ray_dir[1] - py * ray_dir[0]) / denom
    
    # 相交條件: t > 0 (射線正向) 且 0 <= s <= 1 (在線段上)
    if t > eps and -eps <= s <= 1 + eps:
        # 計算實際距離
        distance = math.sqrt(t * t * (ray_dir[0]**2 + ray_dir[1]**2))
        return distance
    
    return float('inf')

# 主程式
while True:
    line = input().strip()
    if not line or line == '0':
        break
    
    n = int(line)
    mirrors = []
    
    # 讀入 n 個鏡子
    for _ in range(n):
        sx, sy, ex, ey = map(int, input().split())
        mirrors.append(((sx, sy), (ex, ey)))
    
    result = []
    
    # 檢查每個鏡子的可見性
    for mirror_idx in range(n):
        mirror_start, mirror_end = mirrors[mirror_idx]
        
        visible = False
        
        # 檢查鏡子的兩個端點
        for target_point in [mirror_start, mirror_end]:
            # 跳過原點
            if abs(target_point[0]) < 1e-9 and abs(target_point[1]) < 1e-9:
                continue
            
            # 射線方向: 從原點指向目標點
            ray_dir = (target_point[0], target_point[1])
            
            # 計算目標點的距離
            target_dist = math.sqrt(ray_dir[0]**2 + ray_dir[1]**2)
            
            blocked = False
            
            # 檢查其他鏡子是否遮擋
            for other_idx in range(n):
                if other_idx == mirror_idx:
                    continue
                
                other_start, other_end = mirrors[other_idx]
                
                # 計算此射線與其他鏡子的相交距離
                intersect_dist = ray_segment_intersection(
                    (0, 0), ray_dir,
                    other_start, other_end
                )
                
                # 如果其他鏡子更近,則本鏡子被遮擋
                if intersect_dist < target_dist - 1e-9:
                    blocked = True
                    break
            
            # 如果此端點未被遮擋,則鏡子可見
            if not blocked:
                visible = True
                break
        
        # 輸出結果: 1 或 0
        result.append('1' if visible else '0')
    
    # 輸出一行 (無分隔符)
    print(''.join(result))
