from __future__ import annotations

import sys


def solve_case(n: int, forbidden: list[set[int]]) -> str:
    # 固定人名為 A, B, C...，DFS 時自然就是字典序。
    letters = [chr(ord("A") + i) for i in range(n)]
    used = [False] * n
    current: list[str] = []
    permutations: list[str] = []

    def dfs(position: int) -> None:
        # 填滿所有位置後，得到一個合法排列。
        if position == n:
            permutations.append("".join(current))
            return

        # 逐一嘗試尚未使用的人，並檢查是否踩到不想排的位置。
        for idx, letter in enumerate(letters):
            if used[idx]:
                continue
            if position + 1 in forbidden[idx]:
                continue
            used[idx] = True
            current.append(letter)
            dfs(position + 1)
            current.pop()
            used[idx] = False

    dfs(0)

    # 依題意只輸出和上一個排列不同的尾端。
    output: list[str] = []
    previous = ""
    for permutation in permutations:
        prefix = 0
        while prefix < len(previous) and previous[prefix] == permutation[prefix]:
            prefix += 1
        output.append(permutation[prefix:])
        previous = permutation
    return "\n".join(output)


def main() -> None:
    # 讀到 EOF 為止，每筆測資為一個 N 搭配 N 行限制。
    lines = sys.stdin.read().splitlines()
    index = 0
    answers: list[str] = []

    while index < len(lines):
        if not lines[index].strip():
            index += 1
            continue
        n = int(lines[index].strip())
        index += 1
        forbidden: list[set[int]] = []
        for _ in range(n):
            positions = list(map(int, lines[index].split()))
            index += 1
            forbidden.append({value for value in positions if value != 0})
        answers.append(solve_case(n, forbidden))

    sys.stdout.write("\n\n".join(answers))


if __name__ == "__main__":
    main()