from collections import Counter

def summarize_logs(logs):
    if not logs: return [], None, 0
    user_counts = Counter(u for u, a in logs)
    action_counts = Counter(a for u, a in logs)
    sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
    top_action, count = action_counts.most_common(1)[0]
    return sorted_users, top_action, count