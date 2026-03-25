import sys

# 假設 input() 讀取方式，邏輯最直觀
def solve():
    # 讀取測試資料組數
    t = int(input())
    for _ in range(t):
        # 讀取一整列，把第一個數字 (r) 拿掉，剩下的就是門牌號碼
        data = list(map(int, input().split()))
        r = data[0]
        streets = sorted(data[1:])  # 排序後面的門牌
        
        # 直接抓中間那個數
        median = streets[r // 2]
        
        # 一行搞定：計算總距離
        print(sum(abs(s - median) for s in streets))

if __name__ == "__main__":
    solve()