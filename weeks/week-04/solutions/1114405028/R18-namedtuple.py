# R18. namedtuple（1.18）

from collections import namedtuple  # namedtuple：可用屬性名稱存取欄位的不可變輕量資料結構

# 定義 Subscriber 型別，有 addr 和 joined 兩個欄位
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub.addr  # 用名稱存取，比索引 sub[0] 更具可讀性

# 定義 Stock 型別，有 name、shares、price 三個欄位
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)  # _replace：回傳修改指定欄位的新實例，原物件不變（不可變性）
