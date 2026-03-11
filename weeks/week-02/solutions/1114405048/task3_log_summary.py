"""
Task 3: Log Summary
給定多行事件紀錄（user action），統計每位使用者行為次數，輸出：
1. 每位使用者總事件數（依總數由大到小，若同數則使用者名稱由小到大）
2. 全域最常見 action 及其次數
"""

from collections import defaultdict, Counter


def parse_logs(m, lines):
    """
    解析日誌
    
    Args:
        m: 紀錄筆數
        lines: 日誌行的列表
    
    Returns:
        使用者事件字典和所有動作列表
    """
    user_actions = defaultdict(int)  # 每個使用者的總事件數
    all_actions = []  # 所有動作，用於統計最常見動作
    
    for line in lines:
        if line.strip():  # 忽略空行
            parts = line.split()
            if len(parts) >= 2:
                user = parts[0]
                action = parts[1]
                user_actions[user] += 1
                all_actions.append(action)
    
    return user_actions, all_actions


def rank_users(user_actions):
    """
    排名使用者
    規則：按總事件數由大到小，若同數則名稱由小到大
    
    Args:
        user_actions: {user: count} 字典
    
    Returns:
        排序後的 [(user, count), ...] 列表
    """
    # 按計數降序，名稱升序排列
    return sorted(user_actions.items(), key=lambda x: (-x[1], x[0]))


def get_top_action(all_actions):
    """
    取得最常見的動作
    
    Args:
        all_actions: 所有動作的列表
    
    Returns:
        (action, count) 或 (None, 0) 如果無動作
    """
    if not all_actions:
        return None, 0
    
    # 使用 Counter 統計最常見動作
    action_counter = Counter(all_actions)
    most_common = action_counter.most_common(1)[0]
    return most_common


def format_output(ranked_users, top_action, top_count):
    """
    格式化輸出
    
    Args:
        ranked_users: 排序後的使用者列表
        top_action: 最常見的動作
        top_count: 該動作的出現次數
    
    Returns:
        格式化後的字符串列表
    """
    output = []
    
    # 輸出每個使用者
    for user, count in ranked_users:
        output.append(f"{user} {count}")
    
    # 輸出最常見動作
    if top_action is not None:
        output.append(f"top_action: {top_action} {top_count}")
    
    return output


def process_logs(m, lines):
    """
    主要處理函式
    
    Args:
        m: 紀錄筆數
        lines: 日誌行的列表
    
    Returns:
        格式化後的輸出
    """
    user_actions, all_actions = parse_logs(m, lines)
    ranked_users = rank_users(user_actions)
    top_action, top_count = get_top_action(all_actions)
    return format_output(ranked_users, top_action, top_count)


def main():
    """主程式入口"""
    try:
        m = int(input().strip())
        
        lines = []
        for _ in range(m):
            lines.append(input().strip())
        
        results = process_logs(m, lines)
        for line in results:
            print(line)
    except EOFError:
        pass


if __name__ == "__main__":
    main()
