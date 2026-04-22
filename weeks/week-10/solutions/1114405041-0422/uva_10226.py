from __future__ import annotations

import sys


def build_outputs(n: int, forbidden: list[set[int]]) -> list[str]:
    used = [False] * n
    path = [""] * n
    outputs: list[str] = []
    prev = ""

    def dfs(pos: int) -> None:
        nonlocal prev
        if pos == n:
            current = "".join(path)
            if not prev:
                outputs.append(current)
            else:
                diff = 0
                while diff < n and prev[diff] == current[diff]:
                    diff += 1
                outputs.append(current[diff:])
            prev = current
            return

        for person in range(n):
            if used[person]:
                continue
            if (pos + 1) in forbidden[person]:
                continue
            used[person] = True
            path[pos] = chr(ord("A") + person)
            dfs(pos + 1)
            used[person] = False

    dfs(0)
    return outputs


def solve(data: str) -> str:
    lines = data.splitlines()
    i = 0
    cases: list[str] = []

    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue

        n = int(line)
        forbidden = [set() for _ in range(n)]
        for person in range(n):
            nums = [int(x) for x in lines[i].split()]
            i += 1
            for v in nums:
                if v == 0:
                    break
                forbidden[person].add(v)

        cases.append("\n".join(build_outputs(n, forbidden)))

    return "\n\n".join(cases)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
