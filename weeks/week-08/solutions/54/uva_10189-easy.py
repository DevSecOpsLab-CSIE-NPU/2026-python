import sys


def solve(data: str) -> str:
    lines = data.splitlines()
    i = 0
    case_no = 1
    outputs: list[str] = []

    while i < len(lines):
        head = lines[i].strip()
        i += 1
        if not head:
            continue

        n, m = map(int, head.split())
        if n == 0 and m == 0:
            break

        board = [list(lines[i + r].rstrip("\n")) for r in range(n)]
        i += n

        result = [["0"] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if board[r][c] == "*":
                    result[r][c] = "*"
                    continue
                cnt = 0
                for rr in range(max(0, r - 1), min(n, r + 2)):
                    for cc in range(max(0, c - 1), min(m, c + 2)):
                        if board[rr][cc] == "*":
                            cnt += 1
                result[r][c] = str(cnt)

        block = [f"Field #{case_no}:"] + ["".join(row) for row in result]
        outputs.append("\n".join(block))
        case_no += 1

    return "\n\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
