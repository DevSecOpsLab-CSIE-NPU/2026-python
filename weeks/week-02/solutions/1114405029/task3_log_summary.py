"""
Task 3: Log Summary
統計使用者行為次數，並找出全域最常見的動作。
"""
from collections import defaultdict, Counter

def summarize_logs(logs):
    """
    處理紀錄並回傳：
    1. 排序後的使用者統計列表
    2. 最常見的動作及其次數
    """
    user_counts = defaultdict(int)
    action_counts = Counter()

    for user, action in logs:
        user_counts[user] += 1
        action_counts[action] += 1

    # 排序規則：次數由大到小 (-x[1])，使用者名稱由小到大 (x[0])
    sorted_users = sorted(
        user_counts.items(), 
        key=lambda x: (-x[1], x[0])
    )

    # 取得最常見的動作
    top_action_item = None
    if action_counts:
        # most_common(1) 回傳 [('action', count)]
        top_action_item = action_counts.most_common(1)[0]

    return sorted_users, top_action_item

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    try:
        m = int(input_data[0])
        logs = []
        idx = 1
        for _ in range(m):
            if idx + 1 < len(input_data):
                user = input_data[idx]
                action = input_data[idx + 1]
                logs.append((user, action))
                idx += 2
        
        sorted_users, top_action = summarize_logs(logs)

        # 輸出使用者統計
        for user, count in sorted_users:
            print(f"{user} {count}")

        # 輸出最常見動作
        if top_action:
            print(f"top_action: {top_action[0]} {top_action[1]}")
            
    except (ValueError, IndexError):
        return

if __name__ == "__main__":
    main()