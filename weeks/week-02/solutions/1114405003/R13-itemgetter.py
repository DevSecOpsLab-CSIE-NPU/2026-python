"""
R13：itemgetter 進行字典列表排序

學習目標：
1. 了解 itemgetter("欄位") 作為排序鍵。
2. 了解 itemgetter 支援多欄位排序（主鍵/次鍵）。
3. 比較 itemgetter 與 lambda 在可讀性上的差異。
"""

from operator import itemgetter


def main():
    print("=== R13 itemgetter 排序 ===")

    rows = [
        {"fname": "Brian", "lname": "Jones", "uid": 1003},
        {"fname": "David", "lname": "Beazley", "uid": 1002},
        {"fname": "John", "lname": "Cleese", "uid": 1001},
        {"fname": "Big", "lname": "Jones", "uid": 1004},
    ]
    print("[原始 rows]", rows)

    by_fname = sorted(rows, key=itemgetter("fname"))
    by_uid = sorted(rows, key=itemgetter("uid"))
    by_uid_fname = sorted(rows, key=itemgetter("uid", "fname"))

    print("[例1] 依 fname 排序 =", by_fname)
    print("[例2] 依 uid 排序 =", by_uid)
    print("[例3] 依 uid, fname 排序 =", by_uid_fname)


if __name__ == "__main__":
    main()
