import sys

def solve():
    # 讀取測試資料組數
    line = sys.stdin.readline()
    if not line:
        return
    try:
        n = int(line.strip())
    except ValueError:
        return
    
    for _ in range(n):
        # 讀取 S (和) 與 D (差)
        data = sys.stdin.readline().split()
        if not data:
            break
        s = int(data[0])
        d = int(data[1])
        
        # 根據數學公式：
        # a + b = s
        # a - b = d
        # 2a = s + d  => a = (s + d) / 2
        # 2b = s - d  => b = (s - d) / 2
        
        # 判斷是否有解：
        # 1. s 必須大於等於 d (得分不能為負)
        # 2. (s + d) 必須是偶數 (得分必須是整數)
        if s < d or (s + d) % 2 != 0:
            print("impossible")
        else:
            a = (s + d) // 2
            b = (s - d) // 2
            print(f"{a} {b}")

if __name__ == "__main__":
    solve()
