# U10. zip 為何只能用一次（1.8）

# 建立一個字典 prices
# key 代表商品名稱
# value 代表價格
prices = {'A': 2.0, 'B': 1.0}

# 使用 zip 將 values 與 keys 配對
# 這裡的 z 不是串列，而是「迭代器（iterator）」
# 迭代器的特性是：資料會被逐次取出，而且只能使用一次
z = zip(prices.values(), prices.keys())

# 印出 z 本身（會看到是一個 zip 物件，而不是內容）
print("z 本身（zip 物件）：", z)

print()  # 空一行

# 第一次使用 z：用 min() 取得最小的 (value, key)
# 這個動作會「消耗掉」迭代器中的資料
min_result = min(z)  # OK（消耗掉迭代器）

print("第一次使用 min(z) 的結果：", min_result)

print()  # 空一行

# 嘗試再次使用 z
# 這時候 z 已經被消耗完，所以會是空的
print("將 z 轉成 list 檢查剩餘內容：", list(z))

print()  # 空一行

# # max(z)  # 會失敗：因為 z 已經被消耗完
# 上面這行如果真的執行，會發生錯誤（ValueError: max() arg is an empty sequence）

# 為了安全示範，我們用 try-except 來展示錯誤情況
try:
    result = max(z)
    print("max(z) 的結果：", result)
except ValueError as e:
    print("再次使用 max(z) 時發生錯誤：", e)

print()  # 空一行

# 說明為什麼會這樣
print("說明：")
print("zip() 產生的是迭代器（iterator），資料在被取出後就會被消耗掉。")
print("因此像 min() 這類操作會一次讀完所有元素，之後就無法再使用同一個 zip 物件。")
print("如果需要重複使用，應該重新建立 zip，或先轉成 list。")