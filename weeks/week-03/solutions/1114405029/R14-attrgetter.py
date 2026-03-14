# R14. 物件排序 attrgetter（1.14）
#
# 這份程式示範：
# - 當資料是「物件列表」時，如何依物件屬性排序
# - 使用 operator.attrgetter 讓 key 寫法更簡潔

from operator import attrgetter


class User:
    def __init__(self, user_id):
        # 每個 User 物件都有一個 user_id 屬性
        self.user_id = user_id


# 建立三個 User 物件
users = [User(23), User(3), User(99)]

# 依 user_id 由小到大排序
# attrgetter('user_id') 可理解成：lambda u: u.user_id
# 排序後順序會是 user_id: 3, 23, 99
# 注意：sorted(...) 會回傳新列表，不會改動原本 users 順序。
sorted(users, key=attrgetter('user_id'))


# 讀懂這份程式的步驟：
# 1. 先確認排序對象是物件（不是 dict）。
# 2. 看 key 指到哪個屬性（這裡是 user_id）。
# 3. sorted 預設升冪排序（小到大）。
# 4. attrgetter 是取屬性的簡潔工具，概念與 lambda 版本相同。
