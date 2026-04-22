import sys


def solve_one_case(n, forbidden):
    used = [False] * n
    path = [""] * n
    previous = ""
    outputs = []

    def dfs(position):
        nonlocal previous
        if position == n:
            now = "".join(path)
            if previous == "":
                outputs.append(now)
            else:
                idx = 0
                while idx < n and previous[idx] == now[idx]:
                    idx += 1
                outputs.append(now[idx:])
            previous = now
            return

        for person in range(n):
            if used[person]:
                continue
            if (position + 1) in forbidden[person]:
                continue
            used[person] = True
            path[position] = chr(ord("A") + person)
            dfs(position + 1)
            used[person] = False

    dfs(0)
    return "\n".join(outputs)


def solve(data):
    lines = data.splitlines()
    i = 0
    all_cases = []

    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue

        n = int(line)
        forbidden = [set() for _ in range(n)]
        for person in range(n):
            values = [int(x) for x in lines[i].split()]
            i += 1
            for pos in values:
                if pos == 0:
                    break
                forbidden[person].add(pos)

        all_cases.append(solve_one_case(n, forbidden))

    return "\n\n".join(all_cases)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
