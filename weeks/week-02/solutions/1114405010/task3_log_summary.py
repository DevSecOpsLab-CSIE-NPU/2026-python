"""Task 3: user and action summary from logs."""


from collections import Counter, defaultdict
from typing import Iterable


def summarize_logs(entries: Iterable[tuple[str, str]]) -> tuple[list[tuple[str, int]], tuple[str, int]]:
    user_count: defaultdict[str, int] = defaultdict(int)
    action_count: Counter[str] = Counter()

    for user, action in entries:
        user_count[user] += 1
        action_count[action] += 1

    sorted_users = sorted(user_count.items(), key=lambda item: (-item[1], item[0]))
    if not action_count:
        top_action = ("NONE", 0)
    else:
        top_action = sorted(action_count.items(), key=lambda item: (-item[1], item[0]))[0]

    return sorted_users, top_action


def parse_log_input(text: str) -> list[tuple[str, str]]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    m = int(lines[0])
    entries: list[tuple[str, str]] = []
    for line in lines[1 : 1 + m]:
        user, action = line.split()
        entries.append((user, action))
    return entries


def format_summary(user_summary: list[tuple[str, int]], top_action: tuple[str, int]) -> str:
    user_lines = [f"{user} {count}" for user, count in user_summary]
    user_lines.append(f"top_action: {top_action[0]} {top_action[1]}")
    return "\n".join(user_lines)


def main() -> None:
    import sys

    entries = parse_log_input(sys.stdin.read())
    user_summary, top_action = summarize_logs(entries)
    print(format_summary(user_summary, top_action))


if __name__ == "__main__":
    main()
