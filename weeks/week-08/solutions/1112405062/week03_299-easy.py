"""
UVA 299 - Train Swapping
計算將火車車廂排序所需的最少相鄰交換次數
"""


def solve():
    """主程式：讀取測資、計算逆序對、輸出結果"""
    import sys

    # 支援兩種輸入方式：
    # 1. 命令列引數：python week03_299-easy.py input.txt
    # 2. 標準輸入（stdin）
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = [line.strip() for line in f]
    else:
        lines = [line.strip() for line in sys.stdin]

    # 第一行是測資數量
    t = int(lines[0])
    idx = 1  # 目前讀到第幾行

    # 處理每一組測資
    for _ in range(t):
        # 讀取車廂數量
        n = int(lines[idx])
        idx += 1

        # 讀取車廂順序
        train = list(map(int, lines[idx].split()))
        idx += 1

        # 計算逆序對數量
        # 逆序對 = 前面元素比後面元素大的情況
        # 例如：[4, 3, 2, 1] 有 6 個逆序對：(4,3),(4,2),(4,1),(3,2),(3,1),(2,1)
        # 這也是將陣列排序所需的最小相鄰交換次數
        swaps = sum(
            1  # 符合條件就加 1
            for i, a in enumerate(train)  # i 是索引，a 是目前元素
            for b in train[i + 1 :]  # b 是 a 後面的所有元素
            if a > b  # 如果 a > b，代表逆序
        )

        # 輸出結果
        print(f"Optimal train swapping takes {swaps} swaps.")


if __name__ == "__main__":
    solve()
