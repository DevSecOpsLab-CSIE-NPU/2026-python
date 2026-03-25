import sys

nums = list(map(int, sys.stdin.read().split()))

if not nums:
    raise SystemExit

t = nums[0]

idx = 1

answers = []

for _ in range(t):
    r = nums[idx]
    idx += 1

    addresses = nums[idx:idx + r]
    idx += r

    addresses.sort()
    median = addresses[r // 2]

    total = sum(abs(x - median) for x in addresses)
    answers.append(str(total))

print("\n".join(answers))