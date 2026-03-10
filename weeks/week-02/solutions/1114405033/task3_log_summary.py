from collections import defaultdict, Counter

def summarize_logs(logs):
    if not logs:
        return [], None
    
    user_map = defaultdict(int)
    action_list = []
    for user, action in logs:
        user_map[user] += 1
        action_list.append(action)
    
    
    sorted_users = sorted(user_map.items(), key=lambda x: (-x[1], x[0]))
     
    top_action = Counter(action_list).most_common(1)[0]
    return sorted_users, top_action

if __name__ == "__main__":
    try:
        line = input()
        if not line: exit()
        m = int(line)
        logs = [tuple(input().split()) for _ in range(m)]
        users, top = summarize_logs(logs)
        for u, c in users:
            print(f"{u} {c}")
        if top:
            print(f"top_action: {top[0]} {top[1]}")
    except (EOFError, ValueError):
        pass