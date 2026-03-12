# R14. 物件排序 attrgetter（1.14）

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'User({self.user_id})'

users = [User(23), User(3), User(99)]

# 用物件屬性 user_id 排序
users_sorted = sorted(users, key=attrgetter('user_id'))
smallest_user = min(users, key=attrgetter('user_id'))

print('排序前:', users)
print('排序後:', users_sorted)
print('user_id 最小的物件:', smallest_user)
