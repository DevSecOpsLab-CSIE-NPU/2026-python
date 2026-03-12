# R12. Counter 統計 + most_common（Determining the Most Frequently Occurring Items）—— Python Cookbook 1.12

from collections import Counter

# ── 建立 Counter ──────────────────────────────────────────
# Counter 是 dict 的子類別，key = 元素，value = 出現次數
# 傳入任何可迭代物件即可初始化
words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)
# word_counts = Counter({'look': 2, 'into': 1, 'my': 1, 'eyes': 1})

# ── most_common(n) ────────────────────────────────────────
# 回傳出現次數最多的 n 個 (元素, 次數) tuple，由高到低排列
# 底層使用 heapq.nlargest，效率 O(k log n)
word_counts.most_common(3)
# → [('look', 2), ('into', 1), ('my', 1)]（次序相同的元素順序不保證）

# ── update：累加計數 ──────────────────────────────────────
# 與 dict.update 不同：Counter.update 是「加法合併」而非「覆蓋」
word_counts.update(['eyes', 'eyes'])   # eyes: 1 → 3
# word_counts = Counter({'look': 2, 'eyes': 3, 'into': 1, 'my': 1})

# ── 其他常用操作 ─────────────────────────────────────────
# word_counts['look']  → 2（不存在的 key 回傳 0，不會 KeyError）
# word_counts + Counter(['look'])  → 計數相加
# word_counts - Counter(['look'])  → 計數相減（結果 < 0 的項目會被移除）
