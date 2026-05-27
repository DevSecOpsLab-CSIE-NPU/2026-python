import re
import sys


def solve(data):
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    total = int(lines[0])
    position = 1
    result = []

    for case_no in range(1, total + 1):
        size = int(re.search(r"\d+", lines[position]).group())
        position += 1

        matrix = [list(map(int, lines[position + i].split())) for i in range(size)]
        position += size

        ok = True
        for i in range(size):
            for j in range(size):
                if matrix[i][j] < 0 or matrix[i][j] != matrix[size - 1 - i][size - 1 - j]:
                    ok = False
                    break
            if not ok:
                break

        result.append(f"Test #{case_no}: {'Symmetric' if ok else 'Non-symmetric'}.")

    return "\n".join(result)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))