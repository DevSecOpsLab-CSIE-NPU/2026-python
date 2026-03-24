from collections import Counter, defaultdict

def summarize_logs(logs):
    """
    Summarize user actions from logs.

    Args:
        logs (list): List of tuples (user, action)

    Returns:
        tuple: (user_counts, top_action)
            user_counts: List of (user, count) sorted by count desc, then user asc
            top_action: (action, count) of most frequent action, or None if empty
    """
    if not logs:
        return [], None

    # Count actions per user
    user_counter = Counter()
    action_counter = Counter()

    for user, action in logs:
        user_counter[user] += 1
        action_counter[action] += 1

    # Sort users: by count desc, then by name asc
    user_counts = sorted(user_counter.items(), key=lambda x: (-x[1], x[0]))

    # Find top action
    if action_counter:
        top_action = action_counter.most_common(1)[0]
    else:
        top_action = None

    return user_counts, top_action