import sys


# UVA 10050 - Hartals
# 第 1 天是星期日，因此：
# - day % 7 == 6 是星期五
# - day % 7 == 0 是星期六
# 這兩天是週末，不計入罷會工作日損失。
def is_weekend(day: int) -> bool:
    return day % 7 == 6 or day % 7 == 0


def main() -> None:
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return

    t = nums[0]
    idx = 1
    out = []

    for _ in range(t):
        n = nums[idx]  # 模擬天數
        idx += 1
        p = nums[idx]  # 政黨數量
        idx += 1

        hartals = nums[idx:idx + p]  # 各政黨罷會參數 h
        idx += p

        # lost[day] = True 代表這天是工作日且有罷會
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
