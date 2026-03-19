"""R18. namedtuple（1.18）

示範使用 collections.namedtuple 快速建立具命名欄位且不可變的資料結構。
"""

from collections import namedtuple

# Subscriber: 範例命名元組，包含 addr（電子郵件）與 joined（加入日期）
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 可以透過屬性名稱存取欄位
sub.addr

# Stock 範例：示範 _replace 用來建立修改後的新命名元組（namedtuple 是不可變的） 
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)
