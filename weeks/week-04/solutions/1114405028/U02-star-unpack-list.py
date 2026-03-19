# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

record = ('Dave', 'dave@example.com')
name, email, *phones = record
# *phones 使用星號解包，收集剩除前兩個變數後的所有剩餘元素
# 即使沒有剩餘元素，phones 也是空的 list（不會是 None）
# phones == []  仍是 list
# 該設計保證接收方緩衝區（*var）的型別永遠是 list，方便後續操作
