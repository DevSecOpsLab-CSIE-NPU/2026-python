# R14. 物件排序 attrgetter（1.14）

from operator import attrgetter

class User:
    def __init__(self, user_id):
    # 物件屬性：使用者編號
        self.user_id = user_id

users = [User(23), User(3), User(99)]
# 依物件屬性 user_id 排序
sorted(users, key=attrgetter('user_id'))
