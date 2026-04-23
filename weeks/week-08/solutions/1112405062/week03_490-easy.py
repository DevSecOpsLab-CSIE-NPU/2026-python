"""
UVA 490 - Rotating Sentences
將數列文字順時針旋轉 90 度輸出
"""


def solve():
    """主程式：讀取多行文字、順時針旋轉 90 度輸出"""
    import sys

    # 支援兩種輸入方式：
    # 1. 命令列引數：python week03_490-easy.py input.txt
    # 2. 標準輸入（stdin）
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = [line.rstrip("\n") for line in f]
    else:
        lines = [line.rstrip("\n") for line in sys.stdin]

    # 找出最長行的長度（作為旋轉後的列數）
    max_len = max(len(l) for l in lines)

    # 逐一處理每一列（旋轉後的每一行）
    # 旋轉後的 column 數量 = 原始最大行長度
    for col in range(max_len):
        # 用生成式組成一行：
        # 從上到下讀取同一 column 的字元
        # 若該行長度不足 col，則填空白
        row_str = "".join(
            line[col] if col < len(line) else " "  # 三元運算子
            for line in lines  # 遍歷每一行
        )
        print(row_str)


if __name__ == "__main__":
    solve()
