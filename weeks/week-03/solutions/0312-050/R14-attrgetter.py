# R14. 物件排序 attrgetter（1.14）

# 從 operator 模組導入 attrgetter 函式，它用於快速從物件中提取指定「屬性 (attribute)」的值。
from operator import attrgetter

# 定義一個 User 類別，代表一個使用者物件。
class User:
    # 初始化方法，在建立 User 物件時被呼叫。
    def __init__(self, user_id):
        # 將傳入的 user_id 儲存為物件的屬性。
        self.user_id = user_id

    # 定義 __repr__ 方法，決定物件被轉成字串或在列表中印出時的顯示格式。
    # 加上這個方法，列印時才不會只看到一堆無法辨識的記憶體位址。
    def __repr__(self):
        return f"User({self.user_id})"

print("--- 建立 User 物件列表 ---")
# 建立一個包含三個 User 物件的列表 users，它們的 user_id 分別為 23, 3, 99。
users = [User(23), User(3), User(99)]
# 顯示原始未排序的使用者列表。
print(f"原始 users 列表:\n  {users}\n")

print("--- 使用 attrgetter 進行排序 ---")
# 使用 sorted() 函式對 users 列表進行排序。
# key=attrgetter('user_id') 表示排序的依據是每個 User 物件中的 'user_id' 屬性。
# 這在邏輯上完全等同於使用 key=lambda u: u.user_id，但 attrgetter 是在底層 C 語言執行，速度更快且語意更清晰。
sorted_users = sorted(users, key=attrgetter('user_id'))

# 顯示根據 user_id 排序後的結果。
print(f"根據 'user_id' 排序後的列表:\n  {sorted_users}")
