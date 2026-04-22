# UVA 10235 - Simply Emirp
# 詳細註解版（繁體中文）

import sys


def is_prime(n: int) -> bool:
    # 小於 2 不是質數
    if n < 2:
        return False
    # 2 是唯一偶質數
    if n == 2:
        return True
    # 其他偶數都不是質數
    if n % 2 == 0:
        return False

    # 只需試除到 sqrt(n)
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def solve() -> None:
    out = []

    # 每一行是一個整數 n，直到 EOF
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        n = int(line)

        # 先判斷 n 是否是質數
        if not is_prime(n):
            out.append(f"{n} is not prime.")
            continue

        # 反轉數字後再判斷是否質數
        rev = int(str(n)[::-1])

        # emirp 需滿足：n 是質數、rev 是質數、且 rev != n
        if rev != n and is_prime(rev):
            out.append(f"{n} is emirp.")
        else:
            out.append(f"{n} is prime.")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
