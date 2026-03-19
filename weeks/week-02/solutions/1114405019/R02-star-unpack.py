# R2. 解包數量不固定：星號解包（1.2）

def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
