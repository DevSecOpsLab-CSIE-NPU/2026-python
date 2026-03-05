# 8 容器操作與推導式

你必須已經「不需要解釋」就能看懂：

```python
# 列表推導式：從 data 中過濾出大於 0 的元素，並組成新列表
# 語法：[表達式 for 變數 in 可迭代對象 if 條件]
# 相當於：result = []; for x in data: if x > 0: result.append(x)
[x for x in data if x > 0]

# 字典推導式：從字典 d 中創建新字典，包含所有鍵值對
# 語法：{鍵表達式: 值表達式 for 鍵, 值 in 可迭代對象.items()}
# 相當於：result = {}; for k, v in d.items(): result[k] = v
{k: v for k, v in d.items()}
```

```python
# 生成器表達式：生成 nums 中每個元素的平方，但不立即計算
# 語法：(表達式 for 變數 in 可迭代對象)
# 相當於：def generator(): for x in nums: yield x * x
# 使用時才計算，節省記憶體
(x * x for x in nums)
```

用途（對應第一章範例）：

- 過濾序列（1.16）：使用列表推導式移除不符合條件的元素
- 字典子集（1.17）：使用字典推導式創建字典的子集
- `sum(...)` / `min(...)` / `join(...)`：這些函數接受可迭代對象，生成器表達式很適合用於大型數據處理
