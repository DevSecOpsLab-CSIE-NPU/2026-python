"""R14. 物件排序 attrgetter（1.14）

attrgetter() 和 itemgetter() 很像，差別在於：
1. itemgetter() 是從序列 / 字典項目中取值。
2. attrgetter() 是從物件屬性中取值。
3. 常用於 sorted / min / max 的 key 參數。
"""

from operator import attrgetter


class User:
    def __init__(self, user_id):
    # 建立物件時，把傳入的 user_id 存成物件屬性
        self.user_id = user_id

# 建立幾個 User 物件，user_id 各不相同
users = [User(23), User(3), User(99)]

# 依照 user_id 屬性排序
# attrgetter('user_id') 會回傳一個函式，這個函式會去讀取物件的 user_id
sorted(users, key=attrgetter('user_id'))
