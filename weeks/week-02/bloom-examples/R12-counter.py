"""R12: Counter 計數與 most_common。"""

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes']
word_counts = Counter(words)

print('字詞統計:', word_counts)
print('前 3 常見字詞:', word_counts.most_common(3))

# update 可以把另一批資料加進來
word_counts.update(['eyes', 'eyes', 'look'])
print('更新後統計:', word_counts)
