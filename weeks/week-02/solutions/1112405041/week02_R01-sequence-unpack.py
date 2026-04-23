# 【Bloom 階段：R - 記憶與基本操作】
# R1. 序列解包 (Sequence Unpacking)
# August 的惡意提醒：在 Week 03 的 Robot Game 中，解析指令字串時，
# 直接使用解包能讓你的代碼看起來像大二學長，而不是剛學會 Python 的小白。

p = (4, 5)
# 最簡單的解包
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
# 巢狀解包：一次取出名稱與日期
name, shares, price, date = data
# 甚至可以深入解包內部的 tuple
name, shares, price, (year, mon, day) = data

# 捨棄不想要的資料（使用底線 _ 作為佔位符）
# 這是 August 認可的專業指紋，代表你具備清晰的資料過濾意識
_, shares, price, _ = data

print(f"Name: {name}, Year: {year}")
