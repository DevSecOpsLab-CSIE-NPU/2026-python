import sys


def calculate_cost(number, base, costs):
    """
    計算 number 在指定 base 進位下的印刷總成本。

    參數：
    number：原本輸入的十進位整數
    base：目前要檢查的進位制，範圍是 2 到 36
    costs：長度為 36 的列表，costs[i] 代表數值 i 這個字元的印刷成本

    回傳：
    number 轉成 base 進位後，所有位數字元成本的總和
    """

    # 特殊情況：
    # 數字 0 在任何進位制下都表示為「0」。
    # 因此它的成本不是 0，而是印出字元 0 的成本 costs[0]。
    if number == 0:
        return costs[0]

    # total_cost 用來累加目前這個進位制下，每一位數字的印刷成本。
    total_cost = 0

    # 使用進位轉換的概念：
    # 不斷用 number % base 取得最低位數字，
    # 再用 number //= base 移除最低位。
    while number > 0:
        # digit 是目前最低位的數值。
        # 例如 number = 31, base = 16 時：
        # 31 % 16 = 15，代表最低位是 F。
        digit = number % base

        # 題目給的 costs 順序剛好對應：
        # costs[0] 代表 0 的成本，
        # costs[10] 代表 A 的成本，
        # costs[35] 代表 Z 的成本。
        total_cost += costs[digit]

        # 去掉已經處理過的最低位。
        number //= base

    return total_cost


def find_cheapest_bases(number, costs):
    """
    找出 number 在 2 到 36 進位中，成本最低的所有進位制。

    若有多個進位制成本相同，都要保留下來。
    """

    # min_cost 紀錄目前遇過的最低成本。
    # 一開始還沒有算任何 base，所以先設為 None。
    min_cost = None

    # cheapest 用來存放所有成本等於 min_cost 的進位制。
    cheapest = []

    # 題目規定只需要檢查 2 進位到 36 進位。
    for base in range(2, 37):
        # 計算 number 在目前 base 下的總成本。
        cost = calculate_cost(number, base, costs)

        # 如果這是第一個檢查的 base，
        # 或者目前成本比之前的最低成本更低，
        # 就更新最低成本，並把答案清空後放入目前 base。
        if min_cost is None or cost < min_cost:
            min_cost = cost
            cheapest = [base]

        # 如果目前成本剛好等於最低成本，
        # 表示這個 base 也是答案之一。
        elif cost == min_cost:
            cheapest.append(base)

    # 因為 base 是從 2 到 36 依序檢查，
    # 所以 cheapest 裡面的 base 自然會是升序排列。
    return cheapest


def solve(data):
    """
    處理整份輸入資料，並回傳完整輸出字串。

    將輸入輸出邏輯寫成 solve(data) 的好處：
    1. 線上評測時 main() 可以直接呼叫。
    2. test.py 測試時也可以用輸入字串檢查結果。
    3. 程式結構更清楚，方便除錯。
    """

    # 用 split() 直接把所有輸入切成 token。
    # 因為本題輸入都是整數，不需要逐行處理也能正確解析。
    tokens = data.split()

    # idx 表示目前讀到 tokens 的哪一個位置。
    idx = 0

    # 第一個數字是測試資料組數。
    test_cases = int(tokens[idx])
    idx += 1

    # output 用來收集所有輸出行，最後再一次 join 成字串。
    output = []

    for case_num in range(1, test_cases + 1):
        # 每組測試資料會給 36 個成本。
        # 這 36 個成本依序對應：
        # 0, 1, 2, ..., 9, A, B, ..., Z
        costs = list(map(int, tokens[idx:idx + 36]))
        idx += 36

        # 接著讀取查詢數量。
        query_count = int(tokens[idx])
        idx += 1

        # 每組測試資料都要先輸出 Case X:
        output.append(f"Case {case_num}:")

        # 逐一處理每個查詢數字。
        for _ in range(query_count):
            number = int(tokens[idx])
            idx += 1

            # 找出這個 number 的所有最低成本進位制。
            bases = find_cheapest_bases(number, costs)

            # 將 base 列表轉成題目要求的空格分隔格式。
            bases_text = " ".join(map(str, bases))

            # 依照題目指定格式輸出。
            output.append(f"Cheapest base(s) for number {number}: {bases_text}")

        # 題目要求不同測試資料之間空一行。
        # 但最後一組後面不需要再多補空白行。
        if case_num != test_cases:
            output.append("")

    return "\n".join(output)


def main():
    """
    主程式進入點。

    從標準輸入讀取全部資料，
    呼叫 solve() 取得答案，
    最後印出結果。
    """

    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()