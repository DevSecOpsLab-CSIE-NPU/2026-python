# R13. 字典列表排序 itemgetter（1.13）
#
# itemgetter 是用來取出 dict 或序列中特定欄位的工具：
# 1. 當排序條件很簡單時，比 lambda 更直觀。
# 2. 可以排序單一欄位，也可以一次排序多個欄位。
# 3. 很適合搭配 sorted() 使用。

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]
sorted(rows, key=itemgetter('fname'))
sorted(rows, key=itemgetter('uid'))
sorted(rows, key=itemgetter('uid', 'fname'))
