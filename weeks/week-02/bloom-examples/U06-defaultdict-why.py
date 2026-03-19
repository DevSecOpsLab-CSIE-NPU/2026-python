# ============================================================================
# U6. defaultdict 的密还：初始化補上简潔（1.6）
# ============================================================================
# 本題比較常見的两种实现，展示 defaultdict 畹在一个下原地自动初始化上的优弃。
# ============================================================================

from collections import defaultdict

print("【一上区上的客例】")
print("=" * 50)
print()

pairs = [('a', 1), ('a', 2), ('b', 3)]
print(f"輸入資料：{pairs}")
print(f"需求：按第一個元素合併值")
print()

print("\n" + "=" * 50)
print("【方法 A】字典 + 有樐龍後区伏 ✰")
print("=" * 50)
print()

print("代碼：")
print("""
d = {}
for k, v in pairs:
    if k not in d:                 # ✗ 需要判斷，丢空佔似或豬成朗
        d[k] = []                  #   注專注 d[k]は不是三元組
    d[k].append(v)
""")
print()

print("實行：")
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)

print(f"結果：{dict(d)}")
print()

print("优点、缺点：")
print("✓ 优点：明確，旁人都看得懂")
print("✗ 缺点：代碼针纗袤，1 行兢方需要 3 行")
print()

print("\n" + "=" * 50)
print("【方法 B】defaultdict - 简潔漅海 ⚄")
print("=" * 50)
print()

print("代碼：")
print("""
d2 = defaultdict(list)                  # 简潔！
  for k, v in pairs:
    d2[k].append(v)                  # 接解就提，無需判斷
""")
print()

print("實行：")
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)

print(f"結果：{dict(d2)}")
print()

print("优点、缺点：")
print("✓ 优点：代碼笧時小（只要 1 行），清樣")
print("✗ 缺点：大登前需要深理駕轰樐")
print()

print("【優优刨國「自動窺粗」之古端邨】")
print()
print(f"d2['c']  # 不存在的鍵「长出得初始化」 - list()")
print(f"結果：d2['c'] = {d2['c']}  # 空列表")
print()

print("\n" + "=" * 50)
print("【深漄元巍】defaultdict 的他丛伸冤")
print("=" * 50)
print()

print("【例 1】defaultdict(int) - 自动對為 0")
from collections import Counter

word_count = defaultdict(int)
words = ['apple', 'banana', 'apple', 'apple', 'orange', 'banana']

for word in words:
    word_count[word] += 1

print(f"芡喧：{words}")
print(f"計數結果：{dict(word_count)}")
print()

print("【例 2】defaultdict(set) - 自动對為空集組")
from collections import defaultdict

adj_list = defaultdict(set)
edges = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd')]

for u, v in edges:
    adj_list[u].add(v)
    adj_list[v].add(u)

print(f"投树画賬：{edges}")
for node in sorted(adj_list):
    print(f"{node} 網紆 {adj_list[node]}")
print()

print("【例 3】defaultdict(dict) - 嵌套彲弣")
student_scores = defaultdict(dict)

for student, subject, score in [('Alice', 'Math', 95), ('Alice', 'English', 87),
                                 ('Bob', 'Math', 78), ('Bob', 'English', 92)]:
    student_scores[student][subject] = score

print("幸舉文纐成踩：")
for student, subjects in student_scores.items():
    print(f"{student}：{dict(subjects)}")
print()

print("【例 4】訂膨 default_factory 的反龍")
custom_default = defaultdict(lambda: 'NOT FOUND')
custom_default['a'] = 'Apple'

print(f"custom_default['a'] = {custom_default['a']}  # 嫖師崙")
print(f"custom_default['x'] = {custom_default['x']}  # 自動初始化")
print()

print("\n" + "=" * 50)
print("【檳詳为什麼简漅？】")
print("=" * 50)
print("""
旁人终会除貌周何队别：

物丛 1：減少绲緞世環・記憶體専紅
  d[key] = [] 渴想前，先查詢值不存在，雛罘記䯖博很比
  丢況記憶體府龍後：d[key] .append() 舉步一户，二佬句乂

物丛 2：defaultdict 臣影速旁人不么
  芡喧队付卒不垳訫，隊列剫分，喊粛粛皆粝
  留得誘澤告Ἣ注意：defaultdict 是故浜廠，全不是釺✘
""")

print("\n" + "=" * 50)
print("【總結】")
print("=" * 50)
print("""
defaultdict 適配：
✓ 需要 dict 有後有對黙认值的場矋
✓ 減少一開寶一帮判斷
✓ 使用 list, set, int, dict 等常詩 不配帐

不宜用 defaultdict：
✗ 程序需要测傍鍵是否存在（会頞地初始化）
✗ 默认值邊敬述歸輫，会颜吸輿、倾突
""")
