import re
import sys


def is_symmetric(matrix):
    # 把矩陣想成從左上角和右下角同時往中間看。
    # 如果每一格都和它的「中心鏡像格」相同，而且沒有任何負數，就通過。
    size = len(matrix)
    for row in range(size):
        for col in range(size):
            value = matrix[row][col]
            mirror_value = matrix[size - 1 - row][size - 1 - col]
            if value < 0:
                return False
            if value != mirror_value:
                return False
    return True


def solve(data):
    # 題目輸入雖然看起來像固定格式，但實際上會出現「N = 3」這種寫法。
    # 所以先把每一行清掉空白，再用正規表示法抓出真正的數字。
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    total_cases = int(lines[0])
    index = 1
    outputs = []

    for case_no in range(1, total_cases + 1):
        # 例如「N = 3」只要抓出 3 就好。
        size_text = lines[index]
        index += 1
        match = re.search(r"-?\d+", size_text)
        size = int(match.group()) if match else 0

        # 讀進整個矩陣。
        matrix = []
        for _ in range(size):
            row = list(map(int, lines[index].split()))
            matrix.append(row)
            index += 1

        # 題目要的是中心對稱，不是轉置對稱。
        if is_symmetric(matrix):
            outputs.append(f"Test #{case_no}: Symmetric.")
        else:
            outputs.append(f"Test #{case_no}: Non-symmetric.")

    return "\n".join(outputs)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()