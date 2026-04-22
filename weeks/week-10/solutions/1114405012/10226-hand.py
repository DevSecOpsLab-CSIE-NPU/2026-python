from __future__ import annotations

import sys


def solve_case(n: int, forbidden: list[set[int]]) -> str:
    # 手打版：邏輯和 easy 相同，維持最直覺的 DFS 寫法。
    letters = [chr(ord("A") + i) for i in range(n)]
    used = [False] * n
    path: list[str] = []
    all_permutations: list[str] = []

    def dfs(pos: int) -> None:
        if pos == n:
            all_permutations.append("".join(path))
            return

        for i, ch in enumerate(letters):
            if used[i]:
                continue
            if pos + 1 in forbidden[i]:
                continue

            used[i] = True
            path.append(ch)
            dfs(pos + 1)
            path.pop()
            used[i] = False

    dfs(0)

    # 只輸出和前一個排列不同的尾端字串。
    out: list[str] = []
    prev = ""
    for perm in all_permutations:
        same = 0
        while same < len(prev) and prev[same] == perm[same]:
            same += 1
        out.append(perm[same:])
        prev = perm
    return "\n".join(out)


def main() -> None:
    lines = sys.stdin.read().splitlines()
    idx = 0
    answers: list[str] = []

    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue

        n = int(lines[idx].strip())
        idx += 1
        forbidden: list[set[int]] = []
        for _ in range(n):
            nums = list(map(int, lines[idx].split()))
            idx += 1
            forbidden.append({x for x in nums if x != 0})

        answers.append(solve_case(n, forbidden))

    sys.stdout.write("\n\n".join(answers))


if __name__ == "__main__":
    main()