# AI 教你的簡單版本 - UVA 11332 Mirrors Visibility
# 題目概念：從原點(0,0)檢查是否能看到某條線段（鏡子）

import math

def cross(o, a, b):
    """
    計算叉積：(a-o) × (b-o)
    如果結果 > 0：b 在射線 o->a 的左邊
    如果結果 < 0：b 在射線 o->a 的右邊
    如果結果 = 0：三點共線
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def is_visible(mirror_idx, mirrors):
    """
    檢查指定的鏡子是否從原點可見
    
    思路：對鏡子線段上的多個點進行採樣，
    檢查這些點是否被其他縣段遮擋
    """
    s, e = mirrors[mirror_idx]
    
    # 對線段上的多個點進行採樣
    for t in [0, 0.25, 0.5, 0.75, 1.0]:
        # 計算線段上的採樣點
        px = s[0] + t * (e[0] - s[0])
        py = s[1] + t * (e[1] - s[1])
        p = (px, py)
        
        # 檢查是否被其他線段遮擋
        blocked = False
        
        for j in range(len(mirrors)):
            if i == j:
                continue
            
            s2, e2 = mirrors[j]
            
            # 計算從原點到p的距離平方
            dist_p = px * px + py * py
            
            # 使用叉積檢查線段是否與射線相交
            cross_s2 = cross((0, 0), (px, py), s2)
            cross_e2 = cross((0, 0), (px, py), e2)
            
            # 如果線段的兩個端點在射線的兩側
            if cross_s2 * cross_e2 <= 0 and (cross_s2 != 0 or cross_e2 != 0):
                # 檢查交點是否在p之前
                dist_s2 = s2[0] * s2[0] + s2[1] * s2[1]
                dist_e2 = e2[0] * e2[0] + e2[1] * e2[1]
                
                min_dist = min(dist_s2, dist_e2)
                if min_dist < dist_p:
                    blocked = True
                    break
        
        # 如果有至少一個點沒被遮擋，則鏡子可見
        if not blocked:
            return True
    
    return False


def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        
        mirrors = []
        for _ in range(n):
            sx, sy, ex, ey = map(int, input().split())
            mirrors.append(((sx, sy), (ex, ey)))
        
        # 檢查每個鏡子是否可見
        result = []
        for i in range(n):
            if is_visible(i, mirrors):
                result.append('1')
            else:
                result.append('0')
        
        print(''.join(result))


# 執行
if __name__ == "__main__":
    solve()
