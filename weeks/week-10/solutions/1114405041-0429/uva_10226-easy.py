from __future__ import annotations

import sys


def build_outputs(n: int, forbidden: list[list[bool]]) -> list[str]:
    used = [False] * n
    arrangement = [""] * n
    names = [chr(ord("A") + index) for index in range(n)]
    outputs: list[str] = []
    previous = ""

    def dfs(position: int) -> None:
        nonlocal previous
        if position == n:
            current = "".join(arrangement)
            if previous:
                diff = 0
                while diff < n and previous[diff] == current[diff]:
                    diff += 1
                outputs.append(current[diff:])
            else:
                outputs.append(current)
            previous = current
            return

        for person in range(n):
            if used[person] or forbidden[person][position]:
                continue
            used[person] = True
            arrangement[position] = names[person]
            dfs(position + 1)
            used[person] = False

    dfs(0)
    return outputs


def solve(data: str) -> str:
    lines = data.splitlines()
    index = 0
    results: list[str] = []

    while index < len(lines):
        line = lines[index].strip()
        index += 1
        if not line:
            continue

        n = int(line)
        forbidden = [[False] * n for _ in range(n)]
        for person in range(n):
            for value in map(int, lines[index].split()):
                if value == 0:
                    break
                forbidden[person][value - 1] = True
            index += 1

        results.append("\n".join(build_outputs(n, forbidden)))

    return "\n\n".join(results)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()