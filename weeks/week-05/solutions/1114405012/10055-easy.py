import sys

# 讀入所有整數
nums = list(map(int, sys.stdin.read().split()))
if not nums:
    raise SystemExit

n, q = nums[0], nums[1]
idx = 2

# state[i] = 0 代表增函數，1 代表減函數
state = [0] * (n + 1)
out = []

for _ in range(q):
    op = nums[idx]
    idx += 1

    if op == 1:
        i = nums[idx]
        idx += 1
        state[i] ^= 1  # 翻轉增/減
    else:
        l = nums[idx]
        r = nums[idx + 1]
        idx += 2

        # 區間內 1 的個數奇偶，決定合成後增/減
        parity = 0
        for j in range(l, r + 1):
            parity ^= state[j]
        out.append(str(parity))

print("\n".join(out))
