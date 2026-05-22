"""
UVA 11332 解題模組（教學版）

問題重述（簡短）：給定多個線段（鏡子），判斷從原點出發的視線能否看到每一個鏡子（若能看到鏡子上任一小段即視為可見）。

解法概要（教學版）：
- 對每個線段計算其兩端相對於原點的角度（使用 atan2），線段在角度空間會對應一個角度區間。
- 所有端點角度把集合排序；任意兩相鄰角度所對應的角度區間內，射線與線段的交序關係不會改變，
  因此可取每個區間中一個代表角度（中點）並沿該方向求與每個線段的交點距離 t，找到最小 t 的線段即為該方向可見。
- 若某線段在任一代表方向上為最接近的交點，則該線段可見。

此版本為教學/正確性驗證用，對大量線段 (n ~ 3e4) 的效能可能不足（O(n^2) 邏輯），但適合單元測試與示範。
"""

from typing import List, Tuple
import math


def cross(ax: float, ay: float, bx: float, by: float) -> float:
    return ax * by - ay * bx


# 註：向量外積（2D cross）可用於判斷兩向量的相對方向與面積關係。
# cross(a,b) 的符號代表 a 相對於 b 的旋轉方向（順/逆時針），數值大小與夾角與長度相關。


def angle_of(x: float, y: float) -> float:
    # normalize to [0, 2*pi)
    a = math.atan2(y, x)
    if a < 0:
        a += 2 * math.pi
    return a


# 註：angle_of 回傳從 x 軸正方向逆時針到向量 (x,y) 的角度，範圍在 [0,2π)。
# 這裡將角度標準化為非負以便後續在環狀角度空間作排序與中點計算。


def visible_segments(segments: List[Tuple[int, int, int, int]]) -> List[int]:
    """
    給定 segments 為 [(sx, sy, ex, ey), ...]，回傳長度為 n 的 0/1 列表，表示每個線段是否可見。
    """
    n = len(segments)
    # 計算每個端點角度
    endpoints = []  # list of angles
    seg_angles = []  # list of (a1,a2) per segment
    for (sx, sy, ex, ey) in segments:
        a1 = angle_of(sx, sy)
        a2 = angle_of(ex, ey)
        seg_angles.append((a1, a2))
        endpoints.append(a1)
        endpoints.append(a2)

    # 去重並排序
    unique_angles = sorted(set(endpoints))
    # 若所有端點角度相同，仍需檢查該射線方向
    if not unique_angles:
        return [0] * n

    # 為處理跨 2pi 邊界的區間，將每一段角度區間視為有可能跨越 0
    # 建立代表角度：在每對相鄰角度中取中點（考慮環狀）
    reps = []
    m = len(unique_angles)
    for i in range(m):
        a = unique_angles[i]
        b = unique_angles[(i + 1) % m]
        # 計算中點沿最短環向量
        diff = b - a
        if i == m - 1:
            # 最後一段，穿過 2pi
            diff = (b + 2 * math.pi) - a
        if diff <= 0:
            continue
        mid = a + diff / 2.0
        mid = mid % (2 * math.pi)
        reps.append(mid)

    visible = [0] * n

    # 對每個代表方向, 計算哪個線段的交點 t 最近
    # 我們也需要處理 "共線" 的情形：當射線方向與線段共線時，denom 會接近 0，
    # 此時應檢查該線段在此方向上是否落在正向射線上，並找出最小的正向投影距離。
    # 為此，我們會同時檢查 reps（區間代表角度）與 unique_angles（精確端點角度）。
    angles_to_check = reps + unique_angles
    for theta in angles_to_check:
        dx = math.cos(theta)
        dy = math.sin(theta)
        best_t = float('inf')
        best_idx = -1
        for idx, (sx, sy, ex, ey) in enumerate(segments):
            # segment vector
            vx = ex - sx
            vy = ey - sy
            denom = cross(dx, dy, vx, vy)
            if abs(denom) < 1e-12:
                # 平行或共線情形：denom 約為 0 表示方向向量 d 與線段向量 v 共線或平行。
                # 我們需要分辨平行但不在同一直線（此時無交點）與真正共線（射線與線段在同一直線上）。
                # 若共線，cross(s, d) 亦會接近 0，此時以端點在 d 方向的內積（投影）判斷是否在正向射線上。
                # 以下透過檢查端點投影值 ts, te 來決定是否存在正向的交點。
                # cross(s, d) 接近 0 表示共線
                if abs(cross(sx, sy, dx, dy)) < 1e-9:
                    # 計算端點在 d 方向上的投影距離
                    ts = sx * dx + sy * dy
                    te = ex * dx + ey * dy
                    cand = None
                    if ts > 0 and te > 0:
                        # 兩端點投影皆在正向，取較小者
                        cand = min(ts, te)
                    elif ts > 0:
                        cand = ts
                    elif te > 0:
                        cand = te
                    # 若有正向交點且比目前 best_t 小，更新
                    if cand is not None and cand < best_t:
                        best_t = cand
                        best_idx = idx
                continue
            t = cross(sx, sy, vx, vy) / denom
            # u = cross(sx, sy, dx, dy) / denom  # optional
            u = cross(sx, sy, dx, dy) / denom
            # 交點存在於 ray (t>0) 且於 segment 0<=u<=1
            if t > 0 and 0.0 <= u <= 1.0:
                if t < best_t:
                    best_t = t
                    best_idx = idx
        if best_idx != -1:
            visible[best_idx] = 1

    return visible


def parse_and_run_stdin() -> None:
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    out_lines = []
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        segs = []
        for _ in range(n):
            sx = int(next(it)); sy = int(next(it)); ex = int(next(it)); ey = int(next(it))
            segs.append((sx, sy, ex, ey))
        vis = visible_segments(segs)
        out_lines.append(' '.join(str(x) for x in vis))
    sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
    parse_and_run_stdin()
