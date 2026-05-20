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

    if number == 0:
        return costs[0]

    total = 0
    n = number

    while n > 0:
        digit = n % base
        total += costs[digit]
        n = n // base

    return total


def solve(data):
    values = data.split()
    pos = 0

    t = int(values[pos])
    pos += 1

    answer = []

    for case_id in range(1, t + 1):
        costs = []

        for _ in range(36):
            costs.append(int(values[pos]))
            pos += 1

        q = int(values[pos])
        pos += 1

        answer.append(f"Case {case_id}:")

        for _ in range(q):
            number = int(values[pos])
            pos += 1

            best_cost = None
            best_bases = []

            for base in range(2, 37):
                current_cost = get_cost(number, base, costs)

                if best_cost is None or current_cost < best_cost:
                    best_cost = current_cost
                    best_bases = [base]
                elif current_cost == best_cost:
                    best_bases.append(base)

            bases_string = " ".join(str(base) for base in best_bases)
            answer.append(f"Cheapest base(s) for number {number}: {bases_string}")

        if case_id != t:
            answer.append("")

    return "\n".join(answer)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
