from collections import defaultdict, Counter

def log_summary(logs):
    if not logs:
        return [], (None, 0)

    user_counts = defaultdict(int)
    action_counts = Counter()

    for user, action in logs:
        user_counts[user] += 1
        action_counts[action] += 1

    users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
    top_action = action_counts.most_common(1)[0] if action_counts else (None, 0)

    return users, top_action