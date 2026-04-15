import sys
def solve():
    data = (float(x) for x in sys.stdin.read().split())
    for n in data:
        n = int(n)
        w, t, v = next(data), next(data), next(data)
        umbrellas = [ [next(data), next(data), next(data)] for _ in range(n) ]
        covered_area = 0
        steps = 2000 
        dt = t / steps
        for s in range(steps):
            curr_t = (s + 0.5) * dt
            intervals = []
            for x0, l, spd in umbrellas:
                if spd == 0:
                    l_pos = x0
                else:
                    d = w - l 
                    if d <= 0: l_pos = 0
                    else:
                        pos = ((x0 if spd > 0 else 2*d - x0) + abs(spd) * curr_t) % (2*d)
                        l_pos = pos if pos <= d else 2*d - pos
                intervals.append((max(0, l_pos), min(w, l_pos + l)))
            if not intervals: continue
            intervals.sort()
            m_len, cur_e = 0, 0
            for s_p, e_p in intervals:
                if e_p > cur_e:
                    m_len += e_p - max(s_p, cur_e)
                    cur_e = e_p
            covered_area += m_len * dt
        print(f"{max(0.0, (w * t - covered_area) * v):.2f}")
if __name__ == "__main__":
    solve()