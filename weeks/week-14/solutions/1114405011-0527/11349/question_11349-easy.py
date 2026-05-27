import sys


def solve(data):
    lines = data.strip().splitlines()
    if not lines:
        return ""

    t = int(lines[0].strip())
    idx = 1
    answers = []

    for case_id in range(1, t + 1):
        n = int(lines[idx].split("=")[1].strip())
        idx += 1

        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, lines[idx].split())))
            idx += 1

        ok = True
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    ok = False
                if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                    ok = False
                if not ok:
                    break
            if not ok:
                break

        if ok:
            answers.append(f"Test #{case_id}: Symmetric.")
        else:
            answers.append(f"Test #{case_id}: Non-symmetric.")

    return "\n".join(answers)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
