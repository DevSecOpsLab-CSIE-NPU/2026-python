# ============================================================================
# R12. 計數器 Counter - 統計頻率和最常見元素（1.12）
# ============================================================================
# 本題展示 Counter 物件如何優雅地進行頻率統計和篩選。
# ============================================================================

from collections import Counter

print("【場景】統計文本中單詞出現頻率\n")

words = ['look', 'into', 'my', 'eyes', 'look']
print(f"單詞列表：{words}")
print(f"說明：'look' 和 'eyes' 各出現 1 次，'look' 出現 2 次\n")

print("=" * 50)
print("【基本用法】")
print("=" * 50)
print()

print("建立 Counter：")
word_counts = Counter(words)
print(f"word_counts = Counter(words)")
print(f"結果：{word_counts}\n")

print("查詢單個詞頻：")
print(f"word_counts['look'] = {word_counts['look']}")
print(f"word_counts['into'] = {word_counts['into']}")
print(f"word_counts['missing'] = {word_counts['missing']}  （不存在返回 0）\n")

print("=" * 50)
print("【most_common() - 排序")
print("=" * 50)
print()

print("取最常見的 3 個單詞：")
print()
top_3 = word_counts.most_common(3)
print(`word_counts.most_common(3) = {top_3}`)
for word, count in top_3:
    print(f"  '{word}': {count} 次")
print()

print("說明：")
print("  - 返回 (元素, 頻率) 的列表")
print("  - 按頻率遞減排序\n")

print("=" * 50)
print("【update() - 增量更新】")
print("=" * 50)
print()

print("添加新的單詞計數：")
print(f"原始：{word_counts}\n")

new_words = ['eyes', 'eyes']
print(f"word_counts.update({new_words})")
word_counts.update(new_words)
print(f"更新後：{word_counts}")
print()
print("說明：")
print("  - 'eyes' 從 1 變成 3（新增了 2）")
print("  - 已存在的計數累加\n")

print("=" * 50)
print("【Counter 的算術運算】")
print("=" * 50)
print()

c1 = Counter(['a', 'b', 'a', 'c', 'b', 'b'])
c2 = Counter(['a', 'b', 'd', 'd'])

print(f"c1 = {c1}")
print(f"c2 = {c2}\n")

print("加法（合併計數）：")
print(f"c1 + c2 = {c1 + c2}\n")

print("減法（移除計數）：")
print(f"c1 - c2 = {c1 - c2}  （移除 c2 中的元素）\n")

print("交集（取較小值）：")
print(f"c1 & c2 = {c1 & c2}\n")

print("並集（取較大值）：")
print(f"c1 | c2 = {c1 | c2}\n")

print("=" * 50)
print("【實戰應用】")
print("=" * 50)
print()

print("應用 1：找出稀罕詞（出現一次的）")
text = 'the quick brown fox jumps over the lazy dog'
words = text.split()
counts = Counter(words)
rare = [word for word, count in counts.items() if count == 1]
print(f"文本：'{text}'")
print(f"稀罕詞（出現 1 次）：{sorted(rare)}\n")

print("應用 2：消除連續重複的字符")
from collections import Counter

text = 'mississippi'
counts = Counter(text)
print(f"字符統計：{counts}")
for char in sorted(counts, key=counts.get, reverse=True):
    print(f"  '{char}': {counts[char]} 次\n")

print("=" * 50)
print("【Counter vs dict - 效能】")
print("=" * 50)
print("""
操作              Counter    dict        說明
─────────────────────────────────────────────────
計數              ✓✓         ✓✓          Counter 無需檢查
缺失鍵返回 0     ✓          ✗           Counter 安全
most_common()     ✓          N/A         Counter 獨有
算術運算          ✓          ✗           Counter 獨有
記憶體             稍多       ─           繼承自 dict

推薦：
  ✓ 頻率統計 → Counter
  ✓ 獲取排序結果 → Counter.most_common()
  ✓ 簡單計數 → 普通 dict + get()
""")

print("\n" + "=" * 50)
print("【最佳實踐】")
print("=" * 50)
print("""
✓ 使用 Counter 處理頻率統計
✓ 利用 most_common() 排序
✓ 使用 update() 累計計數
✓ 充分利用算術運算能力
✓ 缺失元素自動返回 0（安全）
""")
