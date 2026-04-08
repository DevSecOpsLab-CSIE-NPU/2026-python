"""10071 easy-hand：手打版。"""

import sys
from collections import defaultdict


def solve(values):
    # cnt2[s]：兩數和為 s 的有序對數量。
    cnt2 = defaultdict(int)
    for x in values:
        for y in values:
            cnt2[x + y] += 1

    # cnt3[s]：三數和為 s 的有序三元組數量。
    cnt3 = defaultdict(int)
    for a in values:
        for b in values:
            for c in values:
                cnt3[a + b + c] += 1

    # 固定 f，累加 cnt3[s3] * cnt2[f-s3]。
    ans = 0
    for f in values:
        for s3, c3 in cnt3.items():
            ans += c3 * cnt2.get(f - s3, 0)

    return ans


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    values = data[1 : 1 + n]
    print(solve(values))


if __name__ == "__main__":
    main()
