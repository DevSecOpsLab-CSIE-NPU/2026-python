# 簡單版雨水體積計算程式
# 使用繁體中文註解說明

import sys

def merge_intervals(intervals):
    # 合併重疊區間並計算總長度
    if not intervals:
        return 0
    intervals.sort()  # 排序區間
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # 如果重疊
            merged[-1] = (last[0], max(last[1], current[1]))  # 合併
        else:
            merged.append(current)  # 不重疊，加入
    total = sum(end - start for start, end in merged)  # 計算總長度
    return total

def main():
    # 讀取所有輸入
    lines = sys.stdin.readlines()
    data = []
    for line in lines:
        data.extend(line.split())
    index = 0
    N = int(data[index])  # 自動傘數目
    index += 1
    W = int(data[index])  # 馬路寬度
    index += 1
    T = int(data[index])  # 統計時間
    index += 1
    V = float(data[index])  # 降雨速率
    index += 1
    intervals = []
    for _ in range(N):
        x = int(data[index])  # 傘初始位置
        index += 1
        l = int(data[index])  # 傘長度
        index += 1
        v = int(data[index])  # 速度（忽略，因為平均遮蓋相同）
        index += 1
        intervals.append((x, x + l))  # 傘遮蓋區間
    covered = merge_intervals(intervals)  # 計算總遮蓋長度
    uncovered = W - covered  # 未遮蓋長度
    volume = V * uncovered * T  # 總體積
    print(f"{volume:.2f}")  # 輸出結果

if __name__ == "__main__":
    main()