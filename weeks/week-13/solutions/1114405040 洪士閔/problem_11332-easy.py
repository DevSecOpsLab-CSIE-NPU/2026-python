"""
簡易版 Problem 11332（鏡子可見性）— 詳細註解版

問題快速回顧：給定若干線段（鏡子），從原點出發的視線在不同方向會看到最近的那一段，判定每段是否有任一方向可被看到。

核心想法：可見性的變化僅發生在經過端點的方向，因此只需在端點夾角的中間採樣方向（以及端點附近的微小偏移）即可覆蓋所有不同可見性狀態。

流程要點：
- 取得所有端點角度，排序並產生待測方向（相鄰角度中點以及端點小偏移）。
- 對每個方向發射射線（原點 + t*(dx,dy)），計算與每個線段的交點參數 t、u，選最小正 t 的線段視為可見。
- 特別情況：射線與線段平行或共線需額外處理，本簡化版對共線使用保守略過策略以簡化實作（在教學/測資下通常可接受）。

本檔以直觀數學式與註解呈現，有助理解交點計算與參數意義（t 為射線參數、u 為線段參數）。
"""

import math
from typing import List, Tuple


def cross(ax, ay, bx, by):
    return ax*by - ay*bx


def segment_angles(seg: Tuple[int,int,int,int]) -> Tuple[float,float]:
    x1,y1,x2,y2 = seg
    a1 = math.atan2(y1, x1) % (2*math.pi)
    a2 = math.atan2(y2, x2) % (2*math.pi)
    return a1, a2


def visible_segments(segments: List[Tuple[int,int,int,int]]) -> List[int]:
    n = len(segments)
    if n == 0:
        return []
    angles = []
    for seg in segments:
        a1,a2 = segment_angles(seg)
        angles.append(a1); angles.append(a2)
    angles = sorted(set(angles))
    # 建立待測角度集合：相鄰端點角度的中點 + 端點附近的微小偏移
    test_angles = []
    eps = 1e-7
    if len(angles) == 1:
        a = angles[0]
        # 單一角度時，我們加上微幅偏移以避免剛好穿過端點導致數值不穩定
        test_angles = [a-eps, a, a+eps]
    else:
        # 相鄰角度中點代表該區間內視線狀態不會改變
        for i in range(len(angles)):
            a = angles[i]
            b = angles[(i+1)%len(angles)]
            if b <= a:
                b += 2*math.pi
            test_angles.append((a+b)/2)
        # 另外在每個端點周圍加入微小偏移，能處理近乎共線的邊界情況
        for a in angles:
            test_angles.extend([a-eps, a+eps])
    # 正規化到 [0,2pi) 並去重（四捨五入以避免浮點微小差異）
    test_angles = sorted(set([round(x%(2*math.pi),12) for x in test_angles]))

    visible = [0]*n
    for ang in test_angles:
        dx = math.cos(ang); dy = math.sin(ang)
        best_t = float('inf'); best_idx = -1
        for idx, seg in enumerate(segments):
            x1,y1,x2,y2 = seg
            sx = x2 - x1; sy = y2 - y1
            # 求解線性方程式得 t, u：
            # origin + t*(dx,dy) = (x1,y1) + u*(sx,sy)
            # denom = cross(D, S)
            denom = cross(dx,dy, sx,sy)
            if abs(denom) < 1e-12:
                # 當 denom 接近 0 時，射線與線段平行或共線。
                # 完整處理會需要判斷端點是否位於射線上，本簡化版為教學目的，先略過平行情況的細緻處理。
                continue
            # t 為射線上的參數（>0 表示在射線前方），u 為線段參數（0..1 表示在線段上）
            t = cross(x1,y1, sx,sy) / denom
            u = cross(x1,y1, dx,dy) / denom
            if t > 1e-12 and -1e-12 <= u <= 1+1e-12:
                if t < best_t:
                    best_t = t; best_idx = idx
        if best_idx != -1:
            visible[best_idx] = 1
    return visible


def process(input_str: str) -> str:
    tokens = input_str.strip().split()
    if not tokens:
        return ""
    p = 0
    out_lines = []
    while p < len(tokens):
        n = int(tokens[p]); p += 1
        segs = []
        for _ in range(n):
            sx = int(tokens[p]); sy = int(tokens[p+1]); ex = int(tokens[p+2]); ey = int(tokens[p+3]); p += 4
            segs.append((sx,sy,ex,ey))
        vis = visible_segments(segs)
        out_lines.append(' '.join(str(v) for v in vis))
    return '\n'.join(out_lines)


if __name__ == '__main__':
    import sys
    print(process(sys.stdin.read()))
