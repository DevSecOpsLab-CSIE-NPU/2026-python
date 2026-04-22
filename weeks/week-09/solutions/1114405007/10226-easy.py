import sys


def solve_one_case(n, lines):
    # forbid[i] 表示第 i 個人不能排到哪些位置。
    forbid = [set() for _ in range(n)]
    for i in range(n):
        nums = list(map(int, lines.readline().split()))
        forbid[i] = set(nums[:-1])

    used = [False] * n
    path = [""] * n
    last = ""
    result = []

    def dfs(pos):
        nonlocal last

        # 走到底時，組出一個完整排列。
        if pos == n:
            cur = "".join(path)

            # 題目要求：和上一筆相同的前綴不要重印。
            same = 0
            while same < len(last) and last[same] == cur[same]:
                same += 1

            result.append(cur[same:])
            last = cur
            return

        # 按 A, B, C... 的順序放，才能保證字典序。
        for i in range(n):
            if used[i]:
                continue
            if pos + 1 in forbid[i]:
                continue

            used[i] = True
            path[pos] = chr(ord("A") + i)
            dfs(pos + 1)
            used[i] = False

    dfs(0)
    return "\n".join(result)


def main():
    out = []

    while True:
        line = sys.stdin.readline()
        if not line:
            break

        line = line.strip()
        if not line:
            continue

        n = int(line)
        out.append(solve_one_case(n, sys.stdin))

    sys.stdout.write("\n\n".join(out))


if __name__ == "__main__":
    main()