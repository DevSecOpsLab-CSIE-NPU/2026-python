# R12. Counter 統計 + most_common（1.12）

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)
top3 = word_counts.most_common(3)
print('詞頻統計:', word_counts)
print('出現最多前 3 名:', top3)

# 更新新資料後可累加次數
word_counts.update(['eyes', 'eyes'])
print('更新後 eyes 次數:', word_counts['eyes'])
print('更新後詞頻統計:', word_counts)
