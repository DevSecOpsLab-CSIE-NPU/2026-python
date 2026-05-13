import sys


def main() -> None:
    # 題目的第一行是測資筆數 n。
    # 先讀第一行，方便後面用迴圈逐筆處理資料。
    line = sys.stdin.readline().strip()
    if not line:
        return

    count = int(line)
    output = []

    # 接下來的每一行，都會提供一組 S 和 D。
    # 我們依照題目要求，把每組答案算出來後存起來，最後一次輸出。
    for _ in range(count):
        total, diff = map(int, sys.stdin.readline().split())

        # 先判斷無解情況，這樣可以少做一次公式計算：
        # 1. 如果 D 大於 S，則 (S - D) 會是負數，代表較小分數不合法。
        # 2. 如果 S + D 是奇數，就無法平均分成兩個整數。
        if diff > total or (total + diff) % 2 == 1:
            output.append("impossible")
            continue

        # 公式很好記：
        # 較大的分數 = (S + D) // 2
        # 較小的分數 = (S - D) // 2
        # 這裡用整數除法 //，因為前面已經確認一定是整數解。
        big = (total + diff) // 2
        small = (total - diff) // 2

        # 題目規定較大的分數要寫前面。
        output.append(f"{big} {small}")

    # 所有答案用換行串起來，再一次輸出。
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()