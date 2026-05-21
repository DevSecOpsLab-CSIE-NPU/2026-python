import sys

"""
UVA 11005 - Cheapest Base(s)

這個檔案是針對題目所寫的正式解法，採用暴力枚舉 2~36 進位並計算每個進位的印刷成本。
註解重點說明：
- `calc_cost`: 把十進位數字轉為指定進位，並利用 costs 表加總每一位的印刷成本。
- `main`: 一次性讀取所有輸入，以索引方式解析每組測資，最後一次輸出全部結果以避免格式錯誤。

此檔為正式版（非 easy），包含較多輸出格式控制以吻合 judge 要求。
"""


def calc_cost(number: int, base: int, costs: list[int]) -> int:
    # 計算 number 在 base 進位下的總印刷成本。
    # 實作說明：
    # - 若 number 為 0，則該數在任何進位下都只印一個 0，直接回傳 costs[0]。
    # - 否則重覆 divmod 將最低位逐一取出，並把對應成本累加。
    if number == 0:
        # 0 在任何進位下都只會印出一個 0，所以直接回傳 0 的成本。
        return costs[0]

    total = 0
    while number > 0:
        number, digit = divmod(number, base)
        # digit 就是目前這一位的值，對應 costs[digit] 的印刷成本。
        total += costs[digit]
    return total


def main() -> None:
    # 題目的輸入全部是整數，用 split() 一次讀進來最簡單也最快。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    cases = data[index]
    index += 1
    output = []

    for case_index in range(1, cases + 1):
        # 每組測資先讀入 36 個字元成本，順序固定是 0~9、A~Z。
        # 題目規定總共有 36 個字元，因此這裡直接切片讀取。
        costs = data[index:index + 36]
        index += 36

        # 接著讀入這組測資有幾個查詢數字。
        query_count = data[index]
        index += 1

        # 多組測資之間要空一行，除了第一組以外都先補空白列。
        if case_index > 1:
            output.append("")
        output.append(f"Case {case_index}:")

        for _ in range(query_count):
            # 每個查詢數字都要找出所有成本最低的進位。
            number = data[index]
            index += 1

            # best_cost 先設成 None，代表還沒有比較過任何進位。
            best_cost = None
            best_bases = []

            # 直接嘗試 2~36 進位，雖然是暴力法，但資料量足夠小，寫法最直觀。
            for base in range(2, 37):
                current_cost = calc_cost(number, base, costs)
                if best_cost is None or current_cost < best_cost:
                    # 找到更低成本時，就更新最佳成本，並把進位清空重記。
                    best_cost = current_cost
                    best_bases = [base]
                elif current_cost == best_cost:
                    # 如果成本一樣低，就把這個進位也加入答案。
                    best_bases.append(base)

            # 輸出格式必須完全符合題目要求，進位之間用單一空白分隔。
            output.append(
                f"Cheapest base(s) for number {number}: "
                f"{' '.join(map(str, best_bases))}"
            )

    # 最後一次性輸出全部結果，避免逐行 print 造成格式處理麻煩。
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()