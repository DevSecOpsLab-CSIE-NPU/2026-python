# R02 star unpack
# 目標：示範長度不固定序列的解包方式（* 會吃掉中間或前段多個值）。


def drop_first_last(grades):
    # 第一個與最後一個先拆出，中間全部由 middle 接住
    first, *middle, last = grades
    return sum(middle) / len(middle)


record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")
# phone_numbers 會是 list，收下剩下所有電話
name, email, *phone_numbers = record

# 星號也可放前面，取出最後一個當 current
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
