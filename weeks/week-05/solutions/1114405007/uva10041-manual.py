from sys import stdin


def main():
    data = stdin.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        r = int(data[idx])
        idx += 1
        nums = list(map(int, data[idx:idx + r]))
        idx += r
        nums.sort()
        mid = nums[r // 2]
        total = 0
        for value in nums:
            total += abs(value - mid)
        out.append(str(total))

    print("\n".join(out))


if __name__ == "__main__":
    main()