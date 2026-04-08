import sys
from collections import Counter


def solve(data: str) -> str:
    # 讀取集合 S。
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    n = nums[0]
    s = nums[1:1 + n]

    pair = Counter()
    # pair[x] = a+b==x 的有序對數量。
    for a in s:
        for b in s:
            pair[a + b] += 1

    # quad[y] = a+b+c+d==y 的有序四元組數量。
    quad = Counter()
    pair_items = list(pair.items())
    for x_sum, x_cnt in pair_items:
        for y_sum, y_cnt in pair_items:
            quad[x_sum + y_sum] += x_cnt * y_cnt

    # a+b+c+d+e=f 轉成 a+b+c+d=f-e，逐一累加即可。
    total = 0
    for e in s:
        for f in s:
            total += quad[f - e]

    return str(total)


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    if out:
        print(out)


if __name__ == "__main__":
    main()
