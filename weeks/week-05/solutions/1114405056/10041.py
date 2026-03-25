from __future__ import annotations

import sys


def minimum_total_distance(addresses: list[int]) -> int:
    # 將地址排序後，取中位數位置當作新家，能讓總距離最小。
    sorted_addresses = sorted(addresses)
    meeting_point = sorted_addresses[len(sorted_addresses) // 2]
    return sum(abs(address - meeting_point) for address in sorted_addresses)


def solve(data: str) -> str:
    # 依序讀取每一組測資，計算最小總距離。
    tokens = data.split()
    if not tokens:
        return ""

    test_case_count = int(tokens[0])
    index = 1
    answers: list[str] = []

    for _ in range(test_case_count):
        relative_count = int(tokens[index])
        index += 1
        addresses = [int(tokens[index + offset]) for offset in range(relative_count)]
        index += relative_count
        answers.append(str(minimum_total_distance(addresses)))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()