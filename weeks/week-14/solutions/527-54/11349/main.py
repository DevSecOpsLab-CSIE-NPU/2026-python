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

    if number == 0:
        return costs[0]

    total_cost = 0

    while number > 0:
        digit = number % base
        total_cost += costs[digit]
        number //= base

    return total_cost


def find_cheapest_bases(number, costs):
    """
    找出 number 在 2 到 36 進位中，成本最低的所有進位制。

    若有多個進位制成本相同，都要保留下來。
    """

    min_cost = None
    cheapest = []

    for base in range(2, 37):
        cost = calculate_cost(number, base, costs)

        if min_cost is None or cost < min_cost:
            min_cost = cost
            cheapest = [base]
        elif cost == min_cost:
            cheapest.append(base)

    return cheapest


def solve(data):
    """
    處理整份輸入資料，並回傳完整輸出字串。
    """

    tokens = data.split()
    idx = 0

    test_cases = int(tokens[idx])
    idx += 1

    output = []

    for case_num in range(1, test_cases + 1):
        costs = list(map(int, tokens[idx:idx + 36]))
        idx += 36

        query_count = int(tokens[idx])
        idx += 1

        output.append(f"Case {case_num}:")

        for _ in range(query_count):
            number = int(tokens[idx])
            idx += 1

            bases = find_cheapest_bases(number, costs)
            bases_text = " ".join(map(str, bases))
            output.append(f"Cheapest base(s) for number {number}: {bases_text}")

        if case_num != test_cases:
            output.append("")

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()

