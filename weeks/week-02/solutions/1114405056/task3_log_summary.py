"""
Task 3: Log Summary

輸入多行事件紀錄（user action），統計並輸出：
1. 每位使用者總事件數（總數↓，同數時 name↑）
2. 全域最常見 action 及其次數

輸入格式：
第一行：整數 m（紀錄筆數）
接著 m 行：user action
"""
import sys
from collections import defaultdict, Counter


def log_summary(lines: list[str]) -> None:
    """解析事件紀錄並輸出使用者統計與最熱門動作。"""
    m = int(lines[0])

    if m == 0:
        print("top_action: (none) 0")
        return

    user_counts: dict[str, int] = defaultdict(int)
    action_counter: Counter = Counter()

    for line in lines[1: m + 1]:
        parts = line.split()
        user, action = parts[0], parts[1]
        user_counts[user] += 1
        action_counter[action] += 1

    # 依總數↓ 再 name↑ 排序
    sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
    for user, count in sorted_users:
        print(f"{user} {count}")

    top_action, top_count = action_counter.most_common(1)[0]
    print(f"top_action: {top_action} {top_count}")


if __name__ == "__main__":
    lines = sys.stdin.read().strip().splitlines()
    log_summary(lines)
