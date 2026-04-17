# R14. 物件排序 attrgetter（1.14）
# =========================================================
# attrgetter 是 operator 模組中的函數，用於創建取屬性函數
# 類似於 itemgetter，但用於物件的屬性而非字典的鍵
# 比 lambda x: x.attr 更快、更簡潔
# =========================================================

from operator import attrgetter

# 定義使用者類別
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        # 方便調試和查看
        return f'User({self.user_id})'

# 建立使用者物件列表
users = [User(23), User(3), User(99)]

# =========================================================
# attrgetter('user_id'): 創建一個函數，功能等同於 lambda x: x.user_id
# 調用 attrgetter('user_id')(user) 會返回 user.user_id
# =========================================================

# 按 user_id 排序（升序）
# 返回：[User(3), User(23), User(99)]
sorted(users, key=attrgetter('user_id'))

# =========================================================
# attrgetter 的其他用法
# =========================================================

# 巢狀屬性：使用點號訪問
# attrgetter('address.city')(user) 返回 user.address.city

# 多屬性排序
# sorted(users, key=attrgetter('lastname', 'firstname'))

# =========================================================
# attrgetter vs itemgetter 的比較
# =========================================================

# itemgetter 適用於：字典、元組、列表等可索引的物件
# attrgetter 適用於：類別實例、有屬性的物件

# 假設上述 User 類別加入 name 屬性：
# class User:
#     def __init__(self, user_id, name):
#         self.user_id = user_id
#         self.name = name

# 排序方式：
# sorted(users, key=attrgetter('name'))          # 按 name 排序
# sorted(users, key=attrgetter('user_id'))       # 按 user_id 排序
# sorted(users, key=attrgetter('name', 'user_id'))  # 先 name 再 user_id

# =========================================================
# attrgetter 的效能優勢
# =========================================================

# attrgetter 使用 C 實現，比 lambda 快
# 當需要對大量物件進行排序時，attrgetter 是更好的選擇
# 同時，attrgetter 的語法更聲明式，程式碼意圖更清晰
