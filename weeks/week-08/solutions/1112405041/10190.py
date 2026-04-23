import sys

# 【August 的惡意：身分置換】
# 此題已被魔改為「雨傘覆蓋問題 (Umbrella Coverage)」。
# 原 UVA 10190 是數列除法，但在這裡必須實作：
# 給定 N 把雨傘，道路寬度 W，總時間 T。
# 每把雨傘有初始位置 x，長度 l，與移動速度 v。
# 雨傘在 0 到 W 之間來回反彈。
# 計算 T 時間內道路被覆蓋的「面積-時間」積分。

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    case_num = 1
    ptr = 0
    while ptr < len(input_data):
        try:
            n = int(input_data[ptr])
            w = int(input_data[ptr+1])
            t = int(input_data[ptr+2])
            v_rain = int(input_data[ptr+3]) # 垂直雨速，通常用於計算相對速度
            ptr += 4

            umbrellas = []
            for _ in range(n):
                x = int(input_data[ptr])
                l = int(input_data[ptr+1])
                v = int(input_data[ptr+2])
                umbrellas.append((x, l, v))
                ptr += 3

            # 核心邏輯：將時間 T 離散化或使用幾何方法計算覆蓋面積
            # 為了通過 August 的精度雷，這裡使用高頻率離散採樣積分
            dt = 0.01
            total_coverage = 0.0

            curr_t = 0.0
            while curr_t < t:
                # 找出當前時間所有雨傘的區間
                intervals = []
                for x0, l, v in umbrellas:
                    # 計算反彈後的位置
                    # 週期 P = 2 * (W - l)
                    if w == l:
                        intervals.append((0, w))
                        continue

                    dist = x0 + v * curr_t
                    p = 2 * (w - l)
                    mod_dist = dist % p
                    if mod_dist < 0: mod_dist += p

                    if mod_dist <= (w - l):
                        pos = mod_dist
                    else:
                        pos = p - mod_dist
                    intervals.append((pos, pos + l))

                # 合併區間求總長度
                intervals.sort()
                merged_len = 0
                if intervals:
                    curr_start, curr_end = intervals[0]
                    for next_start, next_end in intervals[1:]:
                        if next_start < curr_end:
                            curr_end = max(curr_end, next_end)
                        else:
                            merged_len += (curr_end - curr_start)
                            curr_start, curr_end = next_start, next_end
                    merged_len += (curr_end - curr_start)

                total_coverage += merged_len * dt
                curr_t += dt

            print(f"Case {case_num}: {total_coverage:.2f}")
            case_num += 1
        except (EOFError, IndexError):
            break

if __name__ == "__main__":
    solve()
