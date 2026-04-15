# R15. 分組 groupby（1.15）

# groupby 來自 itertools，用於「連續相同 key」的分組。
# 注意：它不會自動全域分組，因此通常要先排序，
# 讓相同 key 的資料排在一起，才能得到預期結果。
from itertools import groupby
# itemgetter('date') 會回傳一個函式，用來快速取出每筆資料的 'date' 欄位。
from operator import itemgetter

# 範例資料：每個元素都是 dict，包含日期與地址。
# 這裡僅示範兩筆資料，實務上可以是多筆且日期可能重複。
rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]

# 先依 date 排序是使用 groupby 的關鍵步驟。
# 若未排序，groupby 只會把「相鄰且 key 相同」的項目分在同一組，
# 導致同日期資料可能被拆成多個群組。
rows.sort(key=itemgetter('date'))

# 依照 date 進行分組：
# - date: 目前群組的鍵（例如 '07/01/2012'）
# - items: 該群組的可迭代物件（iterator），可逐筆取出資料
#
# 小提醒：items 是一次性迭代器，若先轉成 list(items) 之後，
# 再次迭代就會是空的，使用時要注意順序。
for date, items in groupby(rows, key=itemgetter('date')):
    # 走訪該日期群組中的每一筆資料 i。
    # i 會是像 {'date': '07/01/2012', 'address': '...'} 的 dict。
    for i in items:
        # 本範例不做實際處理，僅展示分組後如何逐筆讀取。
        # 可在此加入：列印、統計、彙整或寫入檔案等邏輯。
        print(i)
        pass
