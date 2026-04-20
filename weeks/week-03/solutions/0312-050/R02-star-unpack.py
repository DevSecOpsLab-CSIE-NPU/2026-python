# 定義一個函式 drop_first_last，用於計算除了第一個和最後一個元素之外的平均值。
def drop_first_last(grades):
    first, *middle, last = grades
    print(f"  在 drop_first_last 函式中 - 原始成績: {grades}") # 顯示函式內部的原始成績。
    print(f"  解包後 - first: {first}, middle: {middle}, last: {last}") # 顯示解包後的 first, middle, last。
    return sum(middle) / len(middle)

# 測試 drop_first_last 函式。
student_grades = [60, 70, 80, 90, 100]
average_grade = drop_first_last(student_grades)
print(f"學生 {student_grades} 的中間成績平均值: {average_grade}\n") # 顯示計算出的平均值。

# 定義一個元組 record，包含姓名、電子郵件和多個電話號碼。
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# 顯示原始記錄元組。
print(f"原始記錄 record: {record}")
# 使用星號解包將 record 解包。
# name 會取得第一個元素 ('Dave')。
# email 會取得第二個元素 ('dave@example.com')。
# *phone_numbers 會將剩餘的所有元素收集成一個列表，賦值給 phone_numbers。
name, email, *phone_numbers = record
print(f"解包後 name: {name}, email: {email}, phone_numbers: {phone_numbers}\n") # 顯示解包後各變數的值。

# 定義一個列表，並使用星號解包來取得除了最後一個元素之外的所有元素。
data_list = [10, 8, 7, 1, 9, 5, 10, 3]
# 顯示原始列表。
print(f"原始列表 data_list: {data_list}")
# *trailing 會將除了最後一個元素之外的所有元素收集成一個列表。
# current 會取得最後一個元素。
*trailing, current = data_list
print(f"解包後 trailing: {trailing}, current: {current}") # 顯示解包後的 trailing 和 current。
