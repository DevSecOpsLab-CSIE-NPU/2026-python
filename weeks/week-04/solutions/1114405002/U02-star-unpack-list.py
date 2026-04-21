# U02 星號拆包會得到 list
# 重點：*var 會接收「其餘所有元素」，型別一定是 list。

record = ("Dave", "dave@example.com")
name, email, *phones = record

# 因為 record 只有兩個元素，phones 沒有拿到任何項目，所以是空 list。
# phones == []
