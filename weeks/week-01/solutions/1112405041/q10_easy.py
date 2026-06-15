# 主題 10：模組、類別、例外與 Big-O - 簡易教學版

# 模組（module）的使用
from collections import deque

q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)                # 自動丟掉最舊的元素 1，變成 [2, 3]
print(f"Deque: {list(q)}")

# 類別（class）與物件
class User:
    def __init__(self, user_id):
        self.user_id = user_id

u = User(42)
uid = u.user_id
print(f"使用者 ID: {uid}")

# 例外處理（try / except）
def is_int(val):
    """檢查是否可以轉換為整數"""
    try:
        int(val)
        return True
    except ValueError:
        return False

print(f"'42' 是整數嗎？ {is_int('42')}")       # True
print(f"'abc' 是整數嗎？ {is_int('abc')}")     # False

# 其他例外類型
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

# Big-O 複雜度觀念（只是認識）
# O(1)：常數時間（deque append）
# O(N)：線性時間（遍歷列表）
# O(log N)：對數時間（二分搜尋）
# O(N log N)：線性對數時間（合併排序）
# O(N^2)：平方時間（冒泡排序）

print("\nBig-O 複雜度:")
print("- list.append: O(1)")
print("- list slicing: O(N)")
print("- deque append: O(1)")
print("- sorted: O(N log N)")
