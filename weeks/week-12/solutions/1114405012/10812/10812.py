import sys


def solve() -> None:
    # 先一次讀完所有輸入，再用 split() 切成一個個數字字串。
    # 這樣可以同時處理空格、換行，寫法也比較適合比賽題。
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    # 第一個數字代表測資筆數，後面每兩個數字是一組 S 和 D。
    case_count = int(data[0])
    index = 1
    answers = []

    # 逐筆取出總和 S 與差值 D，依題意求兩隊分數。
    for _ in range(case_count):
        total = int(data[index])
        diff = int(data[index + 1])
        index += 2

        # 由題目公式可知：
        # 較大分數 = (S + D) / 2，較小分數 = (S - D) / 2
        # 只有在兩個值都能整除，且不出現負數時才有解。
        if total < diff:
            # 如果差值比總和還大，較小分數一定是負數，直接判定無解。
            answers.append("impossible")
            continue

        if (total + diff) % 2 != 0:
            # 如果 S + D 是奇數，就不可能同時得到兩個整數分數。
            answers.append("impossible")
            continue

        # 這裡代表已經符合整數條件，可以直接算出兩隊分數。
        high = (total + diff) // 2
        low = (total - diff) // 2

        if low < 0:
            # 雖然前面已檢查 total >= diff，這裡保留防守式判斷。
            answers.append("impossible")
        else:
            # 較大的分數要放前面輸出，符合題目要求。
            answers.append(f"{high} {low}")

    # 多筆答案用換行接起來後一次輸出。
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()