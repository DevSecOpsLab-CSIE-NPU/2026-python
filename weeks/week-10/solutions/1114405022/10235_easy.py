"""UVA 10235 - Simply Emirp

簡單版（-easy）：
1. 判斷是否為質數（Emirp = Prime 反向後也是質數）
2. 檢查反向字符串是否相同
3. 回傳結果

這個版本的重點是快速實現質數判斷和回文檢查。
"""

def is_emirp(n: int) -> bool:
    """
    檢查一個數是否為 Emirp
    Emirp = 質數且反向後也是質數且不是回文
    """
    # 先檢查是否為質數
    if n < 2:
        return False
    if n == 2:
        return False  # 2 反向還是 2，是回文，不是 emirp
    
    # 簡單質數判斷
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    # 反向數
    reversed_n = int(str(n)[::-1])
    
    # 如果反向後相同，則是回文，不是 emirp
    if n == reversed_n:
        return False
    
    # 檢查反向數是否為質數
    if reversed_n < 2:
        return False
    for i in range(2, int(reversed_n ** 0.5) + 1):
        if reversed_n % i == 0:
            return False
    
    return True


def main() -> None:
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        result = "emirp" if is_emirp(n) else "not emirp"
        print(f"{n} {result}")


if __name__ == "__main__":
    main()
