"""
UVA 10050 - Hartals
"""

from __future__ import annotations


def count_lost_days(total_days: int, hartal_parameters: list[int]) -> int:
    """計算罷工造成的工作日損失，不含週五與週六。"""
    lost_days = set()

    for hartal in hartal_parameters:
        for day in range(hartal, total_days + 1, hartal):
            if day % 7 in (6, 0):
                continue
            lost_days.add(day)

    return len(lost_days)


def solve(text: str) -> str:
    """依題目格式處理多組罷工資料。"""
    tokens = [int(token) for token in text.split()]
    if not tokens:
        return ""

    case_count = tokens[0]
    index = 1
    results: list[str] = []

    for _ in range(case_count):
        total_days = tokens[index]
        index += 1
        party_count = tokens[index]
        index += 1
        hartal_parameters = tokens[index : index + party_count]
        index += party_count
        results.append(str(count_lost_days(total_days, hartal_parameters)))

    return "\n".join(results)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
