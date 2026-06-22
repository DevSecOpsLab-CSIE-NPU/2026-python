def digit_root(n, base=16):
    """
    實作任意進位的數字根邏輯
    1. 將數字轉成 base 進位並將各位數字相加
    2. 重複直到結果小於 base
    """
    if n == 0:
        return 0
    
    current = n
    while current >= base:
        sum_digits = 0
        temp = current
        while temp > 0:
            sum_digits += temp % base
            temp //= base
        current = sum_digits
        
    return current
