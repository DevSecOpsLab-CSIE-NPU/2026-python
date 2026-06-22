import sys

D = 3


def solve(nums):
    # ① 去重（保留首次出現順序）
    seen = set()
    unique = []
    for x in nums:
        if x not in seen:
            unique.append(x)
            seen.add(x)

    # ② 只保留能被 D 整除的數
    filtered = [x for x in unique if x % D == 0]

    # ③ 由小到大排序
    filtered.sort()
    return filtered


def main():
    data = sys.stdin.read().splitlines()
    out = []
    i = 0

    while i < len(data):
        line = data[i].strip()
        if line == "":
            i += 1
            continue
        n = int(line)
        i += 1
        if n == 0:
            break
        if i >= len(data):
            break

        nums = list(map(int, data[i].strip().split()))
        i += 1

        res = solve(nums)
        out.append(" ".join(map(str, res)) if res else "NONE")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
