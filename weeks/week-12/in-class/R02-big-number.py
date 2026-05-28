# R02. 大數處理（字串讀入超長整數）
# Python 原生支援大整數，但競程常需要字串逐位處理

# ── Python 的 int 本身即大數 ─────────────────────────────
print("=== Python 原生大整數 ===")
n = 2 ** 100
print(n)
print(type(n))

# 讀入超大數：直接用 int() 轉換
big = int("99999999999999999999999999999999")
print(big % 9)      # 0（位數和 = 9*32，是 9 的倍數）

# ── 逐位字串處理（不轉 int，避免速度問題）────────────────
print("\n=== 字串逐位處理 ===")

def digit_sum_str(s: str) -> int:
    """字串形式的數字，計算各位數字和"""
    return sum(int(c) for c in s)

print(digit_sum_str("999999999999999999999"))  # 189

# ── 11 的倍數判斷（UVA 10929）────────────────────────────
# 判斷技巧：奇數位數字和 - 偶數位數字和，差為 11 的倍數
# 從右邊數起：index 0（最右）為奇數位

def is_multiple_of_11(s: str) -> bool:
    """
    s 為數字字串，可達 1000 位
    奇偶交替加減：從右到左，奇數位加、偶數位減
    """
    total = 0
    for i, d in enumerate(reversed(s)):
        if i % 2 == 0:
            total += int(d)
        else:
            total -= int(d)
    return total % 11 == 0

print("\n=== 11 的倍數 ===")
print(is_multiple_of_11("11"))          # True
print(is_multiple_of_11("22"))          # True
print(is_multiple_of_11("12"))          # False
print(is_multiple_of_11("10"))          # False
print(is_multiple_of_11("121"))         # True（1-2+1=0）
print(is_multiple_of_11("1234567890"))  # False

# ── 輸入格式：每行一個大數，0 結束 ───────────────────────
sample = """\
11
22
12
0
"""

print("\n=== 模擬輸入輸出 ===")
import io, sys
for line in io.StringIO(sample):
    n = line.strip()
    if n == "0":
        break
    if is_multiple_of_11(n):
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")
