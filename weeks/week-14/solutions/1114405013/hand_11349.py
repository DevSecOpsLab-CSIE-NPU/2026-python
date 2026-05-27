def is_symmetric(matrix):

    n = len(matrix)
    return all(
        matrix[i][j] >= 0 and matrix[i][j] == matrix[n - 1 - i][n - 1 - j]
        for i in range(n)
        for j in range(n)
    )


def solve() -> None:
    t = int(input().strip())
    for case_no in range(1, t + 1):
        n = int(input().strip().split("=")[1].strip())
        matrix = [list(map(int, input().split())) for _ in range(n)]
        print(f"Test #{case_no}: {'Symmetric.' if is_symmetric(matrix) else 'Non-symmetric.'}")


if __name__ == "__main__":
    solve()
