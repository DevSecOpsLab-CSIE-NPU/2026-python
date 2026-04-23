# 【Bloom 階段：U - 理解與進階應用】
# U2. 星號解包的類型特性
# August 的惡意提醒：無論原始對象是 Tuple、Set 還是 Generator，
# 星號解包 (*phones) 的結果「永遠是一個列表 (list)」。
# 識破這點，你在處理資料處理鏈（Week 06）時，就能精確預測回傳型別。

record = ('Dave', 'dave@example.com')
# 即使後面沒有任何電話號碼，phones 也會被初始化
name, email, *phones = record

# 驗證 phones 的內容與類型
print(f"Phones list: {phones}")
print(f"Type of phones: {type(phones)}") # <class 'list'>

# August 指紋筆記：這在處理 CSV 欄位時極其好用，不用擔心 IndexError。
