# R14. 物件排序 attrgetter（1.14）

from operator import attrgetter

# ── 定義一個簡單的類別 ────────────────────────────────
class User:
    def __init__(self, user_id):
        # 這裡的 user_id 是物件的一個屬性 (Attribute)
        self.user_id = user_id

    def __repr__(self):
        # 為了方便查看排序結果，定義 repr 方法顯示物件內容
        return f'User({self.user_id})'

# ── 建立物件列表 ─────────────────────────────────────
# 原始順序：ID 分別為 23, 3, 99
users = [User(23), User(3), User(99)]

# ── 根據屬性排序 ─────────────────────────────────────
# sorted(..., key=attrgetter('user_id'))：
# 1. 它會自動走訪 users 列表中的每一個 User 物件。
# 2. 呼叫 attrgetter('user_id') 提取該物件的 user_id 屬性值。
# 3. 根據這個屬性值的大小進行排序。
#
# 結果：[User(3), User(23), User(99)]
sorted(users, key=attrgetter('user_id'))

# 補充：attrgetter 也支援多重排序
# 例如：sorted(users, key=attrgetter('last_name', 'first_name'))