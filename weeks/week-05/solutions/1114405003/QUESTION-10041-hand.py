"""
UVA 10041 - 手打版
記法：排序 -> 取中位數 -> 距離總和
"""

from __future__ import annotations


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    t = nums[0]
    i = 1
    ans = []

    for _ in range(t):
        r = nums[i]
        i += 1
        arr = nums[i:i + r]
        i += r

        arr.sort()
        m = arr[(r - 1) // 2]  # 左中位數（偶數也可達最小值）
        ans.append(str(sum(abs(x - m) for x in arr)))

    return "\n".join(ans)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
