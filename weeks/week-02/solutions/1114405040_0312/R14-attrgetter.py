# R14. 物件排序 attrgetter（Sorting Objects Without Native Comparison Support）—— Python Cookbook 1.14

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'User({self.user_id})'

# ── attrgetter 作為 key 函式 ──────────────────────────────
# attrgetter('user_id') 等同於 lambda u: u.user_id，
# 用於「依物件屬性排序」的場景（物件沒有定義 __lt__ 等比較運算子時特別有用）
users = [User(23), User(3), User(99)]

sorted(users, key=attrgetter('user_id'))
# → [User(3), User(23), User(99)]

# ── 與 itemgetter 的差異 ──────────────────────────────────
# itemgetter  →  適合 dict / tuple / list（用 [] 取值）
# attrgetter  →  適合自訂類別物件（用 . 取屬性）

# ── 多屬性排序 ────────────────────────────────────────────
# attrgetter('last_name', 'first_name') 先依姓排，姓相同再依名排
# （等同於 lambda u: (u.last_name, u.first_name)）

# ── 降序排列 ─────────────────────────────────────────────
# sorted(users, key=attrgetter('user_id'), reverse=True)
# → [User(99), User(23), User(3)]
