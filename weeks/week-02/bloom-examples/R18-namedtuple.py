"""R18: namedtuple 建立輕量資料結構。"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print('訂閱者:', sub)
print('Email:', sub.addr)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
print('原始股票資料:', s)

# _replace 會回傳新物件，不會改動原本 s
s2 = s._replace(shares=75)
print('調整後股票資料:', s2)
