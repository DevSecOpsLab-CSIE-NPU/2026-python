import sys


def main() -> None:
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return

    t = nums[0]
    idx = 1
    ans = []

    for _ in range(t):
        r = nums[idx]
        idx += 1
        arr = nums[idx:idx + r]
        idx += r

        arr.sort()
        mid = arr[r // 2]
        total = 0
        for x in arr:
            total += abs(x - mid)
        ans.append(str(total))

    print("\n".join(ans))


if __name__ == "__main__":
    main()
