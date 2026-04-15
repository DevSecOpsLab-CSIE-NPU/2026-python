"""
R14：attrgetter 進行物件列表排序

學習目標：
1. 了解 attrgetter("屬性名") 能直接讀取物件屬性作為排序鍵。
2. 了解它在物件排序時，比 lambda 更簡潔。
"""

from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"User({self.user_id})"


def main():
    print("=== R14 attrgetter 排序 ===")

    users = [User(23), User(3), User(99)]
    print("[原始 users]", users)

    sorted_users = sorted(users, key=attrgetter("user_id"))
    print("[例1] 排序鍵 attrgetter('user_id')")
    print("[例2] 排序後 =", sorted_users)


if __name__ == "__main__":
    main()
