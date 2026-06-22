import sys


def find_digital_root(x: int, base: int = 2) -> int:
    """【AI 教學版】任意進位數字根

    含詳細繁體中文註解，詳細說明任意進位轉換及累加邏輯。
    """
    # 驗證輸入參數之合法性，防止系統錯誤
    if x < 0:
        raise ValueError("輸入的數 x 必須是非負整數")
    if base < 2:
        raise ValueError("進位基底 base 必須大於或等於 2")

    # 0 在任何進位下的數字根皆為 0
    if x == 0:
        return 0

    # 重複進行各位數相加，直到 x 的值小於基底 base（即在該進位下已為個位數）
    while x >= base:
        temp_sum = 0
        temp_x = x
        # 進行經典的進位拆解：除以 base 取餘數得到當前最低位數，再整除 base 往高位移動
        while temp_x > 0:
            temp_sum += temp_x % base
            temp_x //= base
        x = temp_sum

    return x


if __name__ == "__main__":
    # 讀取標準輸入，直到 EOF 為止
    for line in sys.stdin:
        val_str = line.strip()
        if not val_str:
            continue
        try:
            val = int(val_str)
            # 依學號（末兩碼 20，個位數 0）對照：base = 2
            result = find_digital_root(val, 2)
            print(result)
        except ValueError:
            pass
