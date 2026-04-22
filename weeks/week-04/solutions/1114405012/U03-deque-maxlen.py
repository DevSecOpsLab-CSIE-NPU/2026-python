# U03. deque(maxlen=N) 為何能只保留最後 N 筆（1.3）
# 觀念：deque 設定 maxlen 後，append 新元素時若已滿，會自動丟掉最舊元素。

from collections import deque


def section(title: str) -> None:
    print(f"\n=== {title} ===")


section("maxlen=3 的滑動視窗")
q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)
    print(f"append({i}) ->", list(q))

section("appendleft 也會觸發淘汰")
q2 = deque([10, 20, 30], maxlen=3)
print("初始 q2:", list(q2))
q2.appendleft(5)
print("appendleft(5) 後 q2:", list(q2))
