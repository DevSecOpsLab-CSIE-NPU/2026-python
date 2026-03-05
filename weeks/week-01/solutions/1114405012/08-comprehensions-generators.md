# 8 容器操作與推導式

你必須已經「不需要解釋」就能看懂：

## 📚 列表推導式 (List Comprehension) 與字典推導式 (Dictionary Comprehension)

```python
# 列表推導式：從 data 中過濾出所有大於 0 的元素
# 語法：[表達式 for 變數 in 可迭代物件 if 條件]
[x for x in data if x > 0]
# 等同於：
# result = []
# for x in data:
#     if x > 0:
#         result.append(x)

# 字典推導式：從字典 d 中建立新字典
# 語法：{鍵表達式: 值表達式 for 變數 in 可迭代物件}
{k: v for k, v in d.items()}
# 等同於：
# result = {}
# for k, v in d.items():
#     result[k] = v
```

## ⚡ 生成器表達式 (Generator Expression)

```python
# 生成器表達式：惰性求值，一次產生一個值（節省記憶體）
# 語法：(表達式 for 變數 in 可迭代物件)
(x * x for x in nums)
# 與列表推導式的差異：
# - 列表推導式 [x*x for x in nums] → 立即產生完整列表
# - 生成器表達式 (x*x for x in nums) → 按需產生值，記憶體效率高
```

## 🎯 實際應用範例

用途（對應第一章範例）：

- **過濾序列（1.16）**
  ```python
  # 過濾出正數
  positive_nums = [x for x in numbers if x > 0]
  ```

- **字典子集（1.17）**
  ```python
  # 選取特定鍵值對
  filtered_dict = {k: v for k, v in my_dict.items() if v > 100}
  ```

- **搭配內建函數使用**
  ```python
  # 計算總和（使用生成器，節省記憶體）
  total = sum(x * x for x in nums)
  
  # 找最小值
  min_value = min(x for x in data if x > 0)
  
  # 字串連接
  result = ','.join(str(x) for x in numbers)
  ```

## 💡 學習重點

1. **列表推導式** `[]`：建立新列表，適合需要保留所有結果的情況
2. **字典推導式** `{}`：建立新字典，快速轉換或過濾字典資料
3. **生成器表達式** `()`：惰性求值，適合大數據或只需遍歷一次的情況
4. **效能差異**：生成器只在需要時才計算值，列表推導式會立即計算所有值
