from sys import stdin


# 排序後找中間位置。
# 奇數個時只有一個中位數；偶數個時介於兩個中位數之間的整數都可以。
def main():
    data = stdin.read().split()
    if not data:
        return

    idx = 0
    out = []

    while idx < len(data):
        n = int(data[idx])
        idx += 1
        nums = list(map(int, data[idx:idx + n]))
        idx += n

        # low 和 high 是最小總距離可接受的中位數範圍。
        nums.sort()
        low = nums[(n - 1) // 2]
        high = nums[n // 2]

        count = 0
        for value in nums:
            if low <= value <= high:
                count += 1

        ways = high - low + 1
        out.append(f"{low} {count} {ways}")

    print("\n".join(out))


if __name__ == "__main__":
    main()