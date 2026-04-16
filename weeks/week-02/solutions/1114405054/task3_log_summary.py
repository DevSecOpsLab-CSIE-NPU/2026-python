from __future__ import annotations

from collections import Counter, defaultdict
import sys


def parse_logs(data: str) -> list[tuple[str, str]]:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return []
    m = int(lines[0])
    logs: list[tuple[str, str]] = []
    for line in lines[1 : 1 + m]:
        user, action = line.split()
        logs.append((user, action))
    return logs


def summarize(logs: list[tuple[str, str]]) -> tuple[list[tuple[str, int]], tuple[str, int]]:
    user_counts: defaultdict[str, int] = defaultdict(int)
    action_counts: Counter[str] = Counter()

    for user, action in logs:
        user_counts[user] += 1
        action_counts[action] += 1

    ordered_users = sorted(user_counts.items(), key=lambda item: (-item[1], item[0]))

    if not action_counts:
        top_action = ("none", 0)
    else:
        max_count = max(action_counts.values())
        action_name = min(action for action, cnt in action_counts.items() if cnt == max_count)
        top_action = (action_name, max_count)

    return ordered_users, top_action


def solve(data: str) -> str:
    logs = parse_logs(data)
    ordered_users, top_action = summarize(logs)

    lines = [f"{user} {count}" for user, count in ordered_users]
    lines.append(f"top_action: {top_action[0]} {top_action[1]}")
    return "\n".join(lines)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()