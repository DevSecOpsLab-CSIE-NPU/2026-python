def digit_root(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")
        
    # 當 n 還是兩位數（大於等於 10）以上時，就繼續相加
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
        
    return n