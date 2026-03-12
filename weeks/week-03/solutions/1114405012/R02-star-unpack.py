# R2. 解包數量不固定：星號解包（1.2）

def drop_first_last(grades):
    # 星號解包：中間多個元素會收集成 list
    first, *middle, last = grades
    return sum(middle) / len(middle)

grades = [98, 92, 76, 88, 100]
avg_middle = drop_first_last(grades)
print('去頭去尾後平均:', avg_middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print('姓名:', name)
print('信箱:', email)
print('電話清單:', phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print('目前值:', current)
print('前面歷史值:', trailing)
