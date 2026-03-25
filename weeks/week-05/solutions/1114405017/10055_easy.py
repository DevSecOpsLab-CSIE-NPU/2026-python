import sys

# 快速讀取所有輸入
input = sys.stdin.read().split()
if not input: exit()

N, Q = int(input[0]), int(input[1])
bit = [0] * (N + 1)

# 1. 核心更新函數 (修改單點)
def update(i):
    while i <= N:
        bit[i] ^= 1    # 因為是反轉，直接 XOR 1 即可
        i += i & -i    # 往父節點走

# 2. 核心查詢函數 (查詢 1 到 i 的 XOR 總和)
def query(i):
    res = 0
    while i > 0:
        res ^= bit[i]
        i -= i & -i    # 往子節點走
    return res

# 處理指令
ptr = 2
out = []
for _ in range(Q):
    op = input[ptr]
    if op == '1':
        idx = int(input[ptr+1])
        update(idx)
        ptr += 2
    else:
        L, R = int(input[ptr+1]), int(input[ptr+2])
        # 區間 [L, R] 的增減性 = query(R) XOR query(L-1)
        out.append(str(query(R) ^ query(L-1)))
        ptr += 3

# 一次性輸出，速度最快
sys.stdout.write('\n'.join(out) + '\n')