# R6. 多值字典 defaultdict / setdefault（1.6）
# defaultdict 是 collections 模組中的一個類別，
# 它繼承了普通的 dict，但提供了一個工廠函數來自動處理缺失的鍵。
# 當訪問不存在的鍵時，它會自動創建一個預設值，而不是拋出 KeyError。

# 匯入 defaultdict 類別
from collections import defaultdict

# 創建一個 defaultdict，其預設值為空列表
# 當訪問不存在的鍵時，會自動創建一個新的空列表
d = defaultdict(list)

# 向鍵 'a' 添加元素，由於 'a' 不存在，會自動創建一個空列表，然後添加 1
d['a'].append(1)

# 再次向鍵 'a' 添加元素，現在 'a' 已經存在，直接添加 2
d['a'].append(2)

# 創建一個 defaultdict，其預設值為空集合
# 集合用於儲存唯一的值
d = defaultdict(set)

# 向鍵 'a' 添加元素，自動創建空集合並添加 1
d['a'].add(1)

# 再次添加元素 2 到鍵 'a'
d['a'].add(2)

# 使用普通的字典和 setdefault 方法
# setdefault 方法如果鍵不存在，則設定預設值並返回它
d = {}

# 如果 'a' 不存在，設定為空列表 []，然後向該列表添加 1
d.setdefault('a', []).append(1)
