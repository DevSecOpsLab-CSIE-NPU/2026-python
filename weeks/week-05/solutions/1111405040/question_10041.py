"""
UVA 10041 - Vito's Family
"""

from __future__ import annotations


def min_total_distance(addresses: list[int]) -> int:
    """回傳讓總距離最小的距離和。"""
    sorted_addresses = sorted(addresses)
    median = sorted_addresses[len(sorted_addresses) // 2]
    return sum(abs(address - median) for address in sorted_addresses)


def solve(text: str) -> str:
    """依題目格式處理多筆測資。"""
    tokens = [int(token) for token in text.split()]
    if not tokens:
        return ""

    case_count = tokens[0]
    index = 1
    results: list[str] = []

    for _ in range(case_count):
        relative_count = tokens[index]
        index += 1
        addresses = tokens[index : index + relative_count]
        index += relative_count
        results.append(str(min_total_distance(addresses)))

    return "\n".join(results)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
