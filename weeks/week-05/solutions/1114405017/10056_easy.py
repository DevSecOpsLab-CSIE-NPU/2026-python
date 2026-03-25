import sys

# 讀取所有輸入
data = sys.stdin.read().split()
S = int(data[0])

for k in range(S):
    # 每次跳 3 個抓取 N, p, i
    N = int(data[1 + k*3])
    p = float(data[2 + k*3])
    i = int(data[3 + k*3])
    
    if p == 0:
        print("0.0000")
    else:
        q = 1 - p
        # 分子：他在第一輪就贏的機率 (q 的 i-1 次方)
        # 分母：一整輪中「至少有一人贏」的機率 (1 - q 的 N 次方)
        ans = (p * q**(i-1)) / (1 - q**N)
        print(f"{ans:.4f}")