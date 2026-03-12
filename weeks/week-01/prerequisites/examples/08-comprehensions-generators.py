# 8 容器操作與推導式範例

# ── 串列推導式 ────────────────────────────────────────────

# 原始整數列表（同時有正數與負數）
nums = [1, -2, 3, -4]

# 串列推導式：從 nums 挑出所有大於 0 的值
# 等價於：先 for 逐一取出，再用 if 過濾，最後 append 到新串列
positives = [n for n in nums if n > 0]
print(positives)          # [1, 3]

# 也可以直接做運算，不一定要加 if
doubled = [n * 2 for n in nums]
print(doubled)            # [2, -4, 6, -8]

# 巢狀推導式：展開 2D 串列（矩陣攤平）
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)               # [1, 2, 3, 4, 5, 6]

# ── 字典推導式 ────────────────────────────────────────────

# pair 資料常見於「鍵值」形式
pairs = [('a', 1), ('b', 2)]

# 字典推導式：把 pair 轉成 dict
# k 會變成 key，v 會變成 value
lookup = {k: v for k, v in pairs}
print(lookup)             # {'a': 1, 'b': 2}

# 將既有 dict 的 value 全部乘以 2
original = {'x': 10, 'y': 20}
doubled_dict = {k: v * 2 for k, v in original.items()}
print(doubled_dict)       # {'x': 20, 'y': 40}

# ── 集合推導式 ────────────────────────────────────────────
# 與串列推導式相同語法，但用 {} 包住，結果是 set（自動去重）
words = ['apple', 'banana', 'apple', 'cherry']
unique_lengths = {len(w) for w in words}
print(unique_lengths)     # {5, 6} （去除重複長度）

# ── 生成器表達式 ──────────────────────────────────────────
# 逐個產生 n*n，不先建立完整中間串列
# sum(...) 會一邊取值一邊加總，較省記憶體
squares_sum = sum(n * n for n in nums)
print(squares_sum)        # 1+4+9+16 = 30

# 生成器可賦值給變數，之後用 next() 或 for 逐步取值
gen = (n * n for n in range(5))
print(next(gen))          # 0
print(next(gen))          # 1
print(list(gen))          # [4, 9, 16]（剩餘的值）
