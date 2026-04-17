import sys


# UVA 10041 - Vito's Family
# 想讓到所有親戚的總距離最小，最佳位置是「中位數」。
def main() -> None:
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return

    t = nums[0]  # 測資組數
    idx = 1
    ans = []

    for _ in range(t):
        r = nums[idx]  # 親戚數量
        idx += 1
        arr = nums[idx:idx + r]  # 親戚門牌
        idx += r

        arr.sort()
        mid = arr[r // 2]  # 中位數位置

        total = 0
        for x in arr:
            total += abs(x - mid)

        ans.append(str(total))

    print("\n".join(ans))


if __name__ == "__main__":
    main()
