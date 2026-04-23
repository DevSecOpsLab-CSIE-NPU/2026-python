# task3.py
# Task 3: Log Summary

from collections import defaultdict, Counter

def summarize_logs(logs):
    if not logs:
        return {}, ("", 0)
        
    user_counts = defaultdict(int)
    action_counts = Counter()
    
    for user, action in logs:
        user_counts[user] += 1
        action_counts[action] += 1
        
    # 1. 使用者總事件數排序：
    # 次數由大到小 (-x[1]), 使用者名稱由小到大 (x[0])
    sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # 2. 全域最常見 action
    if action_counts:
        top_action = action_counts.most_common(1)[0]
    else:
        top_action = ("", 0)
        
    return sorted_users, top_action

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        sys.exit(0)

    m = int(input_data[0])
    logs = []
    idx = 1
    for _ in range(m):
        if idx + 1 < len(input_data):
            user = input_data[idx]
            action = input_data[idx+1]
            logs.append((user, action))
            idx += 2

    sorted_users, top_action = summarize_logs(logs)
    
    for user, count in sorted_users:
        print(f"{user} {count}")

    if top_action[0]:
        print(f"top_action: {top_action[0]} {top_action[1]}")
