# UVA 11461 - Square Numbers
#
# 這是比較簡單、好記的寫法。
#
# 題目要求：
# 給一個區間 [a, b]，計算裡面有幾個完全平方數。
#
# 完全平方數例子：
# 1 = 1 * 1
# 4 = 2 * 2
# 9 = 3 * 3
# 16 = 4 * 4
#
# 重要公式：
# 小於等於 b 的完全平方數數量是 floor(sqrt(b))。
# 小於 a 的完全平方數數量是 floor(sqrt(a - 1))。
# 所以 [a, b] 之間的答案是：
# floor(sqrt(b)) - floor(sqrt(a - 1))

from math import isqrt


while True:
    a, b = map(int, input().split())

    # 題目規定 0 0 代表結束。
    if a == 0 and b == 0:
        break

    # isqrt(x) 會回傳 floor(sqrt(x))，而且是整數運算，不會有小數誤差。
    answer = isqrt(b) - isqrt(a - 1)
    print(answer)
