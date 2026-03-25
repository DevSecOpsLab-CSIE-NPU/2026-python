import sys

def solve():
    # 讀取所有輸入並轉為整數列表
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    num_test_cases = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(num_test_cases):
        r = int(input_data[idx])
        idx += 1
        # 讀取 r 個門牌號碼
        streets = [int(x) for x in input_data[idx : idx + r]]
        idx += r
        
        # 1. 排序
        streets.sort()
        
        # 2. 找到中位數
        median = streets[r // 2]
        
        # 3. 計算總距離
        total_distance = sum(abs(s - median) for s in streets)
        results.append(str(total_distance))
        
    # 輸出結果
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()