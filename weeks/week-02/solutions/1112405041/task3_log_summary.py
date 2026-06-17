from collections import Counter, defaultdict

def summarize_logs(m, log_data):
    """
    Task 3: Log Summary
    要求：
    1. 每位使用者總事件數 (總數降序，名稱升序)
    2. 全域最常見 action 及其次數
    """
    if m == 0 or not log_data:
        return [], "None 0"

    user_counts = defaultdict(int)
    action_counts = Counter()

    for line in log_data:
        parts = line.split()
        if len(parts) == 2:
            user, action = parts
            user_counts[user] += 1
            action_counts[action] += 1

    # 使用者排序：次數降序 (-count)，名稱升序 (name)
    sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))

    user_results = [f"{user} {count}" for user, count in sorted_users]

    # 全域最常見 action
    if action_counts:
        # most_common(1) 回傳 [('action', count)]
        top_action, top_count = action_counts.most_common(1)[0]
        action_result = f"top_action: {top_action} {top_count}"
    else:
        action_result = "top_action: None 0"

    return user_results, action_result

if __name__ == "__main__":
    # 測試範例
    m = 8
    logs = [
        "alice login",
        "bob login",
        "alice view",
        "alice logout",
        "bob view",
        "bob view",
        "chris login",
        "bob logout"
    ]
    u_res, a_res = summarize_logs(m, logs)
    for u in u_res:
        print(u)
    print(a_res)
