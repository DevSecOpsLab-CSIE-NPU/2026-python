from __future__ import annotations

import sys


def solve_one_case(n: int, forbidden: list[set[int]]) -> str:
    """
    簡單記法：
    1. 用 DFS 依序填第 1 個位置、第 2 個位置...。
    2. 每次嘗試還沒用過的人，且不能填到他討厭的位置。
    3. 產生的排列天然就是字典序。
    4. 輸出時和上一個排列比對，只印出「第一個不同字元之後」的後綴。
    """
    used = [False] * n
    path = [""] * n
    previous = ""
    outputs: list[str] = []

    def dfs(position: int) -> None:
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


def solve(data: str) -> str:
    lines = data.splitlines()
    i = 0
    all_cases: list[str] = []

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


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
