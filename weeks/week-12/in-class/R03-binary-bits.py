# R03. 二進位與位元運算
# bin() / format() / int(x, 2) / bit_count() / 位元運算子

# ── 進位轉換 ─────────────────────────────────────────────
print("=== 進位轉換 ===")
n = 21

print(bin(n))               # '0b10101'
print(bin(n)[2:])           # '10101'  去掉 '0b' 前綴
print(format(n, 'b'))       # '10101'
print(f"{n:b}")             # '10101'
print(f"{n:08b}")           # '00010101'  補零到 8 位

# 二進位字串 → 整數
print(int("10101", 2))      # 21
print(int("0b10101", 2))    # 21  也可以帶前綴

# ── 計算 1 的個數（Parity，UVA 10931）────────────────────
print("\n=== 計算二進位中 1 的個數 ===")

def parity(n: int) -> int:
    """計算 n 的二進位表示中 1 的個數"""
    return bin(n).count('1')

# Python 3.10+ 有內建方法
# print(n.bit_count())

for i in [1, 2, 10, 21]:
    b = format(i, 'b')
    p = parity(i)
    print(f"The parity of {b} is {p} (mod 2).")

# ── 位元運算子 ────────────────────────────────────────────
print("\n=== 位元運算 ===")
a, b = 0b1010, 0b1100

print(f"a     = {a:04b} ({a})")
print(f"b     = {b:04b} ({b})")
print(f"a & b = {a & b:04b}   AND：兩者都是 1 才是 1")
print(f"a | b = {a | b:04b}   OR ：任一為 1 就是 1")
print(f"a ^ b = {a ^ b:04b}   XOR：相同為 0，不同為 1")
print(f"~a    = {~a}          NOT：取反（有符號）")
print(f"a<<1  = {a<<1:04b}   左移：乘 2")
print(f"a>>1  = {a>>1:04b}   右移：除 2")

# ── 應用：奇偶性判斷 ─────────────────────────────────────
print("\n=== 奇偶性 ===")
for i in range(8):
    odd_even = "奇數" if i & 1 else "偶數"
    print(f"{i}: {odd_even}")
