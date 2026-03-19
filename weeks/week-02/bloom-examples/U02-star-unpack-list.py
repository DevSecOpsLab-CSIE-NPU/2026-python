"""U02: 星號解包在元素不足時，仍會給你空 list。"""

record = ('Dave', 'dave@example.com')
name, email, *phones = record

print('name:', name)
print('email:', email)
print('phones:', phones)
print('phones 型別:', type(phones).__name__)
