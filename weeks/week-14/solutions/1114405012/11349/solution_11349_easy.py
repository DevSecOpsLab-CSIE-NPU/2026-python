import sys


# 簡化版的核心想法：
# 1. 逐組讀入測資
# 2. 把矩陣存起來
# 3. 檢查每個元素是否非負
# 4. 檢查它是否和中心對面的元素相同
# 只要有任何一個條件不成立，就不是對稱矩陣。
def main() -> None:
    # 一次把所有輸入讀進來，切成多行，
    # 這樣可以很方便地依照順序逐步取用。
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    # 第一行是測試資料的組數。
    total_cases = int(lines[0])

    # index 用來記錄現在讀到第幾行。
    # 每讀完一行就往後移動一格，避免重複處理同一筆資料。
    index = 1

    # 把每一組測資的答案先存起來，最後再一次輸出。
    outputs = []

    for case_number in range(1, total_cases + 1):
        # 題目每組測資的第一行格式固定是 N = n。
        # 例如 N = 3，就代表接下來有 3 行、每行有 3 個數字。
        size = int(lines[index].split("=")[1])
        index += 1

        # 讀入 n x n 的矩陣。
        # 每一行先用 split() 切開，再轉成整數 list。
        matrix = []
        for _ in range(size):
            matrix.append(list(map(int, lines[index].split())))
            index += 1

        # 先假設這組測資是符合條件的。
        # 只要發現一個負數，或一個位置和中心對面不同，就改成 False。
        symmetric = True

        # 逐一檢查矩陣中的每個位置。
        # row 是目前列的位置，col 是目前行的位置。
        for row in range(size):
            for col in range(size):
                # 第一個條件：題目要求所有數字都必須是非負數。
                if matrix[row][col] < 0:
                    symmetric = False
                    break

                # 第二個條件：中心對稱。
                # 也就是 matrix[row][col] 必須等於矩陣中心對面的那個位置。
                # 對面位置可以用 (size - 1 - row, size - 1 - col) 算出來。
                if matrix[row][col] != matrix[size - 1 - row][size - 1 - col]:
                    symmetric = False
                    break

            # 只要已經判定不是對稱矩陣，就不用再繼續檢查剩下的元素。
            if not symmetric:
                break

        # 依照題目的輸出格式，把結果整理成一行。
        status = "Symmetric." if symmetric else "Non-symmetric."
        outputs.append(f"Test #{case_number}: {status}")

    # 多組測資之間用換行隔開，最後一次輸出。
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
