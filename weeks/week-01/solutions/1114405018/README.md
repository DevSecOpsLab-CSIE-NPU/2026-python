<!-- 
變數與指定(Assignment) - 單元測試說明文件
解釋該測試程式的結構、覆蓋範圍和使用方式
 -->

# 變數與指定(Assignment) 單元測試說明

## 📋 概述

此單元測試程式全面涵蓋 Python 中**變數與指定(assignment)**的所有主要概念，共包含 **26 個測試**，分為 6 個測試類別。

測試程式位置：
```
c:\Users\nina9\OneDrive\桌面\python\python2\2026-python\weeks\week-01\solutions\1114405018\test_variables_assignment.py
```

## 🎯 測試覆蓋範圍

### 1. 簡單變數指定 (TestSimpleAssignment) - 5 個測試
測試基本的變數指定操作

| 測試 | 說明 | 例子 |
|------|------|------|
| `test_integer_assignment` | 整數值指定 | `x = 10` |
| `test_string_assignment` | 字串值指定 | `name = 'ACME'` |
| `test_float_assignment` | 浮點數指定 | `price = 19.99` |
| `test_boolean_assignment` | 布林值指定 | `is_active = True` |
| `test_none_assignment` | None 值指定 | `result = None` |

### 2. 多重變數指定/解包 (TestMultipleAssignment) - 6 個測試
測試同時指定多個變數和從可迭代物件解包

| 測試 | 說明 | 例子 |
|------|------|------|
| `test_swap_style_assignment` | 交換風格指定 | `a, b = 3, 5` |
| `test_three_variable_assignment` | 三個變數指定 | `x, y, z = 1, 2, 3` |
| `test_unpack_from_tuple` | 從元組解包 | `a, b, c = (10, 20, 30)` |
| `test_unpack_from_list` | 從列表解包 | `a, b, c = ['a', 'b', 'c']` |
| `test_string_unpacking` | 從字串解包 | `a, b, c = 'xyz'` |
| `test_mismatched_unpacking_raises_error` | 解包數量不匹配拋異常 | `a, b, c = 1, 2` ❌ |

### 3. 函式回傳值接收 (TestFunctionReturnValue) - 4 個測試
測試如何接收和解包函式的回傳值

| 測試 | 說明 | 例子 |
|------|------|------|
| `test_receive_single_value` | 接收函式回傳值 | `result = get_point()` |
| `test_unpack_function_return` | 解包函式回傳的兩個值 | `px, py = get_point()` |
| `test_unpack_multiple_return_values` | 解包函式回傳的三個值 | `name, age, city = get_multiple_values()` |
| `test_receive_multiple_values_without_unpacking` | 不解包接收 | `data = get_multiple_values()` |

### 4. 交換操作 (TestSwapOperation) - 2 個測試
測試使用多重指定進行變數交換

| 測試 | 說明 | 例子 |
|------|------|------|
| `test_swap_with_function` | 透過函式交換 | `a, b = swap_values(a, b)` |
| `test_swap_inline` | 內聯交換 | `x, y = y, x` |

### 5. 複雜解包 (TestComplexUnpacking) - 5 個測試
測試進階的解包技巧和巢狀結構

| 測試 | 說明 | 例子 |
|------|------|------|
| `test_nested_unpacking` | 巢狀元組解包 | `(x1, y1), (x2, y2) = ((1,2), (3,4))` |
| `test_partial_unpacking_with_star` | 星號解包 | `first, *rest = [1,2,3,4,5]` |
| `test_star_in_middle` | 星號在中間 | `first, *middle, last = [1,2,3,4,5]` |
| `test_underscore_for_ignored_values` | 使用底線忽略值 | `name, _, city = get_multiple_values()` |
| `test_unpacking_with_dict` | 字典解包 | `key1, key2 = data` |

### 6. 變數重新指定 (TestReAssignment) - 4 個測試
測試變數可被多次重新指定

| 測試 | 說明 | 例子 |
|------|------|------|
| `test_sequential_reassignment` | 順序重新指定 | `x = 5; x = 10; x = 15` |
| `test_reassign_different_type` | 指定不同類型 | `value = 42; value = "hello"; value = [1,2,3]` |
| `test_increment_reassignment` | 使用自身重新指定 | `counter = counter + 1` |
| `test_augmented_assignment` | 增量指定運算子 | `x += 5; x -= 3` |

## 🚀 執行測試

### 方法 1：直接執行測試檔
```bash
cd c:\Users\nina9\OneDrive\桌面\python\python2\2026-python\weeks\week-01\solutions\1114405018
python test_variables_assignment.py
```

### 方法 2：使用 unittest 模組
```bash
python -m unittest test_variables_assignment -v
```

### 方法 3：執行特定測試類別
```bash
python -m unittest test_variables_assignment.TestSimpleAssignment -v
```

### 方法 4：執行特定測試方法
```bash
python -m unittest test_variables_assignment.TestSimpleAssignment.test_integer_assignment -v
```

## 📊 測試結果

```
Ran 26 tests in 0.004s

OK
```

✅ 全部測試通過

## 📝 程式碼特點

### 1. 豐富的註解
- 每個測試類別都有類別級文件說明
- 每個測試方法都有詳細的繁體中文註解
- 關鍵步驟都加上了 `#` 開頭的註解

### 2. 完整的文件字串
- 模組級文件說明
- 函式級文件說明（docstring）
- 清楚說明參數和返回值

### 3. 最佳實踐
- 遵循 unittest 框架標準
- 清晰的測試方法命名（test_* 開頭）
- 適當使用 `assertEqual`, `assertTrue`, `assertIsInstance` 等斷言
- 測試異常行為中使用 `assertRaises`

## 🎓 學習重點

此測試程式涵蓋的概念：

1. **基本指定**：將值存儲在變數中
2. **多重指定**：同時指定多個變數
3. **解包**：從序列中提取多個值
4. **函式回傳**：接收函式返回的多個值
5. **嵌套結構**：處理複雜的資料結構
6. **星號運算子**：高級解包技巧
7. **重新指定**：變數值的修改
8. **增量運算子**：快速修改變數值

## 🔧 修改和擴展

如果要添加更多測試，遵循以下模式：

```python
def test_new_feature(self):
    """測試新功能的簡短說明"""
    # 步驟 1：準備數據
    # ...
    
    # 步驟 2：執行操作
    # ...
    
    # 步驟 3：驗證結果
    self.assertEqual(expected, actual)
```

## 📚 相關資源

- 對應的 Markdown 教學檔：`01-variables-assignment.md`
- 對應的 Python 範例：`01-variables-assignment.py`
- 官方 Python 文檔：https://docs.python.org/3/tutorial/datastructures.html

---

**建立日期**: 2026-04-15
**測試數量**: 26
**所有測試**: ✅ 通過
