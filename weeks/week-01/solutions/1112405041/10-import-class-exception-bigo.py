# 10 模組、類別、例外與 Big-O 範例

from collections import deque

q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)
print(f"Deque: {list(q)}")

class User:
    def __init__(self, user_id):
        self.user_id = user_id

u = User(42)
uid = u.user_id

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

test_values = ["123", "abc", "45.6", "0"]
for val in test_values:
    print(f"is_int('{val}') = {is_int(val)}")

print(f"User ID: {uid}")
