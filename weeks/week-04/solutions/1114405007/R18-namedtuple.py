# R18. namedtuple（1.18）

from collections import namedtuple

# 建立具名欄位的 tuple 類別，可用屬性名稱存取資料
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 以欄位名稱讀取，比用索引更清楚
sub.addr

# 另一個 namedtuple 範例：表示股票資料
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)

# namedtuple 不可直接修改，需用 _replace 產生新物件
s = s._replace(shares=75)
