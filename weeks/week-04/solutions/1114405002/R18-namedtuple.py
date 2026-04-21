# R18 namedtuple 使用說明
# 重點：namedtuple 兼具 tuple 輕量與屬性名稱可讀性。

from collections import namedtuple

Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber("jonesy@example.com", "2012-10-19")

# 可用屬性名稱存取，語意比索引更清楚。
sub.addr

Stock = namedtuple("Stock", ["name", "shares", "price"])
s = Stock("ACME", 100, 123.45)

# namedtuple 是不可變物件，更新欄位請用 _replace 產生新物件。
s = s._replace(shares=75)
