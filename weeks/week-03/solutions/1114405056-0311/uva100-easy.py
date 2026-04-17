import sys


# 用字典記住算過的 cycle length，避免重複計算。
memo = {1: 1}


def cycle_length(n: int) -> int:
    """計算單一數字 n 的 cycle length（包含 n 與 1）。"""
    start = n
    path = []

    # 持續走 Collatz 規則，直到走到已知長度的節點。
    while n not in memo:
        path.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2

    # 反向回填，讓 path 內每個點都得到正確長度。
    length = memo[n]
    for value in reversed(path):
        length += 1
        memo[value] = length

    return memo[start]


def max_cycle(i: int, j: int) -> int:
    """找出區間 [min(i, j), max(i, j)] 的最大 cycle length。"""
    left = min(i, j)
    right = max(i, j)

    best = 0
    for n in range(left, right + 1):
        best = max(best, cycle_length(n))
    return best


def solve(data: str) -> str:
    """依題目格式輸入多行 i j，輸出 i j max_cycle。"""
    out = []
    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        i, j = map(int, line.split())
        out.append(f"{i} {j} {max_cycle(i, j)}")

    return "\n".join(out)


def main() -> None:
    text = sys.stdin.read()
    ans = solve(text)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
