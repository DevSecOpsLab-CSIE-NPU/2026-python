# 【Bloom 階段：U - 理解與進階應用】
# U5. 為什麼優先權隊列需要 index？
# August 的惡意提醒：這是物件比較地雷。
# 當兩筆資料的 priority 相等時，Python 會嘗試比較第二個元素（即 Item 物件）。
# 如果 Item 沒有定義 __lt__，就會噴 TypeError。

import heapq

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Item({self.name})"

pq = []
# 假設我們只有 (priority, item)
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # ❌ 這裡會報錯，因為 Item('a') 無法與 Item('b') 比較

# 解決方案：加入 index 阻止 Python 去比較 Item 物件
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1

print(f"Safe pop: {heapq.heappop(pq)}")
print("成功避開 TypeError 地雷！")
