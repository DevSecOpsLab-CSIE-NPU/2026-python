"""
R11：命名切片 slice

學習目標：
1. 了解 slice(start, stop) 可以把索引範圍命名。
2. 透過命名常數提高維護性（避免魔法數字）。
"""


def main():
    print("=== R11 命名切片 ===")

    record = "....................100 .......513.25 .........."
    print("[原始字串]", record)

    SHARES = slice(20, 23)
    PRICE = slice(31, 37)

    shares = int(record[SHARES])
    price = float(record[PRICE])
    cost = shares * price

    print("[例1] SHARES 範圍 =", SHARES, "->", record[SHARES])
    print("[例2] PRICE 範圍 =", PRICE, "->", record[PRICE])
    print("[例3] shares =", shares)
    print("[例4] price =", price)
    print("[例5] cost = shares * price =", cost)


if __name__ == "__main__":
    main()
