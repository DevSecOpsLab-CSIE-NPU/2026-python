# 主題 10：模組、類別、例外與 Big-O - 正式版

from collections import deque

class User:
    """使用者類別"""
    def __init__(self, user_id):
        self.user_id = user_id

def demonstrate_deque():
    """展示 deque 的使用"""
    q = deque(maxlen=2)
    q.append(1)
    q.append(2)
    q.append(3)
    return list(q)

def is_int(val):
    """檢查值是否可以轉換為整數"""
    try:
        int(val)
        return True
    except ValueError:
        return False

def safe_divide(a, b):
    """安全的除法，避免除以零"""
    try:
        return a / b
    except ZeroDivisionError:
        return None

if __name__ == '__main__':
    u = User(42)
    print("使用者 ID:", u.user_id)
    print("Deque:", demonstrate_deque())
    print("是整數:", is_int('42'))
    print("安全除法:", safe_divide(10, 0))
