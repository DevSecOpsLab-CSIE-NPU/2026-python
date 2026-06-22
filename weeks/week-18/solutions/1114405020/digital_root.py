import sys


def find_digital_root(x: int, base: int = 2) -> int:
    """計算任意進位下的數字根：
    1. 將非負整數 x 轉換為 base 進位，加總其各位數
    2. 反覆此步驟直到結果在 base 進位下為一位數（即小於 base）
    3. 以十進位回傳最終數字根
    若 x < 0 或 base < 2，拋出 ValueError。
    """
    if x < 0:
        raise ValueError("x must be a non-negative integer")
    if base < 2:
        raise ValueError("base must be >= 2")

    if x == 0:
        return 0

    # 反覆加總各位數直到結果小於 base
    while x >= base:
        # 將 x 轉換為 base 進位的各位數加總
        temp_sum = 0
        temp_x = x
        while temp_x > 0:
            temp_sum += temp_x % base
            temp_x //= base
        x = temp_sum

    return x


if __name__ == "__main__":
    # 處理多行輸入至 EOF
    for line in sys.stdin:
        val_str = line.strip()
        if not val_str:
            continue
        try:
            val = int(val_str)
            # 學號末碼為 0，進位基底 base = 2
            print(find_digital_root(val, 2))
        except ValueError:
            pass
