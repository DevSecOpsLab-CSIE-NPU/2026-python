from __future__ import annotations

import sys


def count_lost_workdays(total_days: int, hartal_parameters: list[int]) -> int:
    # 以集合記錄罷工日，避免不同政黨撞到同一天時重複計算。
    lost_days: set[int] = set()

    for interval in hartal_parameters:
        for day in range(interval, total_days + 1, interval):
            # 題目規定星期五與星期六不算工作天。
            if day % 7 in (6, 0):
                continue
            lost_days.add(day)

    return len(lost_days)


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    test_case_count = int(tokens[0])
    index = 1
    answers: list[str] = []

    for _ in range(test_case_count):
        total_days = int(tokens[index])
        index += 1
        party_count = int(tokens[index])
        index += 1

        hartal_parameters = [int(tokens[index + offset]) for offset in range(party_count)]
        index += party_count
        answers.append(str(count_lost_workdays(total_days, hartal_parameters)))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()