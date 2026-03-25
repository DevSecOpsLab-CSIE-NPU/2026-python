# UVA 10050 - Hartals（簡單好記版）
# 口訣：
# 1) 每個政黨按 h 的倍數標記罷工日
# 2) 星期五、星期六不算（day % 7 == 6 或 0）
# 3) 用 set 去重複，最後看天數

import sys


def main() -> None:
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return

    t = nums[0]
    i = 1
    ans = []

    for _ in range(t):
        n = nums[i]
        i += 1
        p = nums[i]
        i += 1

        hartals = nums[i:i + p]
        i += p

        lost = set()

        for h in hartals:
            day = h
            while day <= n:
                # 第 1 天是星期天：週五=6、週六=0
                if day % 7 != 6 and day % 7 != 0:
                    lost.add(day)
                day += h

        ans.append(str(len(lost)))

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()
