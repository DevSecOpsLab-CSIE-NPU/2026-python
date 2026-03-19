# R18. namedtuple（1.18）

from collections import namedtuple

# 建立一個 namedtuple 類型：Subscriber
# 它會自動產生一個不可變（immutable）的 tuple-like 物件
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 建立一個 Subscriber 實例
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 可用屬性名稱存取欄位，比 tuple[0] 更易讀
sub.addr
# → 'jonesy@example.com'


# 再建立另一個 namedtuple 類型：Stock
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

# 建立 Stock 物件
s = Stock('ACME', 100, 123.45)

# namedtuple 是不可變的，因此不能直接修改欄位
# _replace() 會回傳一個「新的」 namedtuple，修改指定欄位
s = s._replace(shares=75)
# → Stock(name='ACME', shares=75, price=123.45)