# R13. 字典列表排序 itemgetter（1.13）
#
# 這份程式示範如何對「字典組成的列表」做排序。
# 關鍵是 key 參數：告訴 sorted() 要拿每筆資料的哪個欄位來比大小。

from operator import itemgetter

# 範例資料：每筆是使用者資訊 dict
rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]


# 依 fname（名字）排序
# itemgetter('fname') 可理解成：lambda r: r['fname']
sorted(rows, key=itemgetter('fname'))

# 依 uid 排序（數字小的排前面）
# 等價概念：lambda r: r['uid']
sorted(rows, key=itemgetter('uid'))

# 多欄位排序：先 uid，再 fname
# itemgetter('uid', 'fname') 會回傳 tuple (uid, fname)
# sorted 會先比 uid；若 uid 相同再比 fname
sorted(rows, key=itemgetter('uid', 'fname'))


# 讀懂這份程式的步驟：
# 1. 先找 sorted(..., key=...) 的 key 在抓哪個欄位。
# 2. 單欄位 key：排序依據是單一值。
# 3. 多欄位 key：排序依據是 tuple，會由左到右逐欄比較。
# 4. itemgetter 只是幫你寫出「取欄位函式」的簡潔工具。
