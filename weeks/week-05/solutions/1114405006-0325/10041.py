"""
UVA 10041 - Vito's Family

解題重點：
所有親戚門牌到某一點的絕對距離總和，要最小時可選在中位數位置。

原因簡述：
若把房子位置從左到右移動，左側親戚距離會增加、右側親戚距離會減少。
當左右人數最平衡時（也就是中位數附近），總距離最小。
"""

from __future__ import annotations

import sys


def min_total_distance(addresses: list[int]) -> int:
    """回傳所有地址到最佳位置的最小總距離。"""
    # 先排序，才能直接用索引取中位數。
    addresses.sort()

    # 對奇數個元素，中位數唯一；對偶數個元素，取中間兩者任一都可得到相同最小值。
    median = addresses[len(addresses) // 2]

    # 依題意，距離為絕對值差 |s_i - s_j|。
    return sum(abs(x - median) for x in addresses)


def solve(data: str) -> str:
    # 將整份輸入一次拆成整數序列，方便用指標逐段讀取。
    numbers = list(map(int, data.split()))
    if not numbers:
        return ""

    t = numbers[0]
    idx = 1
    results: list[str] = []

    for _ in range(t):
        # 每組測資第一個數字 r 代表親戚數。
        r = numbers[idx]
        idx += 1

        # 接著讀取 r 個門牌位置。
        addresses = numbers[idx : idx + r]
        idx += r
        results.append(str(min_total_distance(addresses)))

    return "\n".join(results)


def main() -> None:
    input_data = sys.stdin.read()
    output = solve(input_data)
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
