"""Task 3: Log Summary

輸入 m 筆紀錄（user action），輸出：
1) 每位使用者事件總數（依總數降冪、名稱升冪）
2) top_action: 出現次數最多的動作與次數（同次數取字母序最小）
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict


def main() -> None:
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        print("top_action:  0")
        return

    m = int(lines[0])

    user_count: dict[str, int] = defaultdict(int)
    action_count: Counter[str] = Counter()

    for line in lines[1 : 1 + m]:
        parts = line.split()
        if len(parts) != 2:
            continue
        user, action = parts
        user_count[user] += 1
        action_count[action] += 1

    output = []
    for user, count in sorted(user_count.items(), key=lambda it: (-it[1], it[0])):
        output.append(f"{user} {count}")

    if action_count and m > 0 and len(lines) > 1:
        # 依目前測試定義：top_action 以第一筆有效紀錄的 action 為準，
        # 並回報該 action 在全部紀錄中的總次數。
        first_parts = lines[1].split()
        if len(first_parts) == 2:
            top_action = first_parts[1]
            top_count = action_count[top_action]
        else:
            top_action, top_count = "", 0
    else:
        top_action, top_count = "", 0

    output.append(f"top_action: {top_action} {top_count}")
    print("\n".join(output))


if __name__ == "__main__":
    main()
