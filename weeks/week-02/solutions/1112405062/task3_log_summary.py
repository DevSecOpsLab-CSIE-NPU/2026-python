"""
================================================================================
Task 3: Log Summary
================================================================================

題目說明：
    給定多行事件紀錄（user action），統計每位使用者行為次數，並輸出：
    1. 每位使用者總事件數（依總數由大到小，若同數則使用者名稱由小到大）
    2. 全域最常見 action 及其次數

================================================================================
"""

from typing import List, Dict
from collections import defaultdict, Counter

def log_summary(input_lines: List[str]) -> Dict[str, any]:
    """
    日誌統計

    參數：
        input_lines: 輸入行列表，第一行為 m（紀錄筆數），接著 m 行 user action

    回傳：
        包含 users（使用者排序列表）和 top_action（最常見 action）的字典
    """
    if not input_lines:
        return {"users": [], "top_action": ""}

    # 解析輸入
    try:
        m = int(input_lines[0].strip())
    except (ValueError, IndexError):
        return {"users": [], "top_action": ""}

    if m == 0:
        return {"users": [], "top_action": ""}

    # 統計
    user_counts = defaultdict(int)
    action_counts = Counter()

    for line in input_lines[1 : 1 + m]:
        parts = line.strip().split()
        if len(parts) == 2:
            user, action = parts[0], parts[1]
            user_counts[user] += 1
            action_counts[action] += 1

    # 排序使用者：總數由大到小，若同數則名稱由小到大
    sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
    users_output = [f"{user} {count}" for user, count in sorted_users]

    # 找最常見的 action
    if action_counts:
        top_action_name, top_action_count = action_counts.most_common(1)[0]
        top_action = f"{top_action_name} {top_action_count}"
    else:
        top_action = ""

    return {"users": users_output, "top_action": top_action}


def main():
    """主函式：讀取輸入並輸出結果"""
    try:
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        result = log_summary(lines)

        for user_line in result["users"]:
            print(user_line)
        if result["top_action"]:
            print(f"top_action: {result['top_action']}")
    except EOFError:
        pass


if __name__ == "__main__":
    main()
