import sys


def base_cost(number: int, base: int, costs: list[int]) -> int:
    # 這個函式的目的很單純：計算 number 在 base 進位下的總印刷成本。
    # 做法是把 number 反覆除以 base，逐位取出數字，再把每一位對應的成本加總起來。

    # 先處理 0，因為 0 在任何進位下都只會有一個數字 0。
    if number == 0:
        return costs[0]

    total = 0
    while number:
        # divmod(number, base) 會同時回傳「商」和「餘數」。
        # 餘數就是目前最低位的數字，商則是剩下還沒處理的部分。
        number, digit = divmod(number, base)
        # digit 介於 0 到 base-1 之間，而題目的成本表剛好可以直接用 digit 當索引。
        total += costs[digit]
    return total


def main() -> None:
    # 題目的資料全部都是整數，而且格式固定。
    # 所以直接把整份輸入一次讀進來，再用索引一步一步往後取值，最簡單也最快。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    # index 用來記錄目前讀到哪裡，避免一直切字串或重複呼叫 input()。
    index = 0
    case_count = data[index]
    index += 1

    # answers 先把所有輸出存起來，最後一次寫出，方便控制換行格式。
    answers = []

    for case_id in range(1, case_count + 1):
        # 每組測資開頭是 36 個成本，順序固定是 0~9、A~Z。
        # 因為成本表的長度不會變，所以這裡直接切出 36 個值。
        costs = data[index:index + 36]
        index += 36

        # 接下來是這組測資要查詢幾個數字。
        query_count = data[index]
        index += 1

        # 除了第一組以外，每組測資之間都要空一行，這是題目輸出格式要求。
        if case_id > 1:
            answers.append("")
        answers.append(f"Case {case_id}:")

        for _ in range(query_count):
            # 讀入一個要查詢的十進位數字。
            number = data[index]
            index += 1

            # best 用來記錄目前看過的最小成本。
            # 一開始還沒比較過任何進位，所以設成 None。
            best = None

            # best_bases 會存所有成本一樣低的進位，最後要全部輸出。
            best_bases = []

            # 題目允許的進位是 2 到 36。
            # 這裡直接每個進位都試一次，雖然是暴力法，但 35 個進位很少，程式最好記。
            for base in range(2, 37):
                cost = base_cost(number, base, costs)

                # 如果這是第一次比較，或是找到更低成本，就更新答案。
                if best is None or cost < best:
                    best = cost
                    best_bases = [base]
                # 如果成本跟目前最低一樣，就把這個進位一起記錄起來。
                elif cost == best:
                    best_bases.append(base)

            # 最後把所有最低成本的進位組成指定格式輸出。
            answers.append(
                f"Cheapest base(s) for number {number}: "
                f"{' '.join(map(str, best_bases))}"
            )

    # 一次把所有結果輸出，格式才不容易出錯。
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()