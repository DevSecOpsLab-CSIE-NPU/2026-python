# R01. 整除性規則（數字位數和）
# 對應題目：UVA 10922（2 the 9s）、UVA 10929（11 的倍數）

# ── 為什麼要用「位數和」判斷整除？ ───────────────────────
# 對超大數（1000 位），直接做 int(s) % 9 在 Python 沒問題，
# 但在 C/Java 會溢位。位數和是一種不依賴整數大小的通用技巧。

# ── 9 的倍數判斷（UVA 10922）─────────────────────────────
# 規則：各位數字之和若為 9 的倍數，原數也是 9 的倍數。
# 可以反覆加總直到變成個位數 → 若最終是 9，原數即為 9 的倍數。

def digit_sum(s: str) -> int:
    """計算數字字串各位數字之和"""
    return sum(int(c) for c in s)

print("=== 9 的倍數：位數和規則 ===")
for n in ["9", "18", "99", "999", "100", "12345"]:
    s = digit_sum(n)
    print(f"{n:>8s} → 位數和 = {s}，{'是' if s % 9 == 0 else '不是'} 9 的倍數")


def nine_degree(s: str) -> tuple[bool, int]:
    """
    回傳 (是否為 9 的倍數, 9-degree)
    9-degree：依 UVA 10922 定義，若數字本身就是 9，degree 為 1；
    否則反覆做位數和，直到得到個位數 9 為止，並計算層數。
    """
    current = s
    if current == "9":
        return True, 1

    degree = 0
    while len(current) > 1:
        current = str(digit_sum(current))
        degree += 1
        if current == "9":
            return True, degree + 1

    return False, -1

print("\n=== UVA 10922 輸出格式 ===")
for n in ["9", "18", "999", "100", "729"]:
    ok, deg = nine_degree(n)
    if ok:
        print(f"9-degree of {n} is {deg}.")
    else:
        print(f"{n} is not a multiple of 9.")


# ── 11 的倍數判斷（UVA 10929）────────────────────────────
# 規則：從右到左，奇數位（index 0,2,4…）加、偶數位（index 1,3,5…）減，
#       差值為 11 的倍數 → 原數是 11 的倍數。
# 例：121 → 1 - 2 + 1 = 0，0 % 11 == 0 ✓

def is_multiple_of_11(s: str) -> bool:
    """s 為數字字串，可達 1000 位"""
    total = 0
    for i, d in enumerate(reversed(s)):
        total += int(d) if i % 2 == 0 else -int(d)
    return total % 11 == 0

print("\n=== 11 的倍數：奇偶位交替加減 ===")
for n in ["11", "22", "121", "1331", "12", "100"]:
    print(f"{n:>6s} → {'是' if is_multiple_of_11(n) else '不是'} 11 的倍數")

print("\n=== UVA 10929 輸出格式 ===")
for n in ["11", "22", "12"]:
    if is_multiple_of_11(n):
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")


# ── 附：math.gcd（供其他題目參考）───────────────────────
import math
print(f"\n=== math.gcd（工具函式）===")
print(f"gcd(12, 8)   = {math.gcd(12, 8)}")
print(f"gcd(100, 75) = {math.gcd(100, 75)}")
print(f"lcm(4, 6)    = {math.lcm(4, 6)}")   # Python 3.9+
