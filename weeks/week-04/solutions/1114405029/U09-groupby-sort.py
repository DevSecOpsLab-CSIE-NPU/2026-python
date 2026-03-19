# U9. groupby 為何一定要先 sort（1.15）

# 匯入 groupby（用來分組）
from itertools import groupby

# 匯入 itemgetter（用來指定依哪個欄位分組）
from operator import itemgetter

# 建立資料 rows（每一筆都是字典）
# 注意：這裡的 date 並沒有排序
rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 印出原始資料
print("原始資料 rows（未排序）：")
for r in rows:
    print(r)

print()  # 空一行

# 沒排序：07/02 會被分成兩段（因為 groupby 只看「連續」）
print("【未排序直接 groupby 的結果】")

for k, g in groupby(rows, key=itemgetter('date')):
    group_list = list(g)  # 將 group 轉成 list 才能印出
    print("分組 key =", k, "，內容 =", group_list)

print()
print("說明：因為 groupby 只會將「相鄰且相同」的 key 分在同一組，")
print("所以未排序時，07/02 會被拆成兩個群組。")

print()  # 空一行

# 排序後：同 date 才會連在一起，分組才正確
rows.sort(key=itemgetter('date'))

# 印出排序後的資料
print("排序後的 rows：")
for r in rows:
    print(r)

print()  # 空一行

print("【排序後再 groupby 的結果】")

for k, g in groupby(rows, key=itemgetter('date')):
    group_list = list(g)
    print("分組 key =", k, "，內容 =", group_list)

print()
print("說明：排序後，相同的 date 會排列在一起，")
print("因此 groupby 才能正確地把相同日期的資料分在同一組。")