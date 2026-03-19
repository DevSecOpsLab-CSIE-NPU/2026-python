# R18. namedtuple（1.18）

# namedtuple 可建立「具欄位名稱」的 tuple 類別，
# 同時保有 tuple 的輕量特性與不可變（immutable）行為。
from collections import namedtuple

# 建立 Subscriber 類別，包含兩個欄位：
# - addr: 電子郵件地址
# - joined: 加入日期
#
# 這行不會建立實例，而是先定義一個新的型別。
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 建立 Subscriber 實例，位置順序需與欄位定義一致。
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 透過屬性名稱直接讀取欄位值，可讀性比一般 tuple 用索引更好。
# 例如 sub[0] 也能取到 addr，但 sub.addr 通常更清楚。
sub.addr
print(sub.joined)

# 建立另一個 namedtuple 型別：Stock。
# 欄位分別是股票名稱、持有股數、單價。
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

# 建立一筆股票資料。
s = Stock('ACME', 100, 123.45)

# namedtuple 本身不可直接修改欄位，
# _replace(...) 會「回傳一個新的實例」，並套用指定欄位的新值。
# 這裡把 shares 從 100 改為 75，其他欄位保持不變。
s = s._replace(shares=75)
print(s)
