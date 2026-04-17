import sys


def is_weekend(day: int) -> bool:
    # 第 1 天是星期日，因此 day%7==6 是週五、day%7==0 是週六
    return day % 7 == 6 or day % 7 == 0


def main() -> None:
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return

    t = nums[0]
    idx = 1
    out = []

    for _ in range(t):
        n = nums[idx]
        idx += 1
        p = nums[idx]
        idx += 1

        hartals = nums[idx:idx + p]
        idx += p

        lost = [False] * (n + 1)
        for h in hartals:
            day = h
            while day <= n:
                if not is_weekend(day):
                    lost[day] = True
                day += h

        out.append(str(sum(lost)))

    print("\n".join(out))


if __name__ == "__main__":
    main()
