"""UVA 11332 - 簡化版（代表角檢測）

這份程式的核心想法是：
1. 對每一條線段，先找出它兩個端點相對原點的角度
2. 用這兩個角度之間的中間方向，當作這條線段的「代表射線」
3. 沿著這個方向往外看，找哪一條線段最先被射到
4. 如果最先被射到的就是自己，代表它可見

這是一種用幾何近似與排序判斷「可見性」的做法，程式較精簡，適合教學閱讀。
"""

import math
import sys


def intersect_ray_segment(angle, seg):
    # seg = (sx, sy, ex, ey) 表示一條線段的兩個端點。
    sx, sy, ex, ey = seg
    # 線段方向向量。
    dx = ex - sx; dy = ey - sy
    # 代表角對應的單位方向向量。
    cx = math.cos(angle); cy = math.sin(angle)

    # 透過 2D 向量叉積公式，求射線與線段是否相交。
    # denom 太接近 0 表示平行或幾乎平行。
    denom = cx*dy - dx*cy
    if abs(denom) < 1e-12:
        # 平行時改用端點投影的方式做退化情況處理。
        t1 = sx*cx + sy*cy
        t2 = ex*cx + ey*cy
        # 只保留在射線前方（t >= 0）的端點投影距離。
        cand = [t for t in (t1,t2) if t>=0]
        # 若沒有可用候選，代表這條線段在此方向上沒有有效交點。
        return min(cand) if cand else None

    # u 代表交點在「線段」上的比例位置，需介於 0 到 1。
    # t 代表交點在「射線」上的距離，需為非負。
    u = (sx*cy - cx*sy) / denom
    t = (sx*dy - dx*sy) / denom
    if 0<=u<=1 and t>=0:
        return t
    # 若沒有同時落在線段與射線上，則不相交。
    return None


def solve():
    # 題目可能有多組資料，因此先把所有 token 一次讀進來。
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    out_lines = []
    while True:
        try:
            # 每一組資料的開頭是線段數 n。
            n = int(next(it))
        except StopIteration:
            break

        # 讀入 n 條線段，每條線段由四個整數座標組成。
        segs = [tuple(int(next(it)) for _ in range(4)) for _ in range(n)]
        # vis[i] = 1 代表第 i 條線段可見，預設不可見。
        vis = [0]*n

        # 逐一檢查每條線段是否能被「自己的代表方向」最先射到。
        for i,(sx,sy,ex,ey) in enumerate(segs):
            # 端點相對原點的角度。
            a1 = math.atan2(sy, sx); a2 = math.atan2(ey, ex)

            # 兩個角度之差需要調整到 [-pi, pi] 範圍內，避免跨越角度邊界。
            diff = a2 - a1
            if diff <= -math.pi: diff += 2*math.pi
            elif diff > math.pi: diff -= 2*math.pi

            # 代表角：取兩端點角度的中間值。
            mid = a1 + diff/2

            # 再把代表角正規化回 [-pi, pi]，方便後續使用。
            if mid > math.pi: mid -= 2*math.pi
            if mid <= -math.pi: mid += 2*math.pi

            # best_t 紀錄目前為止，沿著 mid 方向看到的最近交點距離。
            # best_idx 紀錄是被哪一條線段擋到。
            best_t = None; best_idx = None
            for j,s2 in enumerate(segs):
                # 計算代表射線與第 j 條線段的交點距離。
                t = intersect_ray_segment(mid, s2)
                if t is not None and (best_t is None or t < best_t):
                    best_t = t; best_idx = j

            # 如果最近的那條線段就是自己，表示它可見。
            if best_idx == i:
                vis[i] = 1

        # 將每組答案合併成 0/1 字串輸出。
        out_lines.append(''.join(map(str,vis)))
    print('\n'.join(out_lines))

if __name__ == '__main__':
    # 直接執行此檔案時，進入解題流程。
    solve()
