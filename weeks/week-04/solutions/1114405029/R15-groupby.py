# 匯入 itertools 模組中的 groupby 函式
# groupby 的功能是：把「連續且條件相同」的資料分成同一組
from itertools import groupby

# 匯入 operator 模組中的 itemgetter 函式
# itemgetter('date') 可以快速取出每筆資料中 key 為 'date' 的值
from operator import itemgetter

# 建立一個串列 rows
# 串列中的每一個元素都是字典(dict)
# 每個字典代表一筆資料，裡面有日期(date)與地址(address)
rows = [
    {'date': '07/01/2012', 'address': '...'},
    {'date': '07/02/2012', 'address': '...'}
]

# 先依照 'date' 這個欄位進行排序
# 這一步非常重要，因為 groupby 只能把「相鄰且相同」的資料分在一起
# 如果資料沒有先排序，即使日期相同，也可能因為位置不連續而被分成不同組
rows.sort(key=itemgetter('date'))

# 印出排序後的原始資料，方便觀察排序結果
print("排序後的資料：")
for row in rows:
    print(row)

print()  # 空一行，讓輸出結果更清楚

# 使用 groupby 依照 'date' 進行分組
# date 會接住目前這一組的日期
# items 會接住屬於這個日期的所有資料（是一個可迭代物件）
for date, items in groupby(rows, key=itemgetter('date')):
    # 印出目前這一組的日期
    print("日期：", date)

    # 逐筆取出這一組中的資料
    for i in items:
        # 印出該日期底下的每一筆資料
        print("資料：", i)

    # 每一組資料結束後空一行，讓分組結果更容易閱讀
    print()