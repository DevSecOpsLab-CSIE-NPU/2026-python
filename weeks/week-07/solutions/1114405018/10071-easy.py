import sys
from collections import defaultdict


def count_tuples(nums):
    """計算滿足 a+b+c+d+e=f 的六元組總數。

    easy 記法：
    1) 先算所有 a+b 的和（兩數和）。
    2) 再算所有 c+d+e 的和（三數和）。
    3) 對每個 f，找 two_sum + three_sum = f 的配對數量。

    注意：
    - 題目中的 a,b,c,d,e,f 都可以重複使用集合 S 內元素。
    - 本題計數的是「有序」選取，因此 (x, y) 與 (y, x) 算不同。
    """

    # 轉成 list 以便後續重複迭代。
    values = list(nums)
    if not values:
        return 0

    # two_sum[s]：有多少組有序 (a, b) 使得 a+b=s
    two_sum = defaultdict(int)
    for a in values:
        for b in values:
            two_sum[a + b] += 1

    # three_sum[s]：有多少組有序 (c, d, e) 使得 c+d+e=s
    three_sum = defaultdict(int)
    for c in values:
        for d in values:
            for e in values:
                three_sum[c + d + e] += 1

    # 目標條件：a+b+c+d+e=f
    # 改寫成：(a+b) + (c+d+e) = f
    # 若 two_sum 裡某個和是 s2，則需要 three_sum 裡有 (f-s2)。
    # 對應組合數要相乘再累加。
    answer = 0
    for f in values:
        for s2, cnt2 in two_sum.items():
            answer += cnt2 * three_sum.get(f - s2, 0)

    return answer


def solve(data):
    """測試友善介面：可接 list 或整段輸入文字。"""

    # 若傳入的是整段輸入文字，依題目格式解析：
    # 第一個數字是 n，後面 n 個是集合 S。
    if isinstance(data, str):
        nums = [int(x) for x in data.split()]
        if not nums:
            return "0"
        n = nums[0]
        values = nums[1:1 + n]
        return str(count_tuples(values))

    # 若傳入的是可迭代物件（如 list），直接計算。
    return count_tuples(data)


def main():
    """競賽模式入口：從標準輸入讀取，輸出答案。"""

    # 一次讀完全部輸入，split 後轉為整數。
    nums = [int(x) for x in sys.stdin.read().split()]
    if not nums:
        return

    # 依題目格式取出集合元素。
    n = nums[0]
    values = nums[1:1 + n]

    # 輸出符合條件的六元組數量。
    print(count_tuples(values))


if __name__ == "__main__":
    main()
