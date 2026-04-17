# R13. 字典列表排序 itemgetter（1.13）
# =========================================================
# itemgetter 是 operator 模組中的函數，用於建立取元素函數
# 比 lambda 更快、更簡潔，常用於 sorted()、min()、max() 等函數的 key 參數
# =========================================================

from operator import itemgetter

# 模擬數據庫查詢結果：使用者列表（字典列表）
rows = [
    {'fname': 'Brian', 'uid': 1003},
    {'fname': 'John', 'uid': 1001}
]

# =========================================================
# itemgetter('fname'): 創建一個函數，功能等同於 lambda x: x['fname']
# 調用 itemgetter('fname')(row) 會返回 row['fname']
# =========================================================

# 按名字排序（升序）
# 返回：[{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]
sorted(rows, key=itemgetter('fname'))

# 按 uid 排序（升序）
# 返回：[{'fname': 'John', 'uid': 1001}, {'fname': 'Brian', 'uid': 1003}]
sorted(rows, key=itemgetter('uid'))

# 多鍵排序：先按 uid 排序，uid 相同時按 fname 排序
# 等同於先按第一個鍵排序，再按第二個鍵排序（穩定排序的特性）
sorted(rows, key=itemgetter('uid', 'fname'))

# =========================================================
# itemgetter 的其他用法
# =========================================================

# 數值索引：適用於元組或列表
# data = [('a', 1), ('b', 2), ('c', 3)]
# sorted(data, key=itemgetter(1)) 按第二個元素排序

# 多索引：同時取多個值
# itemgetter(0, 1)(('a', 'b', 'c')) 返回 ('a', 'b')

# =========================================================
# itemgetter vs lambda 的比較
# =========================================================

# itemgetter('name') 比 lambda x: x['name'] 更快
# 因為 itemgetter 是用 C 實現的
# 當需要排序字典列表時，itemgetter 是首選
