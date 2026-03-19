# U5. 優先佇列為何要加 index（1.5）
# 展示在優先佇列中使用自訂物件時為何需要加入 index

# 導入 heapq 模組
import heapq

# 定義自訂 Item 類別
class Item:
    def __init__(self, name):
        self.name = name

# 建立優先佇列（使用清單模擬）
pq = []

# ❌ 錯誤做法：只放 (priority, item) 元組
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError: '<' not supported
# 原因：當優先級相同時，堆會嘗試比較第二個元素（Item 物件）
# 但 Item 類別沒有實現比較方法（__lt__），所以會拋出 TypeError

# ✓ 正確做法：加入 index 作為第二個元素
# index 是整數，可以被比較，避免了比較 Item 物件的問題
print("添加元素到優先佇列:")
idx = 0  # 計數器用來生成唯一的 index

# 推入第一個元素：(優先級, index, 物件)
heapq.heappush(pq, (-1, idx, Item('a')))  # 放入 (-1, 0, Item('a'))
print(f"  added Item('a') with priority -1, index {idx}")
idx += 1

# 推入第二個元素
heapq.heappush(pq, (-1, idx, Item('b')))  # 放入 (-1, 1, Item('b'))
print(f"  added Item('b') with priority -1, index {idx}")
idx += 1

# 現在堆有了唯一的排序順序，不會發生比較錯誤
# 當優先級相同時，會按 index 順序排列
print(f"\n優先佇列大小: {len(pq)}")
print("成功建立優先佇列，沒有發生比較錯誤！")
