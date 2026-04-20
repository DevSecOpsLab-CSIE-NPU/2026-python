# R6. 多值字典 defaultdict / setdefault（1.6）

# 從 collections 模組導入 defaultdict 類別。
from collections import defaultdict

print("--- 使用 defaultdict(list) ---")
# 創建一個 defaultdict，其預設值工廠函式是 list。
# 這表示當訪問一個不存在的鍵時，會自動創建一個空列表 [] 作為該鍵的值。
d = defaultdict(list)
print(f"初始化 defaultdict(list) d: {d}")

# 向鍵 'a' 對應的列表中添加元素 1。
# 因為 'a' 不存在，會先自動創建一個空列表 []，然後將 1 添加進去。
d['a'].append(1)
print(f"d['a'].append(1) 後: {d}")
# 再次向鍵 'a' 對應的列表中添加元素 2。
d['a'].append(2)
print(f"d['a'].append(2) 後: {d}")

print("\n--- 使用 defaultdict(set) ---")
# 創建一個 defaultdict，其預設值工廠函式是 set。
# 這表示當訪問一個不存在的鍵時，會自動創建一個空集合 set() 作為該鍵的值。
d = defaultdict(set)
print(f"初始化 defaultdict(set) d: {d}")

# 向鍵 'a' 對應的集合中添加元素 1。
d['a'].add(1)
print(f"d['a'].add(1) 後: {d}")
# 向鍵 'a' 對應的集合中添加元素 2。
d['a'].add(2)
print(f"d['a'].add(2) 後: {d}")

print("\n--- 使用 dict.setdefault() ---")
# 創建一個普通的字典 d。
d = {}
print(f"初始化普通字典 d: {d}")

# 使用 setdefault() 方法。
# d.setdefault('a', []) 會檢查鍵 'a' 是否存在。
# 如果不存在，它會將 'a' 的值設定為 [] (預設值)，並回傳這個空列表。
# 如果存在，它會回傳 'a' 當前的值。
# 接著，我們對回傳的列表執行 append(1) 操作。
d.setdefault('a', []).append(1)
print(f"d.setdefault('a', []).append(1) 後: {d}")
