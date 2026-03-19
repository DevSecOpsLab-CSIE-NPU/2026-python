# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

record = ('Dave', 'dave@example.com')

# 前兩個值分別指定給 name、email，剩下的都收進 phones
name, email, *phones = record

# 即使沒有剩餘元素，星號變數也會得到空的 list
# phones == []  仍是 list
print('name =', name)
print('email =', email)
print('phones =', phones)
print('phones type =', type(phones).__name__)
