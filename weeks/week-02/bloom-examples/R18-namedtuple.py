"""
R18: namedtuple

讓 tuple 同時保有名稱與位置索引。
"""

from collections import namedtuple


Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber("jonesy@example.com", "2012-10-19")

# 可以像物件一樣用名稱取值。
sub.addr

Stock = namedtuple("Stock", ["name", "shares", "price"])
s = Stock("ACME", 100, 123.45)

# namedtuple 本身不可修改，若要更新可用 _replace 建立新物件。
s = s._replace(shares=75)
