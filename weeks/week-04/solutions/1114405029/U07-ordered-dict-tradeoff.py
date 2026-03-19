# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

# 從 collections 模組匯入 OrderedDict
# OrderedDict 是「有序字典」，
# 會記住資料插入時的順序
from collections import OrderedDict

# 建立一個 OrderedDict 物件 d
d = OrderedDict()

# 依序加入兩筆資料
# 第一次加入鍵 'foo'，值為 1
d['foo'] = 1

# 第二次加入鍵 'bar'，值為 2
d['bar'] = 2

# 你能解釋：為了維持插入順序，它需要額外結構（因此更耗記憶體）

# 印出 OrderedDict 物件本身
print("OrderedDict 物件 d：")
print(d)

print()  # 空一行，讓輸出結果更清楚

# 逐一印出 d 中的鍵與值
# 可以觀察到輸出的順序會和插入順序一致
print("依照插入順序印出 OrderedDict 中的資料：")
for key, value in d.items():
    print("鍵：", key, "，值：", value)

print()  # 空一行，讓輸出結果更清楚

# 印出所有鍵，方便觀察順序
print("d 的所有鍵：", list(d.keys()))

# 印出所有值，方便觀察順序
print("d 的所有值：", list(d.values()))

print()  # 空一行，讓輸出結果更清楚

# 說明 OrderedDict 的特色與取捨
print("說明：")
print("OrderedDict 會記住元素加入的先後順序，因此輸出時可以保持插入順序。")
print("為了做到這件事，它通常需要額外的內部結構來記錄順序資訊。")
print("也因為要多維護這些順序資料，所以相較於一般 dict，會消耗更多記憶體。")