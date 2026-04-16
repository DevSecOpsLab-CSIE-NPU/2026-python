
# 9 比較、排序與 key 函式

## 比較運算
```python
a < b  # 直接比較 a 與 b，適用於數字、字串、tuple 等
```
tuple 比較會依序比較每個元素，直到分出高下。

---

## 排序與 key 函式
```python
sorted(data, key=lambda x: x.price)  # 依物件的 price 屬性排序
min(data, key=itemgetter('uid'))     # 取 uid 最小的元素
```
key 參數可指定排序或比較的依據，常用 lambda 或 itemgetter。

---

## 用途（對應第一章範例）：

- tuple 比較順序：tuple 會逐一比較每個元素，適合用於多欄位排序
- 為何 `(priority, index, item)` 可排序：先比 priority，相同時比 index，確保排序穩定且不會因 item 不可比而出錯
- Top-N：可用 sorted 或 heapq 取出最大/最小 N 筆
- dict / object 排序：用 key 參數指定排序依據
- groupby 前置排序：groupby 需先依分組欄位排序，才能正確分組
