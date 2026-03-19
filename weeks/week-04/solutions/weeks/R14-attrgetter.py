# R14. 物件排序 attrgetter（1.14）

from operator import attrgetter

class User:
    def __init__(self, user_id):
        # 每個 User 物件都有一個 user_id 屬性
        self.user_id = user_id

# 建立一個 User 物件列表
users = [User(23), User(3), User(99)]

# 使用 attrgetter('user_id') 取得物件的屬性作為排序依據
# sorted() 會依照 user_id 由小到大排序
sorted(users, key=attrgetter('user_id'))