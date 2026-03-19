# R18. namedtuple（1.18）
#
# 觀念重點：
# - namedtuple 讓 tuple 既保有輕量特性，又可用「屬性名稱」存取欄位。
# - namedtuple 物件是不可變（immutable）的，更新值要用 _replace 產生新物件。

from collections import namedtuple

# 定義具名欄位的資料結構：Subscriber(addr, joined)
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 用屬性名稱讀取，語意比 sub[0] 更清楚。
sub.addr

# 另一個具名 tuple：Stock(name, shares, price)
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)

# 不能直接改 s.shares，需用 _replace 建立新物件。
s = s._replace(shares=75)
