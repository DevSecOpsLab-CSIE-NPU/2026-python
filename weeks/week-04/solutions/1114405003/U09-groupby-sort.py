# U9. groupby 為何一定要先 sort（1.15）
# 此示例演示 itertools.groupby() 的重要特性：它只分組「連續」相同的元素
# 如果數據未排序，相同鍵值出現在不同位置時，會被視為不同的分組

# 導入所需模組
from itertools import groupby  # groupby：用於將迭代器按指定鍵進行分組
from operator import itemgetter  # itemgetter：用於從字典中提取指定欄位

# ===== 準備未排序的數據 =====
# 建立包含日期和追蹤值的字典列表
# 注意：相同日期（07/02）出現在位置 0 和位置 2，不連續
rows = [
    {'date': '07/02/2012', 'x': 1},  # 位置 0：07/02
    {'date': '07/01/2012', 'x': 2},  # 位置 1：07/01
    {'date': '07/02/2012', 'x': 3},  # 位置 2：07/02（又是 07/02）
]

# ===== 問題演示：沒排序的 groupby 結果 =====
# 不先排序的情況下使用 groupby
# 沒排序：07/02 會被分成兩段（因為 groupby 只看「連續」）
for k, g in groupby(rows, key=itemgetter('date')):
    # k：當前分組的日期
    # g：該分組的迭代器
    group_list = list(g)  # 將分組轉換為列表以查看內容
    
    # 結果分析：
    # 第一次迴圈（k='07/02'）：group_list = [{'date': '07/02/2012', 'x': 1}]
    # 第二次迴圈（k='07/01'）：group_list = [{'date': '07/01/2012', 'x': 2}]
    # 第三次迴圈（k='07/02'）：group_list = [{'date': '07/02/2012', 'x': 3}]
    # 問題：07/02 被分成了兩個分組（位置 0 和位置 2），而不是合併成一個

# ===== groupby 的核心限制 =====
# groupby() 是一個「流式」分組函數，它只分組「連續」的相同元素
# 它不會自動排序數據，而是基於以下邏輯：
# 1. 遍歷序列中的元素
# 2. 應用 key 函數產生分組鍵
# 3. 當鍵變化時，開始新的分組
# 4. 如果之後再看到相同的鍵，它會被視為新的分組（不是延續）

# ===== 解決方案：先排序 =====
# 排序後：同 date 才會連在一起，分組才正確
# 使用 sort 方法根據日期欄位排序數據
# itemgetter('date') 指定排序的鍵
rows.sort(key=itemgetter('date'))
# 排序後的結果：
# [
#     {'date': '07/01/2012', 'x': 2},
#     {'date': '07/02/2012', 'x': 1},
#     {'date': '07/02/2012', 'x': 3},
# ]

# ===== 排序後的 groupby 結果 =====
for k, g in groupby(rows, key=itemgetter('date')):
    # k：當前分組的日期
    # g：該分組的迭代器
    group_list = list(g)
    
    # 結果分析：
    # 第一次迴圈（k='07/01/2012'）：group_list = [{'date': '07/01/2012', 'x': 2}]
    # 第二次迴圈（k='07/02/2012'）：group_list = [{'date': '07/02/2012', 'x': 1}, {'date': '07/02/2012', 'x': 3}]
    # 正確：同日期的記錄被正確地分組在一起

# ===== 為什麼 groupby 不自動排序 =====
# 1. 效率考慮：排序需要 O(n log n) 時間，groupby 本身只需 O(n)
# 2. 靈活性：有些情況下你可能想在已排序的流上操作
# 3. 責任分離：排序是調用者的責任

# ===== 與 SQL GROUP BY 的區別 =====
# SQL：SELECT * FROM table GROUP BY date
#   - 會自動聚合所有相同的日期，無論順序如何
#
# Python groupby：
#   - 只分組連續的相同元素
#   - 需要調用者先排序

# ===== 實用建議 =====
# 1. 使用 groupby 前，一定要確保數據已按分組鍵排序
# 2. 大多數情況使用：
#    data.sort(key=...)  # 或 sorted(data, key=...)
#    for k, g in groupby(data, key=...):
#
# 3. 如果需要自動分組（不講究順序），考慮使用：
#    from collections import defaultdict
#    groups = defaultdict(list)
#    for item in data:
#        groups[item['date']].append(item)
#    （但這樣無法保持原始順序）

# ===== 記住的要點 =====
# ⚠️ groupby = 「連續相同」的分組，不是「全部相同」的分組
# ⚠️ 一定要先 sort()
# ⚠️ 不同的日期/鍵出現在不同位置，會形成多個分組
