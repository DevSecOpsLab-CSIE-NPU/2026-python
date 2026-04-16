# R14. 物件排序 attrgetter（1.14）
#
# attrgetter 和 itemgetter 類似，但它是用來抓「物件屬性」：
# 1. 先定義好的屬性名稱，可以直接拿來當排序鍵。
# 2. 對自訂類別物件做排序時特別方便。
# 3. 若有多個屬性，也可以一起當作排序依據。

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

users = [User(23), User(3), User(99)]
sorted(users, key=attrgetter('user_id'))
