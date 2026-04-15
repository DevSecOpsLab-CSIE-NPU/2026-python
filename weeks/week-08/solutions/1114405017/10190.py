import sys

def solve():
    # 讀取所有輸入數據
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    while ptr < len(input_data):
        try:
            N = int(input_data[ptr])      # 傘的數量
            W = int(input_data[ptr+1])    # 馬路寬度
            T = int(input_data[ptr+2])    # 統計時間
            V = int(input_data[ptr+3])    # 單位降雨量
            ptr += 4
        except EOFError:
            break
        except IndexError:
            break

        # 準備模擬時間切片，步長越小精度越高
        # 對於大多數競賽題目，1000~5000 個切片通常能達到小數點後兩位的精度
        steps = 4000 
        dt = T / steps
        total_covered_space_time = 0

        for s in range(steps):
            # 取每一小段時間的中點來代表該時段的覆蓋狀態
            t = (s + 0.5) * dt
            intervals = []
            
            # 計算每把傘在時刻 t 的覆蓋區間 [L, R]
            temp_ptr = ptr
            for _ in range(N):
                x_start = int(input_data[temp_ptr])
                length = int(input_data[temp_ptr+1])
                speed = int(input_data[temp_ptr+2])
                temp_ptr += 3
                
                if speed == 0:
                    # 靜止不動的情況
                    l_pos = x_start
                else:
                    # 往返運動邏輯：
                    # 傘能移動的總範圍為 D = W - length
                    D = W - length
                    if D <= 0:
                        # 如果傘比馬路寬或一樣寬，整段都被遮住
                        l_pos = 0
                    else:
                        # 計算 t 秒後相對於初始位置的總位移
                        total_dist = abs(speed) * t
                        # 初始方向判定：speed > 0 向右，speed < 0 向左
                        # 我們將運動轉化為在 [0, 2*D] 週期內的線性運動
                        period = 2 * D
                        
                        # 起點校準
                        if speed > 0:
                            initial_pos = x_start
                        else:
                            initial_pos = D + (D - x_start)
                        
                        current_pos_in_period = (initial_pos + total_dist) % period
                        
                        if current_pos_in_period <= D:
                            l_pos = current_pos_in_period
                        else:
                            l_pos = 2 * D - current_pos_in_period
                
                # 將該傘的覆蓋區間加入列表，確保不超出馬路邊界 [0, W]
                r_pos = min(l_pos + length, W)
                l_pos = max(l_pos, 0)
                if l_pos < r_pos:
                    intervals.append((l_pos, r_pos))
            
            # --- 區間聯集演算法 (Merge Intervals) ---
            if not intervals:
                continue
            
            # 1. 按左端點排序
            intervals.sort()
            
            # 2. 合併重疊區間
            merged_len = 0
            curr_start, curr_end = intervals[0]
            
            for i in range(1, len(intervals)):
                next_start, next_end = intervals[i]
                if next_start < curr_end:
                    # 有重疊，更新當前結束點
                    curr_end = max(curr_end, next_end)
                else:
                    # 無重疊，累加長度並開啟新區間
                    merged_len += curr_end - curr_start
                    curr_start, curr_end = next_start, next_end
            merged_len += curr_end - curr_start
            
            # 將此時段的覆蓋寬度累加到總時空面積
            total_covered_space_time += merged_len * dt

        # 更新輸入指針
        ptr += N * 3
        
        # 最終計算：(總時空面積 - 遮蔽時空面積) * 降雨率
        # 總時空面積 = 馬路寬 W * 時間 T
        ans = (W * T - total_covered_space_time) * V
        
        # 格式化輸出到小數點後兩位
        print(f"{max(0.0, ans):.2f}")

if __name__ == "__main__":
    solve()