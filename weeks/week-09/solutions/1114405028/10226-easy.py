# 10226 題目簡單版
# 這個版本用回溯法，列出所有合法排列，並只輸出與前一列不同的部分。

from typing import List


def solve() -> None:
    import sys

    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    result_lines: List[str] = []

    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break

        # forbidden[i] 存第 i 個人不能排的座位
        forbidden: List[set[int]] = []
        for _ in range(n):
            row = []
            while True:
                x = int(next(it))
                if x == 0:
                    break
                row.append(x - 1)
            forbidden.append(set(row))

        previous = ""

        def backtrack(pos: int, used: int, perm: List[int]) -> None:
            nonlocal previous
            if pos == n:
                line = "".join(chr(ord("A") + x) for x in perm)
                if previous == "":
                    result_lines.append(line)
                else:
                    common = 0
                    while common < len(line) and common < len(previous) and line[common] == previous[common]:
                        common += 1
                    result_lines.append(line[common:])
                previous = line
                return

            for person in range(n):
                if (used >> person) & 1:
                    continue
                if pos in forbidden[person]:
                    continue
                perm.append(person)
                backtrack(pos + 1, used | (1 << person), perm)
                perm.pop()

        if n > 0:
            backtrack(0, 0, [])
        result_lines.append("")

    if result_lines and result_lines[-1] == "":
        result_lines.pop()

    output = "\n".join(result_lines)
    if output:
        output += "\n"
    sys.stdout.write(output)


if __name__ == "__main__":
    solve()
