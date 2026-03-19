# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）
# 展示 OrderedDict 如何維持鍵值對的插入順序及其記憶體取捨

# 導入 OrderedDict 模組
from collections import OrderedDict

# 建立 OrderedDict 實例
d = OrderedDict()

# 按插入順序添加鍵值對
d['foo'] = 1  # 第一對
d['bar'] = 2  # 第二對

print("OrderedDict 內容:", d)
print("迭代結果:")
for key in d:
    print(f"  {key}: {d[key]}")
# 迭代時，元素按插入順序返回
# for key in d: 會得到 'foo', 'bar'（按插入順序）
# 標準 dict 也保序（Python 3.7+），但 OrderedDict 提供了額外保障

# ⚖️ 記憶體取捨的原因：
print("\n記憶體取捨:")
print("  為了維持插入順序，OrderedDict 需要：")
print("  1. 雙向連結串列（doubly-linked list）結構")
print("  2. 每個節點額外存儲指向上一個和下一個元素的指標")
print("  3. 這會增加額外的記憶體開銷（大約是普通字典的 2-3 倍）")

# 何時使用 OrderedDict：
print("\n何時使用 OrderedDict:")
print("  - 需要相容性（Python < 3.7）")
print("  - 需要明確表示順序很重要")
print("  - 需要 move_to_end() 等特殊操作")
