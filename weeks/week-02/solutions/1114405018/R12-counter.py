"""R12. Counter 統計 + most_common（1.12）

Counter 是 collections 模組提供的計數工具，常用來：
1. 統計字詞出現次數
2. 找出最常出現的元素
3. 快速更新統計結果
"""

from collections import Counter

# words 是一個字串列表，適合拿來做次數統計
words = ['look', 'into', 'my', 'eyes', 'look']

# Counter 會把每個元素出現的次數記錄下來
word_counts = Counter(words)

# most_common(n) 會回傳出現次數最高的前 n 個元素
# 結果格式是 [(元素, 次數), ...]
word_counts.most_common(3)

# update() 可以把新的元素統計進來，次數會在原本基礎上累加
# 這裡把 'eyes' 再加兩次
word_counts.update(['eyes', 'eyes'])
