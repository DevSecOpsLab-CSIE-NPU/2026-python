import sys

nums = list(map(int, sys.stdin.read().split()))

if not nums:
    raise SystemExit

t = nums[0]
idx = 1
answers = []

for _ in range(t):
    n = nums[idx]
    idx += 1
    p = nums[idx]
    idx += 1
    hartals = nums[idx:idx + p]
    idx += p

    lost_days = set()

    for h in hartals:
        for day in range(h, n + 1, h):
            weekday = day % 7
            if weekday == 6 or weekday == 0:
                continue
            lost_days.add(day)  

    answers.append(str(len(lost_days)))

print("\n".join(answers))   