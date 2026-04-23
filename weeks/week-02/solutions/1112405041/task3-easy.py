# task3-easy.py
# Task 3: Log Summary (簡單版)

from collections import Counter

def solve():
    # 範例輸入
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
    
    # 分離 user 和 action
    users = []
    actions = []
    for entry in logs:
        u, a = entry.split()
        users.append(u)
        actions.append(a)

    # 統計使用者事件數
    user_counts = Counter(users)
    # 統計 Action
    action_counts = Counter(actions)
    
    # 排序使用者：次數(降序), 名字(升序)
    sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
    
    for user, count in sorted_users:
        print(f"{user} {count}")

    top_action = action_counts.most_common(1)[0]
    print(f"top_action: {top_action[0]} {top_action[1]}")

if __name__ == "__main__":
    solve()
