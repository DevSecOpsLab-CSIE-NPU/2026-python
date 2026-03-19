# R18. namedtuple（1.18）

from collections import namedtuple

# 定義具名 tuple：欄位有 addr, joined
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 建立資料後可以用屬性方式讀取，比純 tuple 可讀性高
sub = Subscriber('jonesy@example.com', '2012-10-19')
subscriber_email = sub.addr

# 另一個具名 tuple 範例
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)

# namedtuple 不可變，修改時用 _replace 產生新物件
s = s._replace(shares=75)
