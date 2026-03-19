# R15. 分組 groupby（1.15）
# groupby 是 itertools 模組中的一個函數，
# 用於將序列中的連續元素按照指定的鍵進行分組。
# 注意：使用前需要先對序列進行排序，確保相同鍵的元素相鄰。

# 匯入 groupby 和 itemgetter
from itertools import groupby
from operator import itemgetter

# 創建一個包含記錄的列表，每個記錄有日期和地址
rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]

# 按日期排序，確保相同日期的記錄相鄰
rows.sort(key=itemgetter('date'))

# 使用 groupby 按日期分組
# groupby 返回一個迭代器，每次迭代返回 (鍵, 組迭代器) 的元組
for date, items in groupby(rows, key=itemgetter('date')):
    # date 是分組鍵（日期）
    # items 是該組的所有記錄的迭代器
    for i in items:
        # 處理組內的每個記錄
        pass
