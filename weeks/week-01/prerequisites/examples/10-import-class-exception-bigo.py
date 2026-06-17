# 10 模組、類別、例外與 Big-O（最低門檻）範例

from collections import deque

q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)  # 自動丟掉最舊

class User:
    def __init__(self, user_id):
        self.user_id = user_id

u = User(42)
uid = u.user_id

# 例外處理

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

# Big-O 只是觀念提示
# list.append 通常是 O(1)
# list 切片是 O(N)
