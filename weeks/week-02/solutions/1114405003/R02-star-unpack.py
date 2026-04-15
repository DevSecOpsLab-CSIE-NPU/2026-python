"""
R02：星號解包（* Unpacking）

學習目標：
1. 當序列長度不固定時，使用 * 一次接住多個元素。
2. 了解 first, *middle, last 的常見拆法。
3. 了解 * 也能放在左邊，拿到「除了最後一個以外」的資料。
"""


def drop_first_last(grades):
    first, *middle, last = grades
    print("  drop_first_last 拆解 -> first:", first, "middle:", middle, "last:", last)
    return sum(middle) / len(middle)


def main():
    print("=== R02 星號解包 ===")

    grades = [98, 87, 91, 84, 100]
    print("[例1] 原始成績 =", grades)
    avg = drop_first_last(grades)
    print("[例1] 去頭去尾後平均 =", avg)

    record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")
    name, email, *phone_numbers = record
    print("[例2] record =", record)
    print("[例2] 姓名:", name)
    print("[例2] 信箱:", email)
    print("[例2] 其餘全部電話 phone_numbers:", phone_numbers)

    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    print("[例3] 最後一筆 current =", current)
    print("[例3] 前面所有值 trailing =", trailing)


if __name__ == "__main__":
    main()
