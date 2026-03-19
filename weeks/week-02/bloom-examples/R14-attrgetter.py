"""R14: attrgetter 用於物件屬性排序。"""

from operator import attrgetter


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return f'User(id={self.user_id}, name={self.name})'


users = [User(23, 'Amy'), User(3, 'Bob'), User(99, 'Carl')]
print('依 user_id 排序:', sorted(users, key=attrgetter('user_id')))
print('依 name 排序:', sorted(users, key=attrgetter('name')))
