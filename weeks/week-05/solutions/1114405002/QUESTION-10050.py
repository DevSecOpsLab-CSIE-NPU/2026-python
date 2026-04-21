import sys


def solve(data: bytes) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    t = nums[0]
    idx = 1
    out = []

    for _ in range(t):
        n = nums[idx]
        idx += 1
        p = nums[idx]
        idx += 1

        lost = set()
        for _ in range(p):
            h = nums[idx]
            idx += 1

            for day in range(h, n + 1, h):
                mod = day % 7
                if mod == 6 or mod == 0:
                    continue
                lost.add(day)

        out.append(str(len(lost)))

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
