# R14. 物件排序 attrgetter（1.14）
# 此程式示範如何使用 operator 模組中的 attrgetter 函數來對物件列表進行排序。
# attrgetter 允許我們指定物件的屬性作為排序鍵，而無需定義自訂的比較函數。

# 引入 operator 模組中的 attrgetter 函數
# attrgetter 用於從物件中提取指定的屬性值，常用於排序或作為鍵函數
from operator import attrgetter

# 定義一個簡單的 User 類別，用來表示使用者
# 這個類別只有一個屬性：user_id，用於識別使用者
class User:
    # __init__ 方法是類別的建構函數，用於初始化新建立的物件
    # 參數 user_id 是使用者的識別號碼
    def __init__(self, user_id):
        # 將傳入的 user_id 賦值給物件的 user_id 屬性
        self.user_id = user_id

# 建立一個包含三個 User 物件的列表
# 每個 User 物件的 user_id 分別是 23、3 和 99
# 這是我們要排序的資料
users = [User(23), User(3), User(99)]

# 使用 sorted 函數對 users 列表進行排序
# key 參數指定排序鍵，這裡使用 attrgetter('user_id') 來提取每個 User 物件的 user_id 屬性
# attrgetter 返回一個函數，該函數從物件中獲取指定的屬性值
# 排序結果將是按 user_id 升序排列的 User 物件列表
# 注意：sorted 函數返回一個新的排序列表，原列表 users 不會被修改
sorted(users, key=attrgetter('user_id'))
