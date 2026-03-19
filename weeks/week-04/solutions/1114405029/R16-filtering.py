# R16. 過濾：推導式 / generator / filter / compress（1.16）

# 建立一個串列 mylist
# 裡面包含正數與負數，等等會拿來示範「過濾資料」
mylist = [1, 4, -5, 10]

# 使用串列推導式（list comprehension）
# 從 mylist 中逐一取出每個元素 n
# 只保留大於 0 的數字
# 最後會產生一個新的串列
positive_list = [n for n in mylist if n > 0]

# 印出原始串列
print("原始 mylist 串列：", mylist)

# 印出經過串列推導式過濾後的結果
print("使用串列推導式篩選出大於 0 的數字：", positive_list)

print()  # 空一行，讓輸出結果更清楚

# 使用生成器推導式（generator expression）
# 與串列推導式很像，但不會一次把結果全部存成串列
# 而是需要時才逐一產生資料，比較節省記憶體
pos = (n for n in mylist if n > 0)

# 直接印出生成器本身，只會看到它的物件資訊，不會看到內容
print("生成器 pos 本身：", pos)

# 若要看到生成器中的實際內容，可以用 list() 轉成串列後再印出
print("將生成器 pos 轉成串列後的結果：", list(pos))

print()  # 空一行，讓輸出結果更清楚

# 建立一個字串串列 values
# 裡面有些內容可以轉成整數，有些不行
values = ['1', '2', '-3', '-', 'N/A']

# 定義一個函式 is_int(val)
# 功能：判斷傳入的 val 是否可以成功轉成整數
def is_int(val):
    try:
        # 嘗試把 val 轉成整數
        # 如果成功，表示它是合法的整數字串
        int(val)
        return True
    except ValueError:
        # 如果轉換失敗，會發生 ValueError 錯誤
        # 代表這個字串不是合法整數
        return False

# 使用 filter() 函式搭配 is_int
# 將 values 中「能轉成整數」的元素篩選出來
# filter() 回傳的是一個可迭代物件，所以用 list() 轉成串列方便顯示
filtered_values = list(filter(is_int, values))

# 印出原始資料
print("原始 values 串列：", values)

# 印出經 filter() 篩選後的結果
print("使用 filter() 篩選可轉成整數的字串：", filtered_values)

print()  # 空一行，讓輸出結果更清楚

# 從 itertools 模組匯入 compress 函式
# compress 的功能是：根據對應位置的布林值(True/False)來決定是否保留資料
from itertools import compress

# 建立地址串列
addresses = ['a1', 'a2', 'a3']

# 建立對應的數量串列
counts = [0, 3, 10]

# 使用串列推導式建立布林值串列 more5
# 判斷 counts 中每個數字是否大於 5
# 若大於 5 則為 True，否則為 False
more5 = [n > 5 for n in counts]

# 使用 compress(addresses, more5)
# 會根據 more5 中的 True / False 來篩選 addresses
# 只有對應位置為 True 的地址才會被保留下來
compressed_result = list(compress(addresses, more5))

# 印出原始地址資料
print("原始 addresses 串列：", addresses)

# 印出原始數量資料
print("原始 counts 串列：", counts)

# 印出布林判斷結果
print("counts 中各元素是否大於 5：", more5)

# 印出 compress 過濾後保留的地址
print("使用 compress() 篩選後的地址：", compressed_result)