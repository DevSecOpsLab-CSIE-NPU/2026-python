# R13. 字典列表排序 itemgetter（1.13）
# itemgetter 是 operator 模組中的一個函數，
# 用於從序列或映射物件中提取元素。
# 在排序時特別有用，可以指定排序鍵。

# 匯入 itemgetter 函數
from operator import itemgetter

# 創建一個包含字典的列表，每個字典代表一個用戶記錄
rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]

# 使用 itemgetter 按 fname（名字）欄位排序
# itemgetter('fname') 創建一個函數，該函數從字典中提取 'fname' 鍵的值
sorted_by_name = sorted(rows, key=itemgetter('fname'))

# 按 uid（用戶 ID）欄位排序
sorted_by_uid = sorted(rows, key=itemgetter('uid'))

# 可以同時指定多個鍵進行排序
# 首先按 uid 排序，如果 uid 相同，則按 fname 排序
sorted_by_uid_then_name = sorted(rows, key=itemgetter('uid', 'fname'))

# itemgetter 也可以用於提取元組的元素
# 例如，從元組列表中提取特定位置的元素
tuples = [('a', 1), ('b', 2), ('c', 3)]

# 按元組的第二個元素（索引 1）排序
sorted_tuples = sorted(tuples, key=itemgetter(1))
