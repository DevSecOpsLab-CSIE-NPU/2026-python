# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）
#
# 觀念重點：
# - 星號變數（*phones）會把「剩下的元素」全部打包。
# - 不管剩下 0 個、1 個或多個，結果型別都會是 list。

record = ('Dave', 'dave@example.com')
name, email, *phones = record

# 這裡沒有多餘元素，所以 phones 會是空 list，而不是 None。
# phones == []
print(record)