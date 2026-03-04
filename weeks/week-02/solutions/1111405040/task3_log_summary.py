"""
Task 3: Log Summary
給定多行事件紀錄（user action），統計每位使用者行為次數，並輸出：
1. 每位使用者總事件數（依總數由大到小，若同數則使用者名稱由小到大）
2. 全域最常見 action 及其次數
"""

from collections import defaultdict, Counter


def parse_log_entry(line):
    """
    解析日誌行。
    
    Args:
        line: 格式為 "user action" 的字串
    
    Returns:
        (user, action) 的元組
    """
    parts = line.split()
    user = parts[0]
    action = parts[1]
    return (user, action)


def count_user_events(logs):
    """
    統計每位使用者的事件總數。
    
    Args:
        logs: 日誌列表，每個元素為 (user, action) 元組
    
    Returns:
        字典，鍵為使用者名稱，值為事件總數
    """
    user_counts = defaultdict(int)
    for user, action in logs:
        user_counts[user] += 1
    return user_counts


def find_top_action(logs):
    """
    找到最常見的 action。
    
    Args:
        logs: 日誌列表，每個元素為 (user, action) 元組
    
    Returns:
        (action, count) 元組
    """
    actions = [action for user, action in logs]
    action_counter = Counter(actions)
    # 使用 most_common(1) 獲得最常見的 action
    most_common_action, count = action_counter.most_common(1)[0]
    return (most_common_action, count)


def sort_users_by_count(user_counts):
    """
    依事件數由大到小排序使用者，若同數則名稱由小到大。
    
    Args:
        user_counts: 字典，鍵為使用者名稱，值為事件總數
    
    Returns:
        排序後的 (user, count) 列表
    """
    sorted_users = sorted(
        user_counts.items(),
        key=lambda x: (-x[1], x[0])  # 負值實現高到低，名稱字母序
    )
    return sorted_users


def log_summary(logs):
    """
    主函式：處理日誌統計。
    
    Args:
        logs: 日誌列表，每個元素為 (user, action) 元組
    
    Returns:
        字典，包含 'user_events' 和 'top_action'
    """
    user_counts = count_user_events(logs)
    sorted_users = sort_users_by_count(user_counts)
    top_action, action_count = find_top_action(logs)
    
    return {
        'user_events': sorted_users,
        'top_action': (top_action, action_count)
    }


def main():
    """主程式入口。"""
    # 第一行：m（日誌筆數）
    m = int(input().strip())
    
    # 讀取 m 行日誌
    logs = []
    for _ in range(m):
        line = input().strip()
        log_entry = parse_log_entry(line)
        logs.append(log_entry)
    
    # 統計並排序
    result = log_summary(logs)
    
    # 輸出使用者統計
    for user, count in result['user_events']:
        print(f"{user} {count}")
    
    # 輸出最常見的 action
    action, count = result['top_action']
    print(f"top_action: {action} {count}")


if __name__ == '__main__':
    main()
