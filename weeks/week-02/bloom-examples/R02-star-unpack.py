"""R02: 星號解包 (* unpacking) 範例。"""


def drop_first_last(grades):
    # 使用 *middle 收集中間所有成績
    first, *middle, last = grades
    return (first, middle, last, sum(middle) / len(middle))


result = drop_first_last([98, 85, 76, 92, 88])
print('首分/中間/尾分/中間平均:', result)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phones = record
print('姓名:', name)
print('Email:', email)
print('電話清單:', phones)

# *trailing 收集前面全部元素，最後一個放到 current
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print('前段資料:', trailing)
print('目前值:', current)
