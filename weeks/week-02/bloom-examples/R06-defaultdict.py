# ============================================================================
# R6. 多值字典 - defaultdict 與 setdefault（1.6）
# ============================================================================
# 本題展示兩種方法建立「一個鍵對應多個值」的字典結構。
# ============================================================================

from collections import defaultdict

print("【場景】統計每個字母出現的次數\n")

letters = ['a', 'b', 'a', 'c', 'b', 'a']
print(f"字母列表：{letters}\n")

print("=" * 50)
print("【方法 1】defaultdict(list)")
print("=" * 50)
print()

print("代碼：")
print("""
d = defaultdict(list)
for letter in letters:
    d[letter].append(letter)
""")
print()

d = defaultdict(list)
for letter in letters:
    d[letter].append(letter)

print(f"結果：")
for key, values in sorted(d.items()):
    print(f"  '{key}': {values}")
print()

print("說明：")
print("  - 初次訪問 d['a'] 時，自動創建 []")
print("  - 不需要檢查鍵是否存在")
print("  - 代碼簡潔優雅\n")

print("=" * 50)
print("【方法 2】defaultdict(set)")
print("=" * 50)
print()

print("如果只關心值的存在性（去重）：")
print()

d = defaultdict(set)
for letter in letters:
    d[letter].add(letter)

print(f"結果：")
for key, values in sorted(d.items()):
    print(f"  '{key}': {values}")
print()

print("說明：")
print("  - 使用 set 存儲，自動去重")
print("  - 適合需要唯一值的場景\n")

print("=" * 50)
print("【方法 3】setdefault(key, default)")
print("=" * 50)
print()

print("普通字典也能實現，但需要手動檢查：")
print()

print("代碼：")
print("""
d = {}
for letter in letters:
    d.setdefault(letter, []).append(letter)
""")
print()

d = {}
for letter in letters:
    d.setdefault(letter, []).append(letter)

print(f"結果：")
for key, values in sorted(d.items()):
    print(f"  '{key}': {values}")
print()

print("說明：")
print("  - setdefault(key, default) 回傳現有值或預設值")
print("  - 一行代碼完成檢查和設置")
print("  - 但不如 defaultdict 簡潔\n")

print("=" * 50)
print("【defaultdict 的其他用法】")
print("=" * 50)
print()

print("usecase 1：defaultdict(int) - 計數器")
counts = defaultdict(int)
for letter in letters:
    counts[letter] += 1
print(f"計數結果：{dict(counts)}\n")

print("usecase 2：defaultdict(dict) - 嵌套字典")
students = defaultdict(dict)
students['Alice']['Math'] = 95
students['Alice']['English'] = 87
students['Bob']['Math'] = 78
print(f"嵌套結果：")
for name, scores in students.items():
    print(f"  {name}: {scores}\n")

print("=" * 50)
print("【defaultdict vs 普通字典")
print("=" * 50)
print("""
特性              defaultdict(T)       普通 dict
─────────────────────────────────────────────────
默認值            自動創建             KeyError
代碼簡潔度        ✓ 很簡潔              ✗ 需檢查
性能              ✓ O(1)                ✓ O(1)
適用場景          多值場景              單值場景

推薦：
  ✓ 多值字典 → defaultdict
  ✓ 計數器   → Counter（更專業）
  ✓ 單值字典 → 普通 dict
""")
