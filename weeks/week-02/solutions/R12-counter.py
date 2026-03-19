# R12. Counter 統計 + most_common（1.12）
# Counter 是 collections 模組中的一個類別，
# 用於統計可雜湊物件的出現次數。
# 它是一個特殊的字典，鍵是元素，值是出現次數。

# 匯入 Counter 類別
from collections import Counter

# 創建一個包含單詞的列表
words = ['look', 'into', 'my', 'eyes', 'look']

# 使用 Counter 統計單詞出現次數
# 創建一個 Counter 物件，自動計算每個單詞的出現頻率
word_counts = Counter(words)

# 使用 most_common 方法取得出現次數最多的前 3 個單詞
# 返回一個列表，包含 (元素, 次數) 的元組，按次數降序排列
word_counts.most_common(3)

# 使用 update 方法更新計數
# 將新元素添加到現有的計數中
word_counts.update(['eyes', 'eyes'])
