"""
R03：deque（雙端佇列）

學習目標：
1. 了解 maxlen 的固定長度行為（滿了會自動淘汰最舊資料）。
2. 了解 append / appendleft / pop / popleft 的差異。
"""

from collections import deque


def main():
    print("=== R03 deque 雙端佇列 ===")

    # 範例 1：固定長度緩衝區。
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print("[例1] 依序加入 1,2,3 ->", list(q))

    q.append(4)  # 超過 maxlen，最舊的 1 會被自動移除
    print("[例1] 再加入 4，最舊值 1 被淘汰 ->", list(q))

    # 範例 2：左右兩端操作。
    q2 = deque()
    q2.append(1)
    q2.appendleft(2)
    print("[例2] append(1) + appendleft(2) ->", list(q2))

    right = q2.pop()
    left = q2.popleft()
    print("[例2] 右邊 pop 取出:", right)
    print("[例2] 左邊 popleft 取出:", left)


if __name__ == "__main__":
    main()
