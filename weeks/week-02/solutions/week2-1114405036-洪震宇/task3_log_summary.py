"""
Task 3: Log Summary
回家作業：使用 defaultdict 和 Counter 進行統計
"""

from collections import defaultdict, Counter


def parse_logs(log_lines):
    """
    解析日誌行列表
    
    Args:
        log_lines: list of strings in format "user action"
        
    Returns:
        list: 包含 (user, action) tuple 的列表
    """
    logs = []
    for line in log_lines:
        parts = line.strip().split()
        if len(parts) != 2:
            raise ValueError(f"Invalid format: {line}")
        user, action = parts
        logs.append((user, action))
    return logs


def count_user_events(logs):
    """
    計算每位使用者的總事件數，使用 defaultdict
    
    Args:
        logs: list of (user, action) tuples
        
    Returns:
        dict: user -> event_count 的映射
    """
    user_count = defaultdict(int)
    for user, action in logs:
        user_count[user] += 1
    return user_count


def get_top_action(logs):
    """
    取得全域最常見的 action，使用 Counter
    
    Args:
        logs: list of (user, action) tuples
        
    Returns:
        tuple: (action, count) 最常見的行為與次數
    """
    if not logs:
        return None, 0
    
    actions = [action for user, action in logs]
    action_counter = Counter(actions)
    
    # 取得最常見的
    if action_counter:
        top_action, count = action_counter.most_common(1)[0]
        return top_action, count
    
    return None, 0


def rank_users(user_count):
    """
    排序使用者：依總數由大到小，同數時使用者名稱由小到大
    
    Args:
        user_count: dict 或 defaultdict，user -> count
        
    Returns:
        list: 排序後的 (user, count) tuple 列表
    """
    # 轉換為列表並排序
    # key: (-count, user) 表示 count 倒序，user 正序
    sorted_users = sorted(
        user_count.items(),
        key=lambda x: (-x[1], x[0])
    )
    return sorted_users


def process_logs(m, log_lines):
    """
    主要處理函式
    
    Args:
        m: 記錄筆數
        log_lines: 記錄行列表
        
    Returns:
        dict: 包含 user_ranking 和 top_action 的結果
    """
    if m != len(log_lines):
        raise ValueError(f"Expected {m} logs, got {len(log_lines)}")
    
    if m == 0:
        # 空輸入的處理
        return {
            'user_ranking': [],
            'top_action': None,
            'top_action_count': 0
        }
    
    logs = parse_logs(log_lines)
    user_count = count_user_events(logs)
    top_action, top_count = get_top_action(logs)
    ranked_users = rank_users(user_count)
    
    return {
        'user_ranking': ranked_users,
        'top_action': top_action,
        'top_action_count': top_count
    }


def format_output(results):
    """
    格式化輸出結果
    
    Args:
        results: process_logs 返回的 dict
        
    Returns:
        str: 格式化的輸出字串
    """
    lines = []
    
    # 輸出使用者統計
    for user, count in results['user_ranking']:
        lines.append(f"{user} {count}")
    
    # 輸出最常見的 action
    if results['top_action']:
        lines.append(f"top_action: {results['top_action']} {results['top_action_count']}")
    
    return '\n'.join(lines)


def main():
    """主程式"""
    print("=== Task 3: Log Summary ===")
    print("輸入 m（記錄筆數）:")
    
    m = int(input().strip())
    
    print(f"輸入 {m} 條記錄（格式: user action）:")
    log_lines = []
    for _ in range(m):
        if m > 0:  # 只在 m > 0 時讀取輸入
            log_lines.append(input().strip())
    
    try:
        results = process_logs(m, log_lines)
        output = format_output(results)
        print("\n輸出:")
        if output:
            print(output)
        else:
            print("(空輸入)")
    except ValueError as e:
        print(f"錯誤：{e}")


if __name__ == "__main__":
    main()
