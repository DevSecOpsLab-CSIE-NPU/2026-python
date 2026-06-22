# AI_LOG - Data Cleaning

## 開工前 Checklist

| 項目 | 回答 |
|------|------|
| ① 函式簽名 | `clean_data(nums: list[int], d: int) -> list[int]`，吃整數串列與除數 D，回傳處理後的整數串列。 |
| ② 輸入邊界 | `n` (1 ≤ n ≤ 10⁵)，整數值無明確上限（在 Python int 範圍內），讀到 `n=0` 結束（非 EOF）。 |
| ③ 例外處理 | 空行自動跳過；`n=0` 立即結束不輸出該行；非法格式（非整數）暫不處理。 |
| ④ edge case | `n=1` 單一數可被 D 整除 / 不可被 D 整除；全部重複（`2 2 2 2`）→ 去重後剩 `2`；全部被 D 剔除 → `NONE`；含 0（`0 % 2 == 0`，應保留）。 |
| ⑤ 驗收標準 | D = **2**。輸出以空白分隔，無結果輸出 `NONE`，與範例輸出完全一致即通過。 |

## 實作摘要

- 先去重（保留首次出現順序）→ 篩選能被 D 整除 → 排序
- 多組測資以 `n=0` 終止
- 測試涵蓋正常、邊界、全部剔除、負數、零、重複等 15 個案例，全數通過

---

## Task 2 - Caesar Cipher

### 開工前 Checklist

| 項目 | 回答 |
|------|------|
| ① 函式簽名 | `caesar_encrypt(text: str, shift: int) -> str`，吃字串與位移數，回傳加密後字串。 |
| ② 輸入邊界 | 多行文字，讀到 EOF 結束，無行數上限。 |
| ③ 例外處理 | 空行直接輸出空行；非英文字元原樣保留。 |
| ④ edge case | 空字串；全非英文字元（`123 !@#`）；大寫 `Z` + shift 繞回 `A`；小寫 `z` + shift 繞回 `a`；shift 很大時需 mod 26。 |
| ⑤ 驗收標準 | SHIFT = **9**。大寫 A~Z 循環，小寫 a~z 循環，非英文字元不變。 |

### 實作摘要

- 依 `chr((ord(ch) - base + shift) % 26 + base)` 計算每個英文字母的位移
- 大寫/小寫分別處理，非字母原樣保留
- 測試涵蓋範例、繞回、非字母、大 shift、空字串等 13 個案例，全數通過

---

## Task 3 - Digit Root (任意進位數字根)

### 開工前 Checklist

| 項目 | 回答 |
|------|------|
| ① 函式簽名 | `digit_root(x: int, base: int) -> int`，吃十進位整數與 base，回傳數字根（十進位）。 |
| ② 輸入邊界 | `x` (0 ≤ x ≤ 10⁹)，多行至 EOF。 |
| ③ 例外處理 | 空行跳過；x=0 → 數字根為 0。 |
| ④ edge case | x=0 → 回 0；x 本身已 < base（如 base=13, x=5）；x 是 base 的冪（如 base=13, x=169 → "100" → 1+0+0=1）；大數如 999999999。 |
| ⑤ 驗收標準 | base = **13**。重複轉進位→加總，直到一位數，以十進位輸出。 |

### 實作摘要

- 演算法：`x >= base` 時，反覆 `x % base` 取各位數加總，直到 `x < base`
- 測試涵蓋 base=8 樣例、base=13 邊界、base=2 與 base=16 跨 base 驗證，共 14 案例，全數通過

---

## Task 4 - Binary Search Performance (二分搜尋效能)

### 開工前 Checklist

| 項目 | 回答 |
|------|------|
| ① 函式簽名 | `binary_search(arr: list[int], target: int) -> tuple[bool, int]`；`linear_search(arr, target) -> tuple[bool, int]`；`timeit_compare(arr, target, number) -> dict`。 |
| ② 輸入邊界 | 陣列升冪排序，長度 ≥ 10⁵，元素整數。K = 100 + 學號末兩碼。 |
| ③ 例外處理 | 空陣列 → NOT FOUND cmp=0；K 超出範圍 → 正常回傳未找到。 |
| ④ edge case | K 是第一個/最後一個元素；K 不存在但介於範圍內；陣列長度 1、2；所有元素相同。 |
| ⑤ 驗收標準 | 學號末兩碼 = **18** → K = **118**。輸出：FOUND idx cmp=次數 / NOT FOUND cmp=次數 + timeit 兩行 + 雷達圖 assets/radar.png。 |

### 實作摘要

- 二分搜尋：標準 lo/hi 指針，記錄比較次數；線性搜尋：逐一比對
- timeit 量測 100 次迭代，輸出兩者耗時與較快者
- 雷達圖：5 維度（小 n 速度、大 n 速度、實作簡易度、最壞比較次數、需先排序），min-max 正規化後以 matplotlib 極座標繪製
- 測試 9 案例全通，實測 100k 陣列查 K=118 → cmp=16，二分較快
