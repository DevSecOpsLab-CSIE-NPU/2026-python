# R14 attrgetter
# 目標：對物件列表依屬性排序。

from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id


users = [User(23), User(3), User(99)]
# 依 user_id 由小到大排序
sorted_users = sorted(users, key=attrgetter("user_id"))
