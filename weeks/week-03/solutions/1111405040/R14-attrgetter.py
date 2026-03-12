"""
R14: attrgetter

attrgetter 與 itemgetter 類似，但取值對象是「物件屬性」。
"""

from operator import attrgetter


class User:
    """簡單使用者物件，只有 user_id 屬性。"""

    def __init__(self, user_id):
        self.user_id = user_id


users = [User(23), User(3), User(99)]

# 依 user_id 由小到大排序。
sorted(users, key=attrgetter("user_id"))
