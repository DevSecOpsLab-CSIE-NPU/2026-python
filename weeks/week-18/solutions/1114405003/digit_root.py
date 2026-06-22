"""
第三題 任意進位的數字根
學號: 1114405003
base = 3 (個位查對照表)

規則：
- 把十進位整數轉成 base 進位
- 將各位數字相加得新數
- 重複直到剩一位數
- 以十進位輸出最終的數字根
"""


def to_base(x: int, base: int) -> list[int]:
    """
    將十進位整數轉換成 base 進位

    Args:
        x: 十進位整數
        base: 目標進位

    Returns:
        各位數字的列表 (高位在前)
    """
    if x == 0:
        return [0]

    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base

    return digits[::-1]


def sum_digits(digits: list[int], base: int) -> int:
    """
    將各位數字相加

    Args:
        digits: 各位數字列表
        base: 進位基底 (未使用，保留一致性)

    Returns:
        各位數字之和
    """
    return sum(digits)


def digit_root(x: int, base: int) -> int:
    """
    計算數字根

    Args:
        x: 十進位非負整數
        base: 進位基底

    Returns:
        數字根 (十進位)
    """
    if x == 0:
        return 0

    current = x
    while current >= base:
        digits = to_base(current, base)
        current = sum_digits(digits, base)

    return current


def main():
    """主程式：讀取多行輸入並輸出數字根"""
    BASE = 3  # 學號 1114405003, 個位 3 查對照表

    results = []

    try:
        while True:
            line = input().strip()
            if not line:
                continue
            x = int(line)
            root = digit_root(x, BASE)
            results.append(str(root))
    except EOFError:
        pass

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
