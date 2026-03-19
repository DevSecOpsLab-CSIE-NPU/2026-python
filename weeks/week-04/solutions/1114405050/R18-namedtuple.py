# R18. namedtuple（1.18）
"""
本範例說明 Python 標準庫 collections.namedtuple 的使用方式。

namedtuple 可以用簡潔的方式定義一個不可變（immutable）的物件類型，
同時保有類似元組（tuple）的記憶體效率，以及可用屬性存取欄位的便利性。

重點：
- namedtuple 定義的是「類型」，類似輕量級的 class
- 建立的執行個體是不可變的（immutable），如需修改需使用 _replace()
- 可透過 index 或名稱存取欄位 (例如 obj[0] 或 obj.field)
"""

from collections import namedtuple

# 定義一個 Subscriber 類型，包含 addr 與 joined 兩個欄位
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 建立一個 Subscriber 實例
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 可以像存取屬性一樣取得欄位的值
sub.addr

# 再舉一個範例：定義股票資料結構
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

# 建立 Stock 實例
s = Stock('ACME', 100, 123.45)

# namedtuple 是不可變的；若要“修改”欄位，需要建立新的實例
# _replace 會回傳一個新實例，且只修改指定的欄位
s = s._replace(shares=75)
