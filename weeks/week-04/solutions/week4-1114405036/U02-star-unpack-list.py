# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）
# 說明：使用星號 (*) 可以捕捉多出來的元素，且該變數永遠是一個 list。

record = ('Dave', 'dave@example.com')
# 就算右邊沒有對應 phones 的內容，phones 也會是個空的 list []
name, email, *phones = record

print(f"姓名: {name}")   # Dave
print(f"電話: {phones}") # []

# 若資料變多：
record2 = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
n, e, *p = record2
# p 會抓取剩下所有元素：['773-555-1212', '847-555-1212']