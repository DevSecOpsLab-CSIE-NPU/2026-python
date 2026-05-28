import sys


def solve(data: str) -> str:
    md = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    wd = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    nums = list(map(int, data.split()))
    out = []
    p = 1
    for _ in range(nums[0]):
        m, d = nums[p], nums[p + 1]
        p += 2
        out.append(wd[(sum(md[:m - 1]) + d - 1) % 7])
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
