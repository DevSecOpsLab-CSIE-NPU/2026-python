"""
Task 3: Log Summary
統計每位使用者的總事件數，以及最常見的 action
"""

from collections import defaultdict, Counter


def summarize_logs(logs):
    """
    統計日誌資料

    參數：
        logs: (user, action) 列表
    回傳：
        (user_counts, top_action) 元組
    """
    if not logs:
        return [], None

    user_counts = defaultdict(int)
    action_counter = Counter()

    for user, action in logs:
        user_counts[user] += 1
        action_counter[action] += 1

    sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))

    top_action = action_counter.most_common(1)[0] if action_counter else None

    return sorted_users, top_action


def main():
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]

    if not lines:
        return

    m = int(lines[0])
    logs = []

    for i in range(1, m + 1):
        parts = lines[i].split()
        user = parts[0]
        action = parts[1]
        logs.append((user, action))

    user_counts, top_action = summarize_logs(logs)

    for user, count in user_counts:
        print(f"{user} {count}")

    if top_action:
        print(f"top_action: {top_action[0]} {top_action[1]}")


if __name__ == "__main__":
    main()
