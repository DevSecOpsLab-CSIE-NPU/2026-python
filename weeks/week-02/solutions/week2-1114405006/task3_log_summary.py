from __future__ import annotations

from collections import Counter, defaultdict
from typing import Iterable, List, Tuple


def parse_events(text: str) -> List[Tuple[str, str]]:
    stripped = text.strip()
    if not stripped:
        return []

    lines = stripped.splitlines()
    event_count = int(lines[0])
    events: List[Tuple[str, str]] = []
    for line in lines[1 : 1 + event_count]:
        user, action = line.split()
        events.append((user, action))
    return events


def summarize_events(events: Iterable[Tuple[str, str]]) -> tuple[list[tuple[str, int]], tuple[str, int]]:
    user_counts = defaultdict(int)
    action_counts = Counter()

    for user, action in events:
        user_counts[user] += 1
        action_counts[action] += 1

    user_totals = sorted(user_counts.items(), key=lambda item: (-item[1], item[0]))
    if action_counts:
        top_action = action_counts.most_common(1)[0]
    else:
        top_action = ("none", 0)
    return user_totals, top_action


def format_summary(user_totals: Iterable[tuple[str, int]], top_action: tuple[str, int]) -> str:
    lines = [f"{user} {count}" for user, count in user_totals]
    lines.append(f"top_action: {top_action[0]} {top_action[1]}")
    return "\n".join(lines)


def solve(text: str) -> str:
    events = parse_events(text)
    user_totals, top_action = summarize_events(events)
    return format_summary(user_totals, top_action)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()