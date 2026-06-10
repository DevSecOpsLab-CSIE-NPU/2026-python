def digit_root(n: int) -> int:
    """計算正整數 n 的數字根。
    反覆把 n 的各位數字相加，直到結果只剩一位數。
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    
    while n >= 10:
        n = sum(int(char) for char in str(n))
        
    return n
