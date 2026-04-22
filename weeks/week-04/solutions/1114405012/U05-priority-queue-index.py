# U05. 優先佇列為何要加 index（1.5）
# 觀念：heap 會比較 tuple 的下一欄位。
# 若 priority 相同且下一欄是自訂物件，可能因無法比較而 TypeError。
# 解法：加上遞增 index，確保同優先權時仍可比較。

import heapq


class Item:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"Item({self.name!r})"


def section(title: str) -> None:
    print(f"\n=== {title} ===")


section("錯誤示範：同 priority 直接比 Item")
pq = []
try:
    heapq.heappush(pq, (-1, Item("a")))
    heapq.heappush(pq, (-1, Item("b")))
except TypeError as e:
    print("TypeError:", e)

section("正確做法：加入 index")
pq2 = []
index = 0
heapq.heappush(pq2, (-1, index, Item("a"))); index += 1
heapq.heappush(pq2, (-1, index, Item("b"))); index += 1
heapq.heappush(pq2, (-5, index, Item("urgent"))); index += 1

while pq2:
    priority, idx, item = heapq.heappop(pq2)
    print(f"pop -> priority={priority}, index={idx}, item={item}")
