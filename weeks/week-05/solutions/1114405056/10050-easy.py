from __future__ import annotations

import sys


def count_lost_workdays(total_days: int, hartal_parameters: list[int]) -> int:
    # 用一個集合來存「真的有損失到的工作天」。
    # 集合的好處是同一天就算被多個政黨同時罷工，也只會算一次。
    lost_days: set[int] = set()

    for interval in hartal_parameters:
        # 每隔 interval 天，就會發生一次該政黨的罷工。
        for day in range(interval, total_days + 1, interval):
            # 題目說第 1 天是星期日，因此：
            # day % 7 == 6 代表星期五，day % 7 == 0 代表星期六。
            # 這兩天是假日，不列入損失工作天。
            if day % 7 == 6 or day % 7 == 0:
                continue

            lost_days.add(day)

    return len(lost_days)


def solve(data: str) -> str:
    parts = data.split()
    if not parts:
        return ""

    case_count = int(parts[0])
    index = 1
    outputs: list[str] = []

    for _ in range(case_count):
        total_days = int(parts[index])
        index += 1

        party_count = int(parts[index])
        index += 1

        hartal_parameters: list[int] = []
        for _ in range(party_count):
            hartal_parameters.append(int(parts[index]))
            index += 1

        outputs.append(str(count_lost_workdays(total_days, hartal_parameters)))

    return "\n".join(outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()