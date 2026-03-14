# R12. Counter 統計 + most_common（1.12）
#
# Counter 是 collections 提供的「計數字典」：
# - key 是元素
# - value 是出現次數
# 可以把它想成一個專門做頻率統計的 dict。

from collections import Counter

# 一段詞彙資料（可重複）
words = ['look', 'into', 'my', 'eyes', 'look']

# 直接統計每個單字出現次數
# 結果概念上類似：
# Counter({'look': 2, 'into': 1, 'my': 1, 'eyes': 1})
word_counts = Counter(words)

# most_common(n)：取出前 n 個高頻元素
# 回傳型態是 list[tuple]，每個 tuple 是 (元素, 次數)
# most_common(3) 例： [('look', 2), ('into', 1), ('my', 1)]
# 注意：同次數之間的順序，可能依內部規則/出現順序而定。
word_counts.most_common(3)


# update(iterable)：把新資料再累加進既有計數
# 這裡新增兩個 'eyes'，所以 eyes 計數會 +2（由 1 變 3）
word_counts.update(['eyes', 'eyes'])


# 讀懂這份程式的步驟：
# 1. 先把 Counter 當成「自動加總次數」的 dict。
# 2. 建立 Counter 時會先跑一次完整統計。
# 3. most_common 用來看排名，不會改變原資料。
# 4. update 會在原 Counter 上累加，是「增量統計」常用操作。
