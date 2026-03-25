import sys

def solve():
    # 讀取測試組數
    line = sys.stdin.readline()
    if not line:
        return
    t = int(line.strip())
    
    for _ in range(t):
        # 讀取總天數 N 與政黨數 P
        n = int(sys.stdin.readline().strip())
        p = int(sys.stdin.readline().strip())
        
        # 使用 set 或 boolean array 來記錄罷會日期，避免重複計算
        hartal_days = [False] * (n + 1)
        
        for _ in range(p):
            h = int(sys.stdin.readline().strip())
            # 從 h 開始，每隔 h 天標記一次
            for day in range(h, n + 1, h):
                # 排除星期五 (day % 7 == 6) 與 星期六 (day % 7 == 0)
                if day % 7 != 6 and day % 7 != 0:
                    hartal_days[day] = True
        
        # 計算 True 的總數即為損失的工作天
        print(sum(hartal_days))

if __name__ == "__main__":
    solve()