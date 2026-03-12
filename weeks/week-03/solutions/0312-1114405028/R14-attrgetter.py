# R14. 物件排序 attrgetter（1.14）

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

users = [User(23), User(3), User(99)]
sorted(users, key=attrgetter('user_id'))
