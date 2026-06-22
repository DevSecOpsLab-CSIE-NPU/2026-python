import sys

def get_digital_root(x: int, base: int) -> int:
    """
    AI 簡單版 - 任意進位下的數字根：
    1. 驗證 x 是否為非負整數，若小於 0 拋出 ValueError。
    2. 當 x >= base 時，反覆做「各位數字相加」進行收斂，直到結果小於 base。
    """
    # 驗證輸入範圍
    if x < 0:
        raise ValueError("Input must be a non-negative integer")
        
    # 根據題目，輸入 0 的數字根直接為 0
    if x == 0:
        return 0
        
    current_val = x
    # 當數值大於或等於 base 時，代表在該進位下大於一位數，需要繼續收斂
    while current_val >= base:
        digits_sum = 0
        temp = current_val
        # 進位轉換：利用 % 取餘數，利用 // 整除降階
        while temp > 0:
            digits_sum += temp % base  # 取得在 base 進位下的最低位數字
            temp = temp // base        # 去除最低位，將數值向右位移（降階）
        current_val = digits_sum
        
    return current_val

def main():
    while True:
        # 讀取單行輸入，若達 EOF 則回傳空字串
        line = sys.stdin.readline()
        if not line:
            break
            
        line = line.strip()
        if not line:
            continue
            
        try:
            x = int(line)
        except ValueError:
            sys.stderr.write("Invalid input format\n")
            continue
            
        try:
            # 依學號計算出的進位基底 base = 7 進行計算
            result = get_digital_root(x, 7)
            print(result)
        except ValueError as e:
            sys.stderr.write(f"Error: {e}\n")

if __name__ == '__main__':
    main()
