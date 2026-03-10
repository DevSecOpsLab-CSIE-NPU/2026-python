from collections import Counter
from typing import List, Tuple


def log_summary(lines: List[str]) -> Tuple[List[str], str]:
    if not lines:
        return [], "top_action:  0"

    try:
        m = int(lines[0].strip())
    except Exception:
        raise ValueError("First line must be integer count")

    records = []
    for line in lines[1:1+m]:
        if not line.strip():
            continue
        parts = line.strip().split()
        if len(parts) != 2:
            raise ValueError("Each record must be 'user action'")
        records.append((parts[0], parts[1]))

    user_counter = Counter()
    action_counter = Counter()
    for user, action in records:
        user_counter[user] += 1
        action_counter[action] += 1

    user_list = sorted(
        user_counter.items(),
        key=lambda item: (-item[1], item[0])
    )

    if action_counter:
        max_action_count = max(action_counter.values())
        top_actions = sorted([a for a, c in action_counter.items() if c == max_action_count])
        top_action = top_actions[0]
        top_action_str = f"top_action: {top_action} {max_action_count}"
    else:
        top_action_str = "top_action:  0"

    user_lines = [f"{user} {count}" for user, count in user_list]
    return user_lines, top_action_str
