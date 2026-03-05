from collections import deque

# 1. 雙端隊列 (deque) 的限額行為
q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3) 
print(f"deque 結果 (應只剩最後兩個): {list(q)}")

# 2. 類別屬性存取
class User:
    def __init__(self, user_id):
        self.user_id = user_id

u = User(42)
uid = u.user_id
print(f"User ID: {uid}")

# 3. 例外處理測試
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

print(f"is_int('123'): {is_int('123')}")
print(f"is_int('abc'): {is_int('abc')}")