import sys


def cost_in_base(n, base, costs):
    # 計算十進位整數 n 在 base 進位下的「印刷總成本」。
    #
    # costs 的索引 0~35 分別對應字元：
    # 0~9, A~Z。
    # 例如：costs[10] 代表字元 A 的印刷成本。

    # n == 0 是特例：任何進位下都寫成單一字元「0」，
    # 所以成本就是 costs[0]。
    if n == 0:
        return costs[0]

    # n > 0 時，透過「連續取餘數」取得每一位數字：
    # n % base 會得到目前最低位的數字值。
    # n //= base 會把最低位移除，繼續處理下一位。
    total = 0
    while n > 0:
        # 把該位數字對應到印刷成本後累加。
        total += costs[n % base]
        n //= base

    # 全部位數加總後，即為此進位下的總成本。
    return total


def solve(text):
    # 題目輸入都是整數，使用 split() 直接切 token 最直覺。
    arr = text.split()

    # p 是讀取指標（pointer），指向下一個要讀的 token。
    p = 0

    # 第一個數字是測資組數。
    t = int(arr[p])
    p += 1

    # out 用來收集最後要輸出的每一行。
    out = []

    # case_id 從 1 開始，符合題目輸出格式 Case X:
    for case_id in range(1, t + 1):
        # 每組測資先讀 36 個成本值。
        # 對應關係是：0~9, A~Z（共 36 個字元）。
        costs = list(map(int, arr[p : p + 36]))
        p += 36

        # 接著讀本組有幾個查詢數字。
        q = int(arr[p])
        p += 1

        out.append(f"Case {case_id}:")

        # 逐一處理每個查詢數字 n。
        for _ in range(q):
            n = int(arr[p])
            p += 1

            # best_cost: 目前找到的最低成本
            # best_bases: 所有達到最低成本的進位（需全部輸出）
            best_cost = None
            best_bases = []

            # 題目規定只需比較 2~36 進位。
            for base in range(2, 37):
                c = cost_in_base(n, base, costs)

                # 第一次比較或找到更低成本，就更新最佳解。
                if best_cost is None or c < best_cost:
                    best_cost = c
                    best_bases = [base]

                # 若成本相同，代表同分最佳解，要一起保留。
                elif c == best_cost:
                    best_bases.append(base)

            # 依題目格式輸出該查詢的所有最佳進位。
            out.append(
                f"Cheapest base(s) for number {n}: {' '.join(map(str, best_bases))}"
            )

        # 不同 case 之間要空一行；最後一組後面不加空行。
        if case_id != t:
            out.append("")

    # 把所有輸出行組成最終字串。
    return "\n".join(out)


def main():
    # 從標準輸入讀入完整內容，交給 solve 處理。
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
