"""
UVA 272 - TeX Quotes
將普通雙引號轉換為 TeX 風格的引號
"""


def solve():
    """主程式：讀取輸入、替換引號、輸出結果"""
    import sys

    # 支援兩種輸入方式：
    # 1. 命令列引數：python week03_272-easy.py input.txt
    # 2. 標準輸入（stdin）
    if len(sys.argv) > 1:
        input_stream = open(sys.argv[1], "r")
    else:
        input_stream = sys.stdin

    # 兩個引號替換列表
    # quotes[0] = ``（左雙引號，用於第 1, 3, 5... 個引號）
    # quotes[1] = ''（右雙引號，用於第 2, 4, 6... 個引號）
    quotes = ["``", "''"]

    # 目前的引號索引，交替在 0 和 1 之間切換
    i = 0

    # 逐一讀取每一行
    for line in input_stream:
        # 逐一處理每一個字元
        for char in line:
            if char == '"':
                # 遇到雙引號，根據目前的索引輸出對應的替換
                print(quotes[i], end="")
                # 切換到另一個引號：0 → 1 或 1 → 0
                i = 1 - i
            else:
                # 非雙引號，直接輸出
                print(char, end="")


if __name__ == "__main__":
    solve()
