"""
Task 3: Log Summary
實現事件日誌統計功能，使用Counter或defaultdict
"""

from collections import Counter, defaultdict
from typing import List, Tuple, Dict, Optional


def count_user_actions(logs: List[str]) -> Dict[str, int]:
    """
    計數每位使用者的事件數
    使用Counter實現
    """
    user_counts = Counter()
    for log in logs:
        parts = log.split()
        user = parts[0]
        user_counts[user] += 1
    return dict(user_counts)


def find_top_action(logs: List[str]) -> Tuple[Optional[str], int]:
    """
    找出最常見的action及其次數
    使用Counter實現
    """
    if not logs:
        return None, 0
    
    action_counts = Counter()
    for log in logs:
        parts = log.split()
        action = parts[1]
        action_counts[action] += 1
    
    if action_counts:
        top_action, count = action_counts.most_common(1)[0]
        return top_action, count
    
    return None, 0


def process_logs(lines: List[str]) -> str:
    """
    主流程：輸入為行列表，回傳統計結果
    第一行：m（紀錄筆數）
    接著m行：user action
    輸出：
    - 每位使用者總事件數（由多到少，同數則使用者名稱由小到大）
    - 全域最常見action及其次數
    """
    m = int(lines[0])
    
    if m == 0:
        return "top_action: none 0"
    
    log_lines = lines[1:m+1]
    
    # 統計使用者動作
    user_counts = count_user_actions(log_lines)
    
    # 排序使用者：由多到少，同數則名稱由小到大
    sorted_users = sorted(
        user_counts.items(),
        key=lambda x: (-x[1], x[0])  # 負數使分數由大到小，名稱由小到大
    )
    
    # 找出最常見的action
    top_action, action_count = find_top_action(log_lines)
    
    # 格式化輸出
    result = []
    for user, count in sorted_users:
        result.append(f"{user} {count}")
    
    if top_action:
        result.append(f"top_action: {top_action} {action_count}")
    else:
        result.append("top_action: none 0")
    
    return '\n'.join(result)


if __name__ == '__main__':
    # 測試預設例子
    test_input = [
        "8",
        "alice login",
        "bob login",
        "alice view",
        "alice logout",
        "bob view",
        "bob view",
        "chris login",
        "bob logout",
    ]
    
    print(process_logs(test_input))
