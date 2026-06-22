import sys

def get_digital_root(x: int, base: int) -> int:
    """
    手打版本 - 任意進位的數字根：
    驗證輸入後，反覆做 base 進位轉換並加總各位數，直到數值小於 base。
    """
    if x < 0:
        raise ValueError("Input must be a non-negative integer")
    if x == 0:
        return 0
        
    current = x
    while current >= base:
        s = 0
        temp = current
        while temp > 0:
            s += temp % base
            temp //= base
        current = s
    return current

def main():
    while True:
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
            result = get_digital_root(x, 7)
            print(result)
        except ValueError as e:
            sys.stderr.write(f"Error: {e}\n")

if __name__ == '__main__':
    main()
