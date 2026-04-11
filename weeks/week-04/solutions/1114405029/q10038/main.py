import sys

def solve():
    # 使用 sys.stdin.read().split() 一次讀取所有內容，處理多筆測資
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        # 讀取接下來的 n 個數字
        nums = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        if n == 1:
            print("Jolly")
            continue
            
        # 使用 set 紀錄差值，自動處理重複與範圍
        diffs = {abs(nums[i] - nums[i-1]) for i in range(1, n)}
        
        # 檢查是否所有 1 到 n-1 都在 set 裡面
        is_jolly = True
        for i in range(1, n):
            if i not in diffs:
                is_jolly = False
                break
        
        print("Jolly" if is_jolly else "Not jolly")

if __name__ == "__main__":
    solve()