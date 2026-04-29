"""
Collatz 序列（3n+1）cycle-length 計算 - 簡化版
"""


def cycle_len(n):
    """
    計算 n 的 Collatz 序列長度

    Collatz 序列規則：
    - 如果 n 是偶數，則 n = n / 2
    - 如果 n 是奇數，則 n = 3 * n + 1
    - 重複直到 n 變成 1

    參數：
        n: 起始數字
    回傳：
        序列的長度（含起始數字和 1）
    """
    # 計數器初始化為 1（因為序列從 n 本身開始）
    count = 1

    # 當 n 不等於 1 時，持續執行
    while n != 1:
        if n % 2 == 0:
            # n 為偶數，除以 2
            n = n // 2
        else:
            # n 為奇數，套用 3n+1 公式
            n = 3 * n + 1
        # 每執行一步，計數器加 1
        count += 1

    return count


def main():
    """主程式：處理輸入、計算並輸出結果"""
    import sys

    # 支援兩種輸入方式：
    # 1. 命令列引數指定檔案：python week03_100-easy.py input.txt
    # 2. 標準輸入（stdin）
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin

    # 逐一處理每一行輸入
    for line in lines:
        # 去除行尾空白
        line = line.strip()
        # 跳過空行
        if not line:
            continue

        # 將一行字串轉換為兩個整數
        # 例如："1 10" → i=1, j=10
        i, j = map(int, line.split())

        # 確保區間正確（不管輸入順序）
        # start 為較小值，end 為較大值
        start, end = min(i, j), max(i, j)

        # 使用生成式找出區間內所有數字的 cycle-length，取最大值
        # range(start, end + 1) 包含 start 和 end
        max_len = max(cycle_len(n) for n in range(start, end + 1))

        # 輸出格式：原始輸入的 i、j，以及區間內的最大 cycle-length
        # 例如：1 10 20
        print(i, j, max_len)


# 當直接執行此檔案時才執行 main()
# 如果被 import 則不執行
if __name__ == "__main__":
    main()
