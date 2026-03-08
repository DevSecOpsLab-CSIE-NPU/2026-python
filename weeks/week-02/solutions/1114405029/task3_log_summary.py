from collections import Counter, defaultdict


def summarize_logs(records):
    """
    records: list of (user, action)
    returns:
        sorted_user_counts
        top_action
    """

    user_count = defaultdict(int)
    action_count = Counter()

    for user, action in records:
        user_count[user] += 1
        action_count[action] += 1

    # sort users
    sorted_users = sorted(
        user_count.items(),
        key=lambda x: (-x[1], x[0])
    )

    # find most common action
    if action_count:
        top_action, count = action_count.most_common(1)[0]
    else:
        top_action, count = None, 0

    return sorted_users, (top_action, count)


def main():
    import sys

    first_line = sys.stdin.readline().strip()
    if not first_line:
        return

    m = int(first_line)

    records = []

    for _ in range(m):
        line = sys.stdin.readline().strip()
        user, action = line.split()
        records.append((user, action))

    users, top = summarize_logs(records)

    for user, count in users:
        print(f"{user} {count}")

    action, count = top
    if action:
        print(f"top_action: {action} {count}")
    else:
        print("top_action: None 0")


if __name__ == "__main__":
    main()