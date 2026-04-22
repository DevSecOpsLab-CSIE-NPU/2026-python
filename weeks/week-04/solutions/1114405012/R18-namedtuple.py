# R18. namedtuple（1.18）
# namedtuple 讓 tuple 同時擁有「不可變」與「欄位名稱可讀性」。

from collections import namedtuple

Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber("jonesy@example.com", "2012-10-19")

print("Subscriber 物件:", sub)
print("用屬性讀取 addr:", sub.addr)
print("用索引讀取 joined:", sub[1])

Stock = namedtuple("Stock", ["name", "shares", "price"])
s = Stock("ACME", 100, 123.45)
print("原始 Stock:", s)

# namedtuple 不可變，因此更新欄位要用 _replace 產生新物件。
s2 = s._replace(shares=75)
print("更新 shares 後的新 Stock:", s2)
print("原本 Stock 仍不變:", s)
