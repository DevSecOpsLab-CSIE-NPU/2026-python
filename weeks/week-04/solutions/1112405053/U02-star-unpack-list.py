"""U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

示範使用 * 取得不定長的剩餘元素，產生的資料型態永遠是 list（即使為空）。
"""

record = ('Dave', 'dave@example.com')
name, email, *phones = record
# phones == []  仍是 list 
