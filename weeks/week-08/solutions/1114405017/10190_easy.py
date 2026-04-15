import sys

def solve():
    # 使用 generator 讀取所有輸入，避免處理 Index 錯誤
    data = (float(x) for x in sys.stdin.read().split())
    
    for n in data:
        n = int(n)
        w, t, v = next(data), next(data), next(data)
        umbrellas = [ [next(data), next(data), next(data)] for _ in range(n) ]
        
        covered_area = 0
        steps = 2000 # 兼顧精度與速度的步長
        dt = t / steps
        
        for s in range(steps):
            curr_t = (s + 0.5) * dt
            intervals = []
            for x0, l, spd in umbrellas:
                if spd == 0:
                    l_pos = x0
                else:
                    d = w - l # 可移動範圍
                    if d <= 0: l_pos = 0
                    else:
                        # 核心簡化：將運動映射到 [0, 2*d] 的循環中
                        # 若 spd < 0，初始位置視為在回程 (2*d - x0)
                        pos = ((x0 if spd > 0 else 2*d - x0) + abs(spd) * curr_t) % (2*d)
                        l_pos = pos if pos <= d else 2*d - pos
                intervals.append((max(0, l_pos), min(w, l_pos + l)))
            
            # 簡化版區間合併
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