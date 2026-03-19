# R18. 具名元組 namedtuple（1.18）
# 說明：提供比普通 tuple 更好的閱讀性，可以用「.屬性名」來存取資料。

from collections import namedtuple

# 定義一個 Subscriber 型別
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 可以透過屬性名稱存取，不用記索引位置
print(sub.addr)   # jonesy@example.com
print(sub.joined) # 2012-10-19

# 注意：namedtuple 是不可變的 (immutable)，若要修改需使用 _replace()
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
# 修改並產生一個新的實例
s = s._replace(shares=75)