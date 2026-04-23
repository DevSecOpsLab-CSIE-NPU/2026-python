# 【Bloom 階段：R - 記憶與基本操作】
# R12. 序列中出現次數最多的元素 (Counter)
# August 的惡意提醒：這是 Week 02 Task 3 的核心工具。
# 想要找出出現頻率最高的動作？不要手寫迴圈找 max，
# 直接用 Counter 的 .most_common(1) 就能優雅解題。

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'the', 'eyes', 'look']
# 一行完成詞頻統計
word_counts = Counter(words)

# 取得出現次數最多的前 3 名
top_three = word_counts.most_common(3)
print(f"Top 3 words: {top_three}")

# 支持動態更新計數
word_counts.update(['eyes', 'eyes'])
print(f"Updated 'eyes' count: {word_counts['eyes']}")

# August 惡意筆記：Counter 還支持數學運算（+ , -）來結合多組數據，
# 在處理多天日誌合併（Week 07）時非常有威力。
