# R15. 分組 groupby（1.15）
# 展示如何使用 groupby 函數將相同日期的記錄分組

# 從 itertools 模組導入 groupby 函數，用於將連續的相同元素分組
from itertools import groupby
# 從 operator 模組導入 itemgetter，用於快速提取字典中的特定鍵值
from operator import itemgetter

# 建立包含字典元素的列表，每個字典有 'date' 和 'address' 兩個鍵
rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]

# 根據 'date' 鍵對列表進行排序，因為 groupby 需要資料先排序好
# groupby 只能將連續相同的元素組合在一起
rows.sort(key=itemgetter('date'))

# 使用 groupby 根據 'date' 值進行分組
# date: 當前組的日期值
# items: 該日期組內所有記錄的迭代器
for date, items in groupby(rows, key=itemgetter('date')):
    # 遍歷每個日期組內的所有記錄
    group_list = list(items)
    # 在這裡可以對每條記錄進行處理
    print(f"{date}: {group_list}")
