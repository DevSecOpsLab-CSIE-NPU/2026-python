# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

record = ('Dave', 'dave@example.com')

# 星號變數 *phones 會接收「剩下的所有元素」
name, email, *phones = record

# record 只有兩個元素，因此 phones 會是空列表 []
# phones == []