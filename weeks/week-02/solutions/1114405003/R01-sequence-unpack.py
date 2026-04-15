"""
R01：序列解包（Sequence Unpacking）

學習目標：
1. 了解 tuple/list 可以一次拆給多個變數。
2. 了解巢狀解包（內層 tuple 再拆解）。
3. 了解用 _ 丟棄不需要的欄位。
"""


def main():
    print("=== R01 序列解包 ===")

    # 範例 1：最基本的二元 tuple 解包。
    p = (4, 5)
    x, y = p
    print("[例1] 原資料 p =", p)
    print("[例1] x, y =", x, y)

    # 範例 2：list 也可以解包，位置一一對應。
    data = ["ACME", 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print("[例2] 原資料 data =", data)
    print("[例2] name, shares, price, date =", name, shares, price, date)

    # 範例 3：巢狀解包，把 data 裡第 4 個元素 (date tuple) 再往下拆。
    name, shares, price, (year, month, day) = data
    print("[例3] 巢狀解包後 =", name, shares, price, year, month, day)

    # 範例 4：_ 當作占位符，表示該欄位刻意忽略。
    _, shares, price, _ = data
    print("[例4] 只保留 shares, price =", shares, price)


if __name__ == "__main__":
    main()
