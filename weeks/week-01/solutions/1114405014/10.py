# 10.py - 使用 collections.deque、類別定義與簡單錯誤檢查
from collections import deque

# 設定最大長度的 deque，超過時會自動丟棄最舊元素
q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)    # 1 會被丟棄

class User:
    def __init__(self, user_id):
        self.user_id = user_id

u = User(42)
uid = u.user_id  # 存取屬性

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False    # 無法轉換則返回 False

print(f"q = {q}")
print(f"uid = {uid}")
print(f"is_int('123') = {is_int('123')}")
print(f"is_int('abc') = {is_int('abc')}")