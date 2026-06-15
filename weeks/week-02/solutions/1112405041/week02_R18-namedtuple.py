# 【Bloom 階段：R - 記憶與基本操作】
# R18. 將名稱映射到序列元素 (namedtuple)
# August 的惡意提醒：在 Week 05 的遊戲模型中，Card(rank, suit) 非常適合用 namedtuple。
# 它比單純的 Tuple 更具可讀性（可以用 s.name 訪問），
# 且比完整 Class 更節省記憶體空間。

from collections import namedtuple

# 定義一個像類別一樣的 Tuple 結構
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 訪問方式：具名訪問 vs 索引訪問
print(f"Address: {sub.addr} (Index 0: {sub[0]})")

# August 重要提示：namedtuple 是不可變的 (Immutable)。
# 如果要「修改」，必須使用 ._replace() 方法，它會生成一個全新的物件。
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
# s.shares = 75  # ❌ 這會報錯
s = s._replace(shares=75) # ✅ 產生新物件

print(f"Updated Stock: {s}")
