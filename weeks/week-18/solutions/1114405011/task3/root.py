import sys

def to_base_digits(n, base):
    """將十進位整數 n 轉換為指定 base 進位下的各位數字列表"""
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return digits[::-1]

def digital_root_base(n, base):
    """計算指定進位基底下的數字根"""
    if n == 0:
        return 0
        
    # 重複拆解與加總，直到結果小於 base（也就是在該進位下變成個位數）
    current_value = n
    while current_value >= base:
        digits = to_base_digits(current_value, base)
        current_value = sum(digits)
        
    return current_value

def main():
    """
    處理標準輸入多組測資，直到 EOF。
    每行包含兩個整數：N 和 Base。
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    while True:
        try:
            n_str = next(iterator)
            base_str = next(iterator)
            
            n = int(n_str)
            base = int(base_str)
            
            # 當讀到 0 0 代表輸入結束
            if n == 0 and base == 0:
                break
                
            # 計算該進位底下的數字根
            result = digital_root_base(n, base)
            print(result)
            
        except StopIteration:
            break
        except ValueError:
            # 忽視不合規律的空白或換行殘留
            continue

if __name__ == "__main__":
    main()