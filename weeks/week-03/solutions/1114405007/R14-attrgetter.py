# R14: attrgetter
# 觀念：attrgetter 與 itemgetter 類似，但用於「物件屬性」而不是字典索引。

from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id


users = [User(23), User(3), User(99)]

# 依 user_id 屬性排序
sorted(users, key=attrgetter('user_id'))
