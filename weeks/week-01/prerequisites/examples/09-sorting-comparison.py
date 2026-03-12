# 9 比較、排序與 key 函式範例

# ── tuple 字典序比較 ──────────────────────────────────────
# tuple 比較採「字典序」：從左到右逐一比
# 先比第一個元素，若相同再比第二個，以此類推
a = (1, 2)
b = (1, 3)
result = a < b        # True，因為前面 1==1，接著 2<3
print(result)         # True
print((2, 0) > (1, 9))  # True，第一個元素 2 > 1 就決定了

# ── sorted() ─────────────────────────────────────────────
# sorted() 不改變原始串列，回傳一個新的已排序串列
nums = [3, 1, 4, 1, 5, 9]
asc = sorted(nums)              # 升冪（預設）
desc = sorted(nums, reverse=True)  # 降冪
print(asc)            # [1, 1, 3, 4, 5, 9]
print(desc)           # [9, 5, 4, 3, 1, 1]

# 字串串列：預設按字母順序
names = ['Charlie', 'Alice', 'Bob']
print(sorted(names))              # ['Alice', 'Bob', 'Charlie']
print(sorted(names, key=len))     # 依長度排序

# ── sorted + key（字典串列）─────────────────────────────
# 這是一個由字典組成的串列，常見於資料列（rows）
rows = [{'uid': 3, 'name': 'C'}, {'uid': 1, 'name': 'A'}, {'uid': 2, 'name': 'B'}]

# sorted + key：告訴 Python「排序依據」是每筆資料的 uid
# lambda r: r['uid'] 的意思：輸入一筆 r，回傳它的 uid 作為排序鍵
rows_sorted = sorted(rows, key=lambda r: r['uid'])
print(rows_sorted)    # uid 1 → 2 → 3 的順序

# 多重排序鍵：先依 score 降冪，再依 name 升冪
students = [
    {'name': 'Alice', 'score': 90},
    {'name': 'Bob',   'score': 90},
    {'name': 'Carol', 'score': 85},
]
# key 回傳 tuple，Python 同樣用字典序比較
result2 = sorted(students, key=lambda s: (-s['score'], s['name']))
print(result2)        # Alice, Bob（同分按名字）, Carol

# ── min / max ────────────────────────────────────────────
# min/max 也能搭配 key
# 這裡會找出 uid 最小的那一筆資料（不是整個字典直接比大小）
smallest = min(rows, key=lambda r: r['uid'])
largest  = max(rows, key=lambda r: r['uid'])
print(smallest)       # {'uid': 1, 'name': 'A'}
print(largest)        # {'uid': 3, 'name': 'C'}
