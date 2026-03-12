import sys
from collections import Counter
from typing import List, Tuple


Event = Tuple[str, str]


def parse_events(raw: str) -> List[Event]:
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    if not lines:
        return []

    m = int(lines[0])
    events: List[Event] = []
    for line in lines[1 : m + 1]:
        user, action = line.split()
        events.append((user, action))
    return events


def sorted_user_counts(events: List[Event]) -> List[Tuple[str, int]]:
    user_counter = Counter(user for user, _ in events)
    return sorted(user_counter.items(), key=lambda item: (-item[1], item[0]))


def most_common_action(events: List[Event]) -> Tuple[str, int]:
    action_counter = Counter(action for _, action in events)
    if not action_counter:
        return "none", 0
    return sorted(action_counter.items(), key=lambda item: (-item[1], item[0]))[0]


def solve(raw: str) -> str:
    events = parse_events(raw)
    user_counts = sorted_user_counts(events)
    action, count = most_common_action(events)

    lines = [f"{user} {total}" for user, total in user_counts]
    lines.append(f"top_action: {action} {count}")
    return "\n".join(lines)


def main() -> None:
    raw = sys.stdin.read()
    print(solve(raw))


if __name__ == "__main__":
    main()
