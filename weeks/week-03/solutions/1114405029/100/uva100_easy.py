import sys

# 計算某個數字的 3n+1 cycle 長度
def cycle_length(n):

    count = 1

    # 持續計算直到變成 1
    while n != 1:

        # 如果是奇數
        if n % 2 == 1:
            n = 3 * n + 1

        # 如果是偶數
        else:
            n = n // 2

        count += 1

    return count


# 一行一行讀取輸入
for line in sys.stdin:

    # 讀取兩個數字
    i, j = map(int, line.split())

    # 確保從小到大計算
    start = min(i, j)
    end = max(i, j)

    max_cycle = 0

    # 計算區間內最大的 cycle length
    for n in range(start, end + 1):

        c = cycle_length(n)

        if c > max_cycle:
            max_cycle = c

    # 按題目要求輸出原本的 i j 與最大 cycle
    print(i, j, max_cycle)