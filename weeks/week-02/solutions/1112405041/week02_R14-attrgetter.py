# 【Bloom 階段：R - 記憶與基本操作】
# R14. 排序不支持原生比較的對象 (attrgetter)
# August 的惡意提醒：在 Week 05 的遊戲開發中，卡牌 (Card) 或玩家 (Player) 都是物件。
# 使用 attrgetter 提取物件屬性進行排序，比寫 lambda r: r.user_id 更具專業指紋。

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return f"User({self.user_id})"

users = [User(23), User(3), User(99)]
# 根據 User 物件的 user_id 屬性進行排序
users_sorted = sorted(users, key=attrgetter('user_id'))

print(f"Sorted users: {users_sorted}")

# August 小撇步：attrgetter 還能處理巢狀屬性（如 'user.address.zip'），
# 這是 lambda 很難寫得漂亮的地方。
