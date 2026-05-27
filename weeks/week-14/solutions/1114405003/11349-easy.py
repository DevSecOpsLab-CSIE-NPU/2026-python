import re
import sys


def is_center_symmetric(matrix):
    # 這題的「對稱」不是轉置對稱，而是「中心對稱」。
    # 也就是左上角要對應右下角、右上角要對應左下角。
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            # 先檢查非負數，再檢查鏡射位置是否相同。
            if matrix[i][j] < 0:
                return False
            if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                return False

    return True


def solve(data):
    # 把輸入拆成乾淨的行，避免空白行干擾讀取。
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    pos = 1
    result = []

    for case_no in range(1, t + 1):
        # 題目給的是 N = n，所以只要把數字抓出來即可。
        n = int(re.search(r"\d+", lines[pos]).group())
        pos += 1

        matrix = []
        for _ in range(n):
            row = list(map(int, lines[pos].split()))
            matrix.append(row)
            pos += 1

        # 一次掃描整個矩陣，找到第一個不符合的地方就可以提早結束。
        if is_center_symmetric(matrix):
            result.append(f"Test #{case_no}: Symmetric.")
        else:
            result.append(f"Test #{case_no}: Non-symmetric.")

    return "\n".join(result)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()