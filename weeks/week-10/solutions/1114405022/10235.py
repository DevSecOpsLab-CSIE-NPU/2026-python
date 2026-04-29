"""UVA 10235 - Simply Emirp

一般版：更完善的質數判斷和 Emirp 檢測
"""

import sys


def is_prime(n: int) -> bool:
    """
    判斷 n 是否為質數
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 檢查奇數因數
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


def is_emirp(n: int) -> bool:
    """
    檢查是否為 Emirp：
    1. 本身是質數
    2. 反向後也是質數
    3. 反向後與原數不同（非回文質數）
    """
    # 本身必須是質數
    if not is_prime(n):
        return False
    
    # 計算反向數
    reversed_n = int(str(n)[::-1])
    
    # 非回文
    if n == reversed_n:
        return False
    
    # 反向數也是質數
    return is_prime(reversed_n)


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        n = int(line)
        result = "emirp" if is_emirp(n) else "not emirp"
        print(f"{n} {result}")


if __name__ == "__main__":
    main()
