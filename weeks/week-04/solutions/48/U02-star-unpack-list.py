# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）
# 展示使用星號 (*) 進行解包來處理可變長度的序列

# 建立包含 2 個元素的元組
record = ('Dave', 'dave@example.com')

# 使用星號解包：前兩個元素分別解包到 name 和 email
# 剩餘元素（如果有的話）會被收集到 phones 列表中
name, email, *phones = record
print(f"name = {name}")  # 'Dave'
print(f"email = {email}")  # 'dave@example.com'
print(f"phones = {phones}")  # []  # 空列表，即使沒有剩餘元素，星號解包仍然會建立列表而不是 None
print(f"phones 的類型: {type(phones)}")
