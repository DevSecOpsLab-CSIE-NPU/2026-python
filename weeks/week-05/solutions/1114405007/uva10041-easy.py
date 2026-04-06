from sys import stdin


# 用中位數當作新家位置，總距離一定最小。
def main():
    data = stdin.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    answer = []

    for _ in range(t):
        r = int(data[idx])
        idx += 1
        nums = list(map(int, data[idx:idx + r]))
        idx += r

        # 排序後直接取中間位置當答案。
        nums.sort()
        mid = nums[r // 2]
        total = 0
        for value in nums:
            total += abs(value - mid)
        answer.append(str(total))

    print("\n".join(answer))


if __name__ == "__main__":
    main()