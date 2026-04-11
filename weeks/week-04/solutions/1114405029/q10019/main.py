import sys

def solve():
    # 使用 sys.stdin 進行高效迭代讀取
    for line in sys.stdin:
        # 分割字串並轉為整數
        nums = list(map(int, line.split()))
        if not nums:
            continue
        a, b = nums
        # 直接印出絕對值差，Python int 自動處理 2^63
        print(abs(a - b))

if __name__ == "__main__":
    solve()