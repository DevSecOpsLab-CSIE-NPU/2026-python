import sys

BASE = 6  # 學號末兩碼 19，個位 9 查對照表得 base=6


def digit_sum_in_base(x: int, base: int) -> int:
    """將十進位非負整數 x 換算成 base 進位，回傳各位數字相加的十進位總和"""
    total = 0
    while x > 0:
        # x % base：取出 base 進位下最右邊那一位的數字（仍以十進位數值表示）
        # x // base：把這一位去掉，準備取下一位，相當於短除法不斷往左移
        total += x % base
        x //= base
    return total


def digital_root(x: int, base: int) -> int:
    """重複呼叫 digit_sum_in_base，直到結果在 base 進位下為一位數，回傳數字根"""
    # x < base 代表 x 在 base 進位下只剩一位數，這就是收斂的終止條件；
    # 例如 63 -> digit_sum_in_base 後變成 8，8 在六進位仍是兩位數（12），
    # 所以還要再跑一輪，直到結果小於 base 為止
    while x >= base:
        x = digit_sum_in_base(x, base)
    return x


def main() -> None:
    # 讀到 EOF 結束（跟第一題用 n=0 終止不同，這題沒有終止值）
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        print(digital_root(x, BASE))


if __name__ == "__main__":
    main()
