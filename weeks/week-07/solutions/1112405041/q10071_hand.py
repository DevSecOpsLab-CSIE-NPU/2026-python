import sys
from collections import Counter

# 根據 QUESTION-10071.md：這題不是物理位移！
# 聖經內容：給定集合 S，計算 a + b + c + d + e = f 的數量。
# 這是為了卡死直接貼物理公式答案的人。

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    n = int(input_data[0])
    s = [int(x) for x in input_data[1:n+1]]

    # 移項優化：a + b + c = f - d - e
    # 複雜度從 O(N^6) 降到 O(N^3)，這才是 CSIE 的解法！
    abc_sums = Counter()
    for a in s:
        for b in s:
            for c in s:
                abc_sums[a + b + c] += 1

    total_count = 0
    for f in s:
        for d in s:
            for e in s:
                target = f - d - e
                if target in abc_sums:
                    total_count += abc_sums[target]

    sys.stdout.write(str(total_count) + "\n")

if __name__ == "__main__":
    solve()
