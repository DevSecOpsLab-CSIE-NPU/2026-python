import sys


def is_symmetric_matrix(values):
    """
    判斷一個已經攤平成一維串列的矩陣是否符合本題的對稱條件。

    本題的對稱不是主對角線對稱，而是中心對稱。
    也就是：
    第一個數要等於最後一個數，
    第二個數要等於倒數第二個數，
    依此類推。

    同時，題目也要求矩陣中的所有數字都必須是非負數。
    只要有任何一個數字小於 0，就不是 Symmetric。
    """

    total = len(values)

    for i in range(total):
        # 題目規定所有元素都不能是負數
        if values[i] < 0:
            return False

        # 檢查中心對稱位置是否相同
        if values[i] != values[total - 1 - i]:
            return False

    return True


def solve(data):
    """
    處理整份輸入資料，並回傳所有輸出結果。

    輸入格式中，每組測資的矩陣大小會寫成：
    N = n

    使用 split() 後會變成：
    ["N", "=", "n"]

    所以讀取每組測資時，要跳過 "N" 和 "="，
    再取得真正的矩陣大小 n。
    """

    tokens = data.split()

    if not tokens:
        return ""

    test_count = int(tokens[0])
    index = 1
    answers = []

    for case_number in range(1, test_count + 1):
        # tokens[index] 是 "N"
        # tokens[index + 1] 是 "="
        # tokens[index + 2] 才是矩陣大小 n
        n = int(tokens[index + 2])
        index += 3

        total_numbers = n * n

        # 讀取 n × n 個矩陣元素
        values = []
        for _ in range(total_numbers):
            values.append(int(tokens[index]))
            index += 1

        if is_symmetric_matrix(values):
            answers.append(f"Test #{case_number}: Symmetric.")
        else:
            answers.append(f"Test #{case_number}: Non-symmetric.")

    return "\n".join(answers)


def main():
    data = sys.stdin.read()
    result = solve(data)
    print(result)


if __name__ == "__main__":
    main()