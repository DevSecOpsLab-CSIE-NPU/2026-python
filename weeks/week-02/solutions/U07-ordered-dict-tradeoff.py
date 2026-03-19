# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）
#
# 在 Python 3.7+ 的 dict 已經保留插入順序，OrderedDict 與 dict 行為相似，
# 但它有一些額外功能（例如 move_to_end）且內部用了一個雙向連結串列來
# 維持順序。
#
# 這代表 OrderedDict 會比普通 dict 佔用更多記憶體（用來儲存指標/節點），
# 但若有需要控制「插入順序」或進行「順序操作」，它仍是有用的。

from collections import OrderedDict

# 1. 基本順序展示
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['baz'] = 3

print("--- 初始順序 ---")
for key, value in d.items():
    print(f"{key}: {value}")

# 2. OrderedDict 特有功能：將某個 key 移到最後 (move_to_end)
# 這是普通 dict 做不到的簡潔操作
d.move_to_end('foo')

print("\n--- 將 'foo' 移至最後後 ---")
print(d)

# 3. OrderedDict 特有功能：從最前面彈出 (popitem)
# last=False 表示彈出第一筆 (FIFO)，last=True (預設) 則是最後一筆 (LIFO)
first_key, first_val = d.popitem(last=False)

print(f"\n--- 彈出第一筆資料 ---")
print(f"Popped: {first_key} -> {first_val}")
print(f"剩餘內容: {dict(d)}")
# 你能解釋：為了維持插入順序，它需要額外結構（因此更耗記憶體）
