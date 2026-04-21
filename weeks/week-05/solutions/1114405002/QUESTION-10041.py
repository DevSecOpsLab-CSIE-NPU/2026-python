import sys


def solve(data: bytes) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    t = nums[0]
    idx = 1
    out = []

    for _ in range(t):
        r = nums[idx]
        idx += 1
        streets = nums[idx:idx + r]
        idx += r

        streets.sort()
        m = streets[r // 2]
        out.append(str(sum(abs(x - m) for x in streets)))

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
