# -*- coding: utf-8 -*-

def digit_root(n: int) -> int:
    """
    計算數字根 (Digit Root)。
    反覆把 n 的各位數字相加，直到結果只剩一位數為止。
    
    參數:
        n (int): 正整數 (1 <= n <= 2,000,000,000)
        
    回傳:
        int: 數字根 (1-9 之間的整數)
        
    例外:
        ValueError: 當 n < 1 時拋出
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    
    current = n
    while current >= 10:
        # 計算各位數之和
        temp_sum = 0
        for digit in str(current):
            temp_sum += int(digit)
        current = temp_sum
        
    return current

if __name__ == "__main__":
    # 簡單手動測試
    test_cases = [24, 199, 9999, 5]
    for tc in test_cases:
        print(f"n={tc:4} -> digit_root={digit_root(tc)}")

