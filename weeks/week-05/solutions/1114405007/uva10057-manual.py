from sys import stdin


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