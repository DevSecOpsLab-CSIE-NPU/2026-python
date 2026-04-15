# R14. 物件排序 attrgetter（1.14）

from operator import attrgetter

class User:
    def __init__(self, user_id):
    # 物件屬性，供 attrgetter 排序時使用
        self.user_id = user_id

users = [User(23), User(3), User(99)]
# 依 user_id 屬性由小到大排序
sorted(users, key=attrgetter('user_id'))
