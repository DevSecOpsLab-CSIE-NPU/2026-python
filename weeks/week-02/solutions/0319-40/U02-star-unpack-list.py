# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

record = ('Dave', 'dave@example.com')
name, email, *phones = record

print("name =", name)
print("email =", email)
print("phones =", phones)
print("phones 的型別 =", type(phones).__name__)
