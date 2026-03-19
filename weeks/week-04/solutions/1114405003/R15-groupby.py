# R15. 分組 groupby（1.15）
# 此示例演示如何使用 itertools.groupby() 函數將列表中的字典按照指定鍵值進行分組

# 導入所需的模組
from itertools import groupby  # groupby：用於將迭代器按指定鍵進行分組的函數
from operator import itemgetter  # itemgetter：用於從字典或序列中提取指定索引的值

# 建立包含多個字典的列表，每個字典代表一筆記錄
# 在此例中，每筆記錄包含日期(date)和地址(address)兩個欄位
rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]

# 重要：在使用 groupby() 之前必須先對數據進行排序
# groupby() 只會對分組鍵值相鄰的元素進行分組，不會排序數據
# 因此需要先使用 sort() 方法按照日期(date)欄位進行排序
# itemgetter('date') 用於指定排序和分組的鍵值
rows.sort(key=itemgetter('date'))

# 使用 groupby() 按日期進行分組
# groupby() 返回一個迭代器，產生(鍵,組)的二元組
# - 鍵(date)：當前分組的日期值
# - 組(items)：該日期內所有行的迭代器
for date, items in groupby(rows, key=itemgetter('date')):
    # 內層迴圈：遍歷當前分組內的所有行
    # items 是一個迭代器，包含該日期的所有記錄
    for i in items:
        # 在此可以對每一筆記錄進行處理
        # 例如：計算該日期的統計資訊、列印記錄詳情等
        print (i)
        pass
