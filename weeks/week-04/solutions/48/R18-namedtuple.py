# R18. namedtuple（1.18）
# 展示 namedtuple 如何提供具名欄位的輕量級結構

# 從 collections 模組導入 namedtuple
from collections import namedtuple

# 定義 Subscriber namedtuple：具有 addr（地址）和 joined（加入日期）兩個欄位
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# 建立 Subscriber 實例
sub = Subscriber('jonesy@example.com', '2012-10-19')
# 使用點符號存取欄位（比位置索引更易讀）
print("Subscriber 地址:", sub.addr)  # 結果：'jonesy@example.com'
print("完整 Subscriber:", sub)

# 定義 Stock namedtuple：具有 name、shares 和 price 三個欄位
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
# 建立 Stock 實例
s = Stock('ACME', 100, 123.45)
# namedtuple 是不可變的（immutable），使用 _replace() 建立新實例
print("原始 Stock:", Stock('ACME', 100, 123.45))
s = s._replace(shares=75)  # 建立新的 Stock 物件，shares 改為 75
print("修改後 Stock:", s)  # 結果：Stock(name='ACME', shares=75, price=123.45)
