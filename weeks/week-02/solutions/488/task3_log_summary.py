"""Task 3: Log Summary."""

from collections import Counter


Record = tuple[str, str]


def summarize_logs(records: list[Record]) -> tuple[list[tuple[str, int]], tuple[str, int] | None]:
    """Return user event counts and global top action."""
    user_counter: Counter[str] = Counter()
    action_counter: Counter[str] = Counter()

    for user, action in records:
        user_counter[user] += 1
        action_counter[action] += 1

    user_counts = sorted(user_counter.items(), key=lambda pair: (-pair[1], pair[0]))

    if not action_counter:
        return user_counts, None

    top_action = sorted(action_counter.items(), key=lambda pair: (-pair[1], pair[0]))[0]
    return user_counts, top_action


def parse_records(lines: list[str]) -> list[Record]:
    """Parse input lines into records."""
    if not lines:
        return []

    m = int(lines[0].strip()) if lines[0].strip() else 0
    records: list[Record] = []

    for line in lines[1:1 + m]:
        parts = line.strip().split()
        if len(parts) == 2:
            user, action = parts
            records.append((user, action))

    return records


def solve(lines: list[str]) -> list[str]:
    """Solve Task 3 from input lines and return output lines."""
    records = parse_records(lines)
    user_counts, top_action = summarize_logs(records)

    output_lines = [f"{user} {count}" for user, count in user_counts]

    if top_action is None:
        output_lines.append("top_action: None 0")
    else:
        action, count = top_action
        output_lines.append(f"top_action: {action} {count}")

    return output_lines


def main() -> None:
    import sys

    lines = [line.rstrip("\n") for line in sys.stdin]
    for output_line in solve(lines):
        print(output_line)


if __name__ == "__main__":
    main()
