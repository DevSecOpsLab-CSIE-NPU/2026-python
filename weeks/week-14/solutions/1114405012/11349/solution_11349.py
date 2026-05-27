import sys


# 直接把整份標準輸入讀進來，
# 這樣可以一次處理多組測資，也不用一直呼叫 input()。
def main() -> None:
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    # 第一行是測資組數。
    total_cases = int(lines[0].strip())
    index = 1
    answers = []

    for case_number in range(1, total_cases + 1):
        # 每組測資的第一行固定是 N = n，
        # 取等號右邊的數字當作矩陣大小。
        size = int(lines[index].split("=")[1])
        index += 1

        # 把 n 行矩陣資料讀進二維陣列。
        matrix = []
        for _ in range(size):
            matrix.append(list(map(int, lines[index].split())))
            index += 1

        # 先假設它是對稱矩陣，
        # 只要找到一個不符合條件的元素就可以直接判定失敗。
        symmetric = True

        # 題目要的是「中心對稱」，不是轉置對稱。
        # 所以要檢查每個位置 (row, col) 是否等於它在中心對面的位置。
        for row in range(size):
            for col in range(size):
                # 題目規定所有元素都必須是非負數。
                if matrix[row][col] < 0:
                    symmetric = False
                    break
                # 中心對稱檢查：左上對右下、右上對左下。
                if matrix[row][col] != matrix[size - 1 - row][size - 1 - col]:
                    symmetric = False
                    break
            if not symmetric:
                break

        # 依照題目格式輸出每一組結果。
        result = "Symmetric." if symmetric else "Non-symmetric."
        answers.append(f"Test #{case_number}: {result}")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
