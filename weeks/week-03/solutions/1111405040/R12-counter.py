"""
R12: Counter 計數器

Counter 用來統計元素出現次數，並快速取得高頻項目。
"""

from collections import Counter

words = ["look", "into", "my", "eyes", "look"]

# 建立詞頻統計。
word_counts = Counter(words)

# most_common(3) 取得前 3 個高頻詞與次數。
word_counts.most_common(3)

# update 可把新資料批次累加到既有計數。
word_counts.update(["eyes", "eyes"])
