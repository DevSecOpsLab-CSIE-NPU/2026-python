# R18. namedtuple（1.18）

from collections import namedtuple

# ── 定義具名元組類型 ──────────────────────────────────
# 創建一個名為 'Subscriber' 的新類別，並定義其欄位名稱為 'addr' 與 'joined'
# 這讓元組中的位置 (index) 擁有了語意化的名稱
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 實例化一個 Subscriber 物件
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 透過「屬性名稱」存取資料，這比使用索引（如 sub[0]）更直觀且不易出錯
sub.addr  # 結果：'jonesy@example.com'

# ── namedtuple 的不可變性與替換 ───────────────────────
# 定義另一個 Stock 結構，包含名稱、股數、價格
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)

# 重要特性：namedtuple 與一般 tuple 一樣是「不可變的 (Immutable)」
# 你不能直接修改 s.shares = 75，這會拋出 AttributeError。

# 如果需要「修改」數值，必須使用 ._replace() 方法
# 該方法會回傳一個「全新的具名元組實體」，並將指定的欄位替換為新值
s = s._replace(shares=75)
# 現在 s 是一個新的 Stock 實體，shares 為 75