# UVA 10929 — 判斷 11 的倍數 (easy)
import sys
for line in sys.stdin:
    num = line.strip()
    if num == '0':
        break
    odd_sum = sum(int(num[i]) for i in range(len(num)-1, -1, -2))  # 奇數位總和 (從右)
    even_sum = sum(int(num[i]) for i in range(len(num)-2, -1, -2))  # 偶數位總和
    diff = abs(odd_sum - even_sum)
    if diff % 11 == 0:
        print(f"{num} is a multiple of 11.")
    else:
        print(f"{num} is not a multiple of 11.")