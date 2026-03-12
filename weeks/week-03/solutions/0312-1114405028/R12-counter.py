# R12. Counter 統計 + most_common（1.12）

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)
print("initial counts", word_counts)
print("most common 3", word_counts.most_common(3))

print("update with more 'eyes'")
word_counts.update(['eyes', 'eyes'])
print("updated counts", word_counts)

