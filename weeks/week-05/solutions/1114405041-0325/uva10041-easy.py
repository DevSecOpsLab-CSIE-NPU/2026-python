"""UVA 10041 - Vito's Family（-easy 版本）。

這份版本刻意使用「容易記憶」的直覺做法：
1. 把每位親戚的門牌都當作候選住址。
2. 逐一計算該候選住址到所有親戚的距離總和。
3. 取最小值。

雖然時間複雜度是 O(r^2)，但對題目上限仍可接受，且概念很直觀。
"""

from __future__ import annotations


def minimum_total_distance_easy(addresses: list[int]) -> int:
    """用直覺枚舉法計算最小總距離。"""
    if not addresses:
        return 0

    best = float("inf")

    # 只要枚舉在既有親戚門牌上即可找到最佳答案。
    for candidate in addresses:
        total = 0
        for addr in addresses:
            total += abs(addr - candidate)

        if total < best:
            best = total

    return int(best)


def solve_io(data: str) -> str:
    """依 UVA 輸入格式解析並輸出答案。"""
    tokens = data.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    idx = 1
    outputs: list[str] = []

    for _ in range(t):
        r = int(tokens[idx])
        idx += 1
        addresses = [int(tokens[idx + i]) for i in range(r)]
        idx += r

        outputs.append(str(minimum_total_distance_easy(addresses)))

    return "\n".join(outputs)


def main() -> None:
    import sys

    input_data = sys.stdin.read()
    result = solve_io(input_data)
    if result:
        print(result)


if __name__ == "__main__":
    main()
