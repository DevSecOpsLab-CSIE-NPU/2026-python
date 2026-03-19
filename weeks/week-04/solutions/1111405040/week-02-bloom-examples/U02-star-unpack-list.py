"""
U02: 星號拆封

即使沒有多餘元素，被星號接住的結果仍會是 list。
"""

record = ("Dave", "dave@example.com")
name, email, *phones = record

# phones 會是空串列，而不是 None。
# phones == []
