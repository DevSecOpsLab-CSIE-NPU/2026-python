# AI_LOG

目的：記錄第 4 題二分搜尋與線性搜尋的開發過程。

- 時間範圍：2026-06-22
- 主要任務：實作二分搜尋、線性搜尋、性能測試、雷達圖繪製

## 1) 題目要求

1. 產生或讀入升冪排序的整數陣列
2. 實作二分搜尋找出 K = 156，輸出「是否存在」與「比較次數」
3. 用 timeit 分別量測線性搜尋與二分搜尋的耗時
4. 畫一張雷達圖呈現線性 vs 二分的多維權衡
5. 輸出 assets/radar.png

## 2) 實作內容

### solution.py

包含：
- `linear_search(arr, target)` - 線性搜尋
- `binary_search(arr, target)` - 二分搜尋
- `generate_array(size)` - 產生升冪陣列
- `main()` - 主程式

**關鍵設定**：
- K = 156（學號末兩碼 + 100）
- ARRAY_SIZE = 100,000（足夠看出效能差異）

### plot.py

包含：
- `calculate_metrics()` - 計算各項指標
- `plot_radar()` - 繪製雷達圖

**維度選擇**（5 維，參考題目建議）：
1. 小 n 速度（n=1000）
2. 大 n 速度（n=100000）
3. 是否需先排序（1=不需、0=需要）
4. 實作簡易度（1=簡單、0=複雜）
5. 最壞情況比較次數（1=少、0=多）

**正規化方式**：
- 時間相對比例（0-1）
- 比較次數相對比例（0-1）
- 評分直接轉換（0-1）

### test_solution.py

測試用例：
- `test_large_array()` - 測試預設 100,000 元素陣列
- `test_custom_array()` - 測試自訂小型陣列
- `test_target_in_array()` - 測試目標在陣列中的情況

## 3) 輸出格式

### 搜尋結果

```
FOUND <索引> cmp=<比較次數>
linear: <時間> s
binary: <時間> s
=> <較快者> faster
```

### 雷達圖

`assets/radar.png` - 5 維雷達圖，比較線性搜尋（紅色）與二分搜尋（青色）

## 4) 性能分析

根據陣列大小 100,000：

- **線性搜尋**：
  - 平均時間：O(n/2)
  - 最壞情況：O(n)
  - 比較次數：~50,000（平均）

- **二分搜尋**：
  - 平均時間：O(log n)
  - 最壞情況：O(log n)
  - 比較次數：~17（最壞）

**預期結果**：二分搜尋快 1000 倍以上

## 5) 雷達圖解讀

- **線性搜尋勝出**：實作簡易度、小 n 速度（差異不大）
- **二分搜尋勝出**：大 n 速度、最壞情況比較次數
- **無絕對贏家原因**：
  - 場景不同：小陣列用線性，大陣列用二分
  - 前提不同：二分需要排序，線性無需

## 6) 函式簽名

### solution.py

```python
def linear_search(arr: list[int], target: int) -> tuple[bool, int]:
    """線性搜尋
    
    Args:
        arr: 升冪排序的整數陣列
        target: 搜尋目標值
        
    Returns:
        (found, cmp_count) - (是否找到, 比較次數)
    """
    
def binary_search(arr: list[int], target: int) -> tuple[bool, int, int]:
    """二分搜尋
    
    Args:
        arr: 升冪排序的整數陣列
        target: 搜尋目標值
        
    Returns:
        (found, cmp_count, index) - (是否找到, 比較次數, 索引或 -1)
    """
    
def generate_array(size: int) -> list[int]:
    """產生升冪排序陣列
    
    Args:
        size: 陣列大小
        
    Returns:
        [0, 2, 4, ..., 2*(size-1)] 升冪偶數陣列
    """
    
def main() -> None:
    """主程式：讀入陣列、執行搜尋、輸出結果、性能測試"""
```

### plot.py

```python
def calculate_metrics(times_linear: float, times_binary: float,
                      cmp_linear: int, cmp_binary: int) -> tuple[list, list]:
    """計算雷達圖 5 維指標
    
    Args:
        times_linear: 線性搜尋耗時
        times_binary: 二分搜尋耗時
        cmp_linear: 線性搜尋比較次數
        cmp_binary: 二分搜尋比較次數
        
    Returns:
        (linear_metrics, binary_metrics) - 各 5 維指標 0-1 正規化值
    """
    
def plot_radar() -> None:
    """繪製並保存雷達圖到 assets/radar.png"""
```

## 7) 輸入邊界與約束

| 參數 | 最小值 | 最大值 | 說明 |
|-----|--------|--------|------|
| K (目標值) | 0 | 199,998 | 搜尋目標，此題為 156 |
| 陣列大小 | 1 | 100,000+ | 此題預設 100,000 |
| 陣列元素 | 0 | 2*(size-1) | 偶數升冪序列 |
| n (timeit 次數) | 1 | ∞ | 預設 100 |

**有效範圍**：
- 陣列長度 ≥ 1（至少 1 個元素）
- K 在 [0, 2*(size-1)] 範圍內
- 陣列必須升冪排序（binary_search 前提條件）

## 8) 例外處理

### 已實作

**binary_search()** 內部邊界檢查：
```python
if left > right:  # 搜尋空間已排除，不存在
    return (False, cmp_count, -1)
```

**generate_array()** 安全檢查：
```python
if size <= 0:  # 防止陣列大小無效
    return []
```

**plot.py** 文件夾創建：
```python
os.makedirs('assets', exist_ok=True)  # 若無則創建，已存在則跳過
```

### 未實作但可加強

- ✗ 空陣列檢查：`if not arr: raise ValueError("陣列為空")`
- ✗ 型態驗證：`isinstance(arr, list)`, `isinstance(target, int)`
- ✗ 排序驗證：`if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)): raise ValueError("陣列未排序")`

## 9) Edge Cases

### 測試過

| Edge Case | 預期行為 | 實作狀態 |
|-----------|---------|---------|
| **K 在陣列最前** | 兩者都快速找到 (idx=0) | ✅ test_custom_array() |
| **K 在陣列最後** | 線性搜尋需完整掃描, 二分快速 | ✅ test_target_in_array() |
| **K 不在陣列中** | 兩者都回傳 (False, cmp_count, -1) | ✅ test_solution.py |
| **單元素陣列 [K]** | 兩者都直接找到 | ✅ test_custom_array() |
| **K 為最小值 0** | 正確處理 (已在 [0, 2, 4...] 中) | ✅ |
| **K 為最大值** | 正確處理 (通常 2*99999=199998) | ✅ |

### 未測試但可能發生

| Edge Case | 情況 | 建議 |
|-----------|------|------|
| **空陣列** | `arr = []` | 加 raise ValueError |
| **重複元素** | `arr = [2, 2, 2, 4]` | 目前實作仍可處理 (回傳任一索引) |
| **非升冪排序** | `arr = [4, 2, 1]` | 二分搜尋會失效, 加排序驗證 |
| **K 為浮點數** | `target = 156.5` | 加型態檢查 isinstance(target, int) |
| **超大陣列** | size = 10,000,000 | 記憶體限制, 目前 100,000 足夠 |
| **負數目標** | `target = -1` | 此題陣列無負數, 邏輯上可正常回傳 False |

## 10) 性能上的設計考量

**為何用偶數陣列 [0, 2, 4, ..., 2*(size-1)]？**
- K = 156 一定在陣列中（確保測試的確定性）
- 避免複雜的隨機陣列生成
- 便於驗證二分搜尋的正確性

**為何 timeit 迴圈 100 次？**
- 足以消除系統抖動
- 顯著揭示大規模陣列的性能差異
- 合理執行時間（數秒內完成）

**為何保留搜尋中的比較次數計數？**
- 驗證演算法複雜度（線性 O(n) vs 二分 O(log n)）
- 雷達圖第 5 維「最壞情況比較次數」的依據
- 教育意義：讓學生看到理論與實踐的一致性