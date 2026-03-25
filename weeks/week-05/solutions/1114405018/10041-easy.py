# UVA 10041 - Vito's Family (簡單好記版)
# 重點口訣：
# 1) 排序
# 2) 取中位數
# 3) 算到中位數的距離總和

import sys


def main() -> None:
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return

    t = nums[0]  # 測資組數
    i = 1
    ans = []

    for _ in range(t):
        r = nums[i]  # 親戚人數
        i += 1

        a = nums[i:i + r]
        i += r

        a.sort()
        m = a[r // 2]  # 中位數（偶數時取右中位數也可）

        total = 0
        for x in a:
            total += abs(x - m)

        ans.append(str(total))

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()
