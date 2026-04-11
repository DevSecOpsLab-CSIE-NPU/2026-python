# R13. 字典列表排序 itemgetter（1.13）

from operator import itemgetter

# 原始資料：包含多個字典的列表，每個字典代表一筆使用者紀錄
rows = [
    {'fname': 'Brian', 'uid': 1003}, 
    {'fname': 'John', 'uid': 1001},
    {'fname': 'David', 'uid': 1002},
    {'fname': 'Brian', 'uid': 1000}
]

# ── 1. 根據單一鍵值 (fname) 排序 ──────────────────────
# itemgetter('fname') 會提取字典中 'fname' 對應的值作為排序基準
# 結果：依據名字字母順序排序 (Brian, Brian, David, John)
sorted(rows, key=itemgetter('fname'))

# ── 2. 根據單一鍵值 (uid) 排序 ────────────────────────
# 結果：依據使用者 ID 數字大小排序 (1001, 1002, 1003)
sorted(rows, key=itemgetter('uid'))

# ── 3. 根據多個鍵值排序 ──────────────────────────────
# itemgetter 支援傳入多個參數。這會建立一個層次化的排序邏輯：
# 首先根據 'uid' 排序，若 'uid' 相同，則再根據 'fname' 排序。
# 此技巧在處理資料庫風格的「多重欄位排序」時非常方便。
sorted(rows, key=itemgetter('uid', 'fname'))