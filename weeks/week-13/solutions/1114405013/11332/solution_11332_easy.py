import math
import sys


PI2 = 2.0 * math.pi
EPS = 1e-10


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def dot(ax, ay, bx, by):
    return ax * bx + ay * by


def norm_angle(a):
    # 把角度統一到 [0, 2pi)。
    #
    # 好處：
    # 1) 可以直接排序角度
    # 2) 不會受 -pi~pi 與 0~2pi 表示差異影響
    a %= PI2
    if a < 0:
        a += PI2
    return a


def hit_distance(angle, seg):
    # 算出從原點朝 angle 的射線，是否會打到 seg 這條鏡子線段。
    #
    # 回傳值：
    # - 有打到：回傳交點距離（沿射線方向的 t）
    # - 沒打到：回傳 None
    #
    # 這裡把射線與線段都寫成參數式：
    #   射線:  O + t * d, t >= 0
    #   線段:  S + u * v, 0 <= u <= 1
    # 然後解 t, u 判斷是否相交。
    sx, sy, ex, ey = seg
    dx = math.cos(angle)
    dy = math.sin(angle)

    vx = ex - sx
    vy = ey - sy
    den = cross(dx, dy, vx, vy)

    # 不平行：可用叉積公式直接解交點參數。
    if abs(den) > EPS:
        t = cross(sx, sy, vx, vy) / den
        u = cross(sx, sy, dx, dy) / den
        if t > EPS and -EPS <= u <= 1.0 + EPS:
            return t
        return None

    # 平行時：
    # - 若不共線，絕不相交
    # - 若共線，可能有重疊，把線段端點投影到射線方向，
    #   取最小正向距離當可見點。
    if abs(cross(sx, sy, dx, dy)) > EPS or abs(cross(ex, ey, dx, dy)) > EPS:
        return None

    t1 = dot(sx, sy, dx, dy)
    t2 = dot(ex, ey, dx, dy)
    lo = min(t1, t2)
    hi = max(t1, t2)

    # hi <= 0 表示整段都在原點後方，不可見。
    if hi <= EPS:
        return None
    # lo > 0 表示整段都在前方，取最近端。
    if lo > EPS:
        return lo
    # 若區間跨過原點，回傳極小正值，代表沿此方向可以立刻看到它。
    return EPS


def visible_mirrors(segments):
    # 主邏輯：找每一面鏡子是否「至少有一小段可見」。
    #
    # 做法（好記版本）：
    # 1) 收集每條線段兩端點的角度
    # 2) 取候選角度：端點角 + 相鄰端點角中點
    # 3) 對每個候選角射線，找最前面的鏡子
    # 4) 被選到過至少一次的鏡子標記為可見（1）
    n = len(segments)
    if n == 0:
        return []

    # 把所有端點角度收集起來。
    angles = []
    for sx, sy, ex, ey in segments:
        angles.append(norm_angle(math.atan2(sy, sx)))
        angles.append(norm_angle(math.atan2(ey, ex)))

    angles.sort()

    # 去掉非常接近的重複角度。
    uniq = []
    for a in angles:
        if not uniq or abs(a - uniq[-1]) > 1e-12:
            uniq.append(a)

    # 候選角度 =
    # - 端點本身角度（處理共線或邊界情況）
    # - 相鄰角度中點（代表這個角度區間內的典型視線）
    #
    # 直覺上：可見性只會在「事件角」附近改變，
    # 所以檢查這些代表角度就足夠。
    cand = list(uniq)
    m = len(uniq)
    for i in range(m):
        a = uniq[i]
        b = uniq[(i + 1) % m]
        diff = (b - a) % PI2
        if diff > 1e-12:
            cand.append(norm_angle(a + diff / 2.0))

    seen = [0] * n

    # 每條候選射線都找「距離最近的鏡子」。
    # 最近者會遮住後面的鏡子，所以只有最近者可見。
    for ang in cand:
        best = None
        best_ids = []

        for i, seg in enumerate(segments):
            d = hit_distance(ang, seg)
            if d is None:
                continue

            # 更新最近距離。
            if best is None or d < best - EPS:
                best = d
                best_ids = [i]
            elif abs(d - best) <= EPS:
                # 幾何上若同距離，視為同時可見。
                best_ids.append(i)

        for i in best_ids:
            seen[i] = 1

    return seen


def solve(text):
    # EOF 多組測資：
    # n
    # sx sy ex ey (共 n 行)
    #
    # 題目敘述寫「輸入有多組測資」，
    # 所以這裡用 while 讀到 token 結束。
    arr = text.split()
    p = 0
    out = []

    while p < len(arr):
        n = int(arr[p])
        p += 1

        # 若平台採用 n=0 當結束符，也能兼容。
        if n == 0:
            break

        segs = []
        for _ in range(n):
            sx = int(arr[p])
            sy = int(arr[p + 1])
            ex = int(arr[p + 2])
            ey = int(arr[p + 3])
            p += 4
            segs.append((sx, sy, ex, ey))

        # 依題目格式輸出 n 個 0/1。
        out.append(" ".join(map(str, visible_mirrors(segs))))

    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
