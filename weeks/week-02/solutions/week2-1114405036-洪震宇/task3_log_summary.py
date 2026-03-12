"""Task 3: Log Summary

Given lines of `user action`, produce:
 1) per-user counts sorted by total desc then username asc
 2) global top action and its count

This module uses Counter/collections as required.
"""

from __future__ import annotations

from collections import Counter
from typing import Iterable, List, Tuple


def parse_log_line(line: str) -> Tuple[str, str]:
    """Parse a log line into (user, action)."""
    parts = line.strip().split()
    if len(parts) != 2:
        raise ValueError(f"Expected 2 parts, got {len(parts)}: {line!r}")
    return parts[0], parts[1]


def summarize_logs(lines: Iterable[str]) -> Tuple[List[Tuple[str, int]], Tuple[str, int]]:
    """Summarize logs.

    Returns:
        A tuple of (sorted_user_counts, top_action_and_count).
    """
    user_counter: Counter[str] = Counter()
    action_counter: Counter[str] = Counter()

    for line in lines:
        if not line.strip():
            continue
        user, action = parse_log_line(line)
        user_counter[user] += 1
        action_counter[action] += 1

    # sort by count desc, then user asc
    sorted_users = sorted(user_counter.items(), key=lambda kv: (-kv[1], kv[0]))

    if action_counter:
        max_count = max(action_counter.values())
        top_actions = sorted([act for act, cnt in action_counter.items() if cnt == max_count])
        top_action = (top_actions[0], max_count)
    else:
        top_action = ("", 0)

    return sorted_users, top_action


def format_summary(users: List[Tuple[str, int]], top_action: Tuple[str, int]) -> str:
    """Format the summary for printing."""
    lines: List[str] = [f"{user} {count}" for user, count in users]
    if top_action[1] > 0:
        lines.append(f"top_action: {top_action[0]} {top_action[1]}")
    else:
        lines.append("top_action:  0")
    return "\n".join(lines)


def main() -> None:
    import sys

    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    try:
        m = int(data[0].strip())
    except ValueError as e:
        raise ValueError(f"First line must be an integer: {data[0]!r}") from e

    lines = data[1 : 1 + m]
    users, top_action = summarize_logs(lines)
    print(format_summary(users, top_action))


if __name__ == "__main__":
    main()
