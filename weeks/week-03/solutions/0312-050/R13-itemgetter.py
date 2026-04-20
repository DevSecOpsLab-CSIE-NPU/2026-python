# R13. 字典列表排序 itemgetter（1.13）

# 從 operator 模組導入 itemgetter 函式，它用於快速從字典等支援 __getitem__ 的物件中提取指定鍵的值。
from operator import itemgetter

# 定義一個字典列表 rows，每個字典代表一筆資料，包含 'fname' (名字) 和 'uid' (使用者ID)。
rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]
# 為了更好地展示多鍵排序效果，我們稍微擴充一下資料，加入更多屬性與重複的 uid。
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Dave', 'lname': 'Jones', 'uid': 1002},
    {'fname': 'Mary', 'lname': 'Cleese', 'uid': 1001}, # 注意這裡 uid 與 John 相同，用於展示多鍵排序
]
# 顯示原始未排序的字典列表。
print(f"原始字典列表 rows:\n  {rows}\n")

print("--- 根據單一鍵 ('fname') 排序 ---")
# 使用 sorted() 函式對 rows 進行排序。
# key=itemgetter('fname') 指定排序的依據是每個字典中 'fname' 鍵對應的值。
# 相當於使用 lambda x: x['fname']，但 itemgetter 是在底層 C 語言層級執行，速度更快。
sorted_by_fname = sorted(rows, key=itemgetter('fname'))
print(f"根據 'fname' 排序後:\n  {sorted_by_fname}\n")

print("--- 根據單一鍵 ('uid') 排序 ---")
# key=itemgetter('uid') 指定排序的依據是 'uid' 鍵對應的值。
sorted_by_uid = sorted(rows, key=itemgetter('uid'))
print(f"根據 'uid' 排序後:\n  {sorted_by_uid}\n")

print("--- 根據多個鍵 ('uid', 然後 'fname') 排序 ---")
# itemgetter 也可以同時接受多個鍵。
# key=itemgetter('uid', 'fname') 表示先根據 'uid' 排序，如果 'uid' 相同（如約翰和瑪麗都是 1001），則再根據 'fname' (名字字母順序) 進行二次排序。
sorted_by_uid_fname = sorted(rows, key=itemgetter('uid', 'fname'))
print(f"根據 'uid' 和 'fname' 排序後:\n  {sorted_by_uid_fname}")
