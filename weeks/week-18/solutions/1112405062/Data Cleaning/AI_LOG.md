# AI_LOG.md — 期末考歷程記錄

## 題目
對每一組整數數列，依序完成：
1. 去重複（保留第一次出現的順序）
2. 只保留能被 D 整除的數（D = 4）
3. 由小排到大

## 函式簽名
```python
def process(nums: list[int], D: int = 4) -> list[int]
```

## 討論歷程

### Step 1 — 規格確認
- 確認 D = 4 固定
- 確認多組測資輸入格式（n 行 + 數列行，n=0 結束）
- 輸出格式：空格分隔，無結果時輸出 NONE

### Step 2 — Test Case 拆解（6 個）
| # | 情境 | 輸入 | 預期輸出 |
|---|------|------|---------|
| 1 | 基本流程 | `[1,4,4,8,3]` | `[4,8]` |
| 2 | 全數篩掉 | `[1,2,3]` | `[]` |
| 3 | 全部重複 | `[4,4,4,4]` | `[4]` |
| 4 | 負數 | `[-4,4,-8,8]` | `[-8,-4,4,8]` |
| 5 | 空輸入 | `[]` | `[]` |
| 6 | 單一元素 | `[4]` | `[4]` |

### Step 3 — 紅燈確認
- 測試 6 項：4 項紅燈（預期有值但 stub 回傳 `[]`）、2 項 pass（預期 `[]`）
- commit: `test: add process function test cases`

### Step 4 — 實作綠燈
- 去重：用 set + 保持順序
- 篩選：`x % D == 0`
- 排序：`list.sort()`
- 6/6 測試通過
- commit: `feat: implement process function`

## 結果
- 測試全數通過 ✅


## Caesar Cipher（Caesar Cipher/）

### 題目
將每行字串中的英文字母向後移位 SHIFT = 3：
- 大寫 A-Z 內循環
- 小寫 a-z 內循環
- 非英文字母原樣保留

### 函式簽名
```python
def caesar_encrypt(text: str, shift: int = 3) -> str
```

### Test Case（7 個）
| # | 情境 | 輸入 | 預期輸出 |
|---|------|------|---------|
| 1 | 大小寫混合 | `"Hello, NPU!"` | `"Khoor, QSX!"` |
| 2 | 純小寫 | `"abc"` | `"def"` |
| 3 | 大寫繞圈 | `"XYZ"` | `"ABC"` |
| 4 | 含非字母字元 | `"abc123! xyz"` | `"def123! abc"` |
| 5 | 空字串 | `""` | `""` |
| 6 | 僅非字母 | `"123 !@#"` | `"123 !@#"` |
| 7 | 小寫繞圈 / 大寫繞圈 | `"z"`, `"Z"` | `"c"`, `"C"` |

### 紅燈確認
- 7 項測試：6 項紅燈、1 項 pass（空字串）
- commit: `test: add caesar_encrypt test cases`

### 實作綠燈
- 用 `ord()` / `chr()` + mod 26 循環移位
- 7/7 測試通過
- commit: `feat: implement caesar_encrypt function`

## ## Hex Digit Root（Hex Digit Root/）

### 題目
對每個輸入的十進位非負整數 x，先換算成 base=16 進位，將各位數字相加得到新數；重複此步驟直到結果為個位數（在 base 進位下的個位數），最終以十進位輸出最終的數字根。
- 多筆輸入，讀到 EOF 結束。
- 輸入 0 的數字根為 0。

### 函式簽名
```python
def get_hex_digit_root(x: int) -> int

```

### Test Case（4 個）

| # | 情境 | 輸入 | 預期輸出 |
| --- | --- | --- | --- |
| 1 | 特例處理 | `0` | `0` |
| 2 | 個位數邊界 | `8` | `8` |
| 3 | 基本案例 | `63` | `3` |
| 4 | 大數邊界（Edge Case） | `1000000000` | `10` |

### 紅燈確認

* 4 項測試：4 項紅燈
* commit: `test: add failing tests for hex digit root`

### 實作綠燈

* 用 `while x >= 16` 進行位數收斂，內部透過 `% 16` 與 `//= 16` 拆解加總各位數數值
* 搭配 `sys.stdin` 處理多筆輸入直到 EOF 結束
* 4/4 測試通過
* commit: `feat: implement hex digit root with eof support`
