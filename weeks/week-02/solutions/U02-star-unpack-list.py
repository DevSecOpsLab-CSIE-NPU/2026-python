# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）
#
# 在 Python 的序列解包中，星號（*）可以用來接收剩餘的元素，
# 這讓對長度不固定的序列進行解包時更加靈活。
#
# 規則：
# - 星號只會出現在左邊（targets）
# - 它會把尚未被其他變數拿走的元素，一次收成 list
# - 即使沒有多餘元素，也會回傳空 list

record = ('Dave', 'dave@example.com')
name, email, *phones = record
# phones == []  仍是 list
