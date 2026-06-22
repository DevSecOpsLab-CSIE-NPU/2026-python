import sys


def to_base(n: int, base: int) -> list[int]:
    """將十進位非負整數 n 轉換為 base 進位的位數列表（低位在前）"""
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return digits


def digit_root_base(n: int, base: int) -> int:
    """
    計算 n 在 base 進位下的數字根。
    重複將各位數字相加（在 base 進位下），直到結果為個位數（< base）。
    回傳十進位整數。
    """
    while n >= base:
        digits = to_base(n, base)
        n = sum(digits)
    return n


def solve() -> None:
    BASE = 6  # 學號 1114405006 個位數 = 6
    out_lines = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        out_lines.append(str(digit_root_base(x, BASE)))
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()