import io
import sys

# 這裡放入我們剛才寫好的核心邏輯函數，稍微修改以接收字串輸入
def calculate_rain(input_str):
    input_data = input_str.split()
    if not input_data: return ""
    
    ptr = 0
    results = []
    while ptr < len(input_data):
        try:
            N = int(input_data[ptr]); W = int(input_data[ptr+1])
            T = int(input_data[ptr+2]); V = int(input_data[ptr+3])
            ptr += 4
        except: break

        steps = 5000 # 提高測試精度
        dt = T / steps
        total_covered_space_time = 0

        # 預先讀取該組測資的所有傘資訊，避免重複計算
        umbrellas = []
        for _ in range(N):
            umbrellas.append((int(input_data[ptr]), int(input_data[ptr+1]), int(input_data[ptr+2])))
            ptr += 3

        for s in range(steps):
            t = (s + 0.5) * dt
            intervals = []
            for x_start, length, speed in umbrellas:
                if speed == 0:
                    l_pos = x_start
                else:
                    D = W - length
                    if D <= 0: l_pos = 0
                    else:
                        period = 2 * D
                        # 邏輯：將初始位置與位移轉換為週期內的座標
                        initial_offset = x_start if speed > 0 else (2 * D - x_start)
                        total_dist = abs(speed) * t
                        curr = (initial_offset + total_dist) % period
                        l_pos = curr if curr <= D else (2 * D - curr)
                
                r_pos = min(l_pos + length, W)
                l_pos = max(l_pos, 0)
                if l_pos < r_pos: intervals.append((l_pos, r_pos))
            
            if not intervals: continue
            intervals.sort()
            merged_len = 0
            if intervals:
                cur_s, cur_e = intervals[0]
                for i in range(1, len(intervals)):
                    nxt_s, nxt_e = intervals[i]
                    if nxt_s < cur_e: cur_e = max(cur_e, nxt_e)
                    else:
                        merged_len += cur_e - cur_s
                        cur_s, cur_e = nxt_s, nxt_e
                merged_len += cur_e - cur_s
            total_covered_space_time += merged_len * dt

        ans = (W * T - total_covered_space_time) * V
        results.append(f"{max(0.0, ans):.2f}")
    return "\n".join(results)

# --- 測試套件 ---
def run_tests():
    test_cases = [
        {
            "name": "基本情境：無傘遮擋",
            "input": "0 10 10 1", # 0把傘, 寬10, 10秒, V=1
            "expected": "100.00"  # 10 * 10 * 1 = 100
        },
        {
            "name": "靜止傘：遮住一半路面",
            "input": "1 10 10 1\n0 5 0", # 1把傘, 寬10, 10秒, V=1, 位置0, 長5, 速度0
            "expected": "50.00"   # (100 - 5*10) * 1 = 50
        },
        {
            "name": "移動傘：剛好走完一圈",
            "input": "1 10 10 1\n0 5 1", # 傘長5, 需移動5距離到終點, 速度1, 往返共10秒
            "expected": "50.00"   # 均速運動下，長度5的傘在寬10的路面恆定遮住50%時間
        },
        {
            "name": "多傘重疊：兩把靜止傘重合",
            "input": "2 10 10 1\n0 5 0\n0 5 0", 
            "expected": "50.00"   # 重疊後遮蔽面積不變
        },
        {
            "name": "多傘重疊：兩把靜止傘分開",
            "input": "2 10 10 1\n0 5 0\n5 5 0", 
            "expected": "0.00"    # 5+5=10，全遮住了
        }
    ]

    print(f"{'測試名稱':<25} | {'結果':<10}")
    print("-" * 40)
    
    for case in test_cases:
        actual = calculate_rain(case["input"])
        status = "✅ 通過" if actual == case["expected"] else f"❌ 失敗 (得到 {actual})"
        print(f"{case['name']:<25} | {status}")

if __name__ == "__main__":
    run_tests()