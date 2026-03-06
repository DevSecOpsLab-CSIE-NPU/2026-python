from __future__ import annotations

from collections import Counter, defaultdict
from typing import List, Optional, Tuple


def summarize_logs(records: List[Tuple[str, str]]) -> tuple[List[Tuple[str, int]], Optional[Tuple[str, int]]]:
    user_counts = defaultdict(int)
    action_counts: Counter[str] = Counter()

    for user, action in records:
        user_counts[user] += 1
        action_counts[action] += 1

    sorted_users = sorted(user_counts.items(), key=lambda item: (-item[1], item[0]))

    if not action_counts:
        return sorted_users, None

    top_count = max(action_counts.values())
    top_action = min(action for action, count in action_counts.items() if count == top_count)
    return sorted_users, (top_action, top_count)


def parse_input(raw: str) -> List[Tuple[str, str]]:
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    if not lines:
        return []

    m = int(lines[0])
    records: List[Tuple[str, str]] = []
    for line in lines[1 : 1 + m]:
        user, action = line.split()
        records.append((user, action))
    return records


def main() -> None:
    import sys

    users, top_action = summarize_logs(parse_input(sys.stdin.read()))
    for user, count in users:
        print(f"{user} {count}")

    if top_action is None:
        print("top_action: NONE 0")
    else:
        action, count = top_action
        print(f"top_action: {action} {count}")


if __name__ == "__main__":
    main()
