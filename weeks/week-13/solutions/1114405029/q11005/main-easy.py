import sys


def get_cost(number, base, costs):
    """
    用最直觀、最好理解的方式計算印刷成本。

    想法：
    如果要知道 number 在 base 進位下需要花多少成本，
    就把 number 轉成 base 進位時會出現的每一位 digit 找出來，
    再把每個 digit 的成本加起來。

    例如：
    number = 31, base = 16

    31 % 16 = 15
    15 對應到十六進位的 F

    31 // 16 = 1

    1 % 16 = 1
    1 對應到字元 1

    所以 31 的 16 進位表示是 1F，
    成本就是 costs[1] + costs[15]。
    """

    # 特別注意：
    # 如果 number 是 0，不能直接進入 while n > 0。
    # 因為 0 在任何進位制下都會寫成一個字元「0」。
    # 所以成本應該是 costs[0]。
    if number == 0:
        return costs[0]

    # total 用來累加所有位數的成本。
    total = 0

    # 用 n 複製 number，避免直接改動原本傳入的 number。
    n = number

    # 只要 n 還大於 0，就代表還有位數沒有處理完。
    while n > 0:
        # n % base 可以取得目前最低位的數字。
        # 例如：
        # 10 在 2 進位中，第一次 10 % 2 = 0。
        # 10 在 10 進位中，第一次 10 % 10 = 0。
        digit = n % base

        # digit 是幾，就代表這一位使用哪個字元。
        # 題目給的成本列表 costs 剛好可以直接用 digit 當索引。
        total += costs[digit]

        # n // base 代表把目前最低位移除，
        # 繼續處理下一位。
        n = n // base

    return total


def solve(data):
    """
    讀取題目輸入，處理每一組測試資料，最後回傳完整輸出。

    這個 easy 版本的寫法刻意比較直觀：
    1. 一個一個讀取 36 個成本。
    2. 一個一個讀取查詢數字。
    3. 對每個數字檢查 2 到 36 進位。
    4. 用 best_cost 和 best_bases 記錄目前最好的答案。
    """

    # 將整份輸入用空白切開。
    # 題目輸入全部都是數字，所以不需要擔心換行位置。
    values = data.split()

    # pos 表示目前讀到 values 的位置。
    pos = 0

    # 第一個數字是測試資料組數。
    t = int(values[pos])
    pos += 1

    # answer 存放所有要輸出的文字行。
    answer = []

    for case_id in range(1, t + 1):
        # costs 存放 36 個字元成本。
        costs = []

        # 讀取 36 個成本。
        # 這些成本依序代表：
        # 0, 1, 2, ..., 9, A, B, ..., Z
        for _ in range(36):
            costs.append(int(values[pos]))
            pos += 1

        # 讀取查詢數量。
        q = int(values[pos])
        pos += 1

        # 輸出 Case 標題。
        answer.append(f"Case {case_id}:")

        for _ in range(q):
            # 讀取目前要查詢的十進位數字。
            number = int(values[pos])
            pos += 1

            # best_cost 記錄目前找到的最低印刷成本。
            # 一開始還沒有算任何進位，所以先用 None。
            best_cost = None

            # best_bases 記錄所有達到最低成本的進位制。
            best_bases = []

            # 題目要求要檢查 2 到 36 進位。
            for base in range(2, 37):
                # 計算 number 在目前 base 下的印刷成本。
                current_cost = get_cost(number, base, costs)

                # 如果這是第一次計算，
                # 或目前成本比已知最低成本還低，
                # 就更新最低成本，並重新記錄答案。
                if best_cost is None or current_cost < best_cost:
                    best_cost = current_cost
                    best_bases = [base]

                # 如果目前成本剛好等於最低成本，
                # 表示目前 base 也是答案之一。
                elif current_cost == best_cost:
                    best_bases.append(base)

            # 將答案中的進位制轉成空格分隔字串。
            bases_string = " ".join(str(base) for base in best_bases)

            # 依照題目格式加入輸出。
            answer.append(f"Cheapest base(s) for number {number}: {bases_string}")

        # 不同 Case 之間要空一行。
        # 最後一組後面不要再多加空白行。
        if case_id != t:
            answer.append("")

    return "\n".join(answer)


def main():
    """
    主程式：
    從標準輸入讀取資料，呼叫 solve()，印出結果。
    """

    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()