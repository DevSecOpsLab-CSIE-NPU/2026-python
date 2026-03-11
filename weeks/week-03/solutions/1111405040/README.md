# Week 03 作業總結

## 基本資訊

- **學號**：1111405040
- **週次**：Week 03
- **提交日期**：2026-03-11
- **完成狀態**：5 題皆已完成

---

## 作業內容

### 五題概覽

| 題號 | 主題 | 核心概念 |
|------|------|---------|
| **QUESTION-100** | The 3n + 1 Problem | Collatz 序列、記憶化快取 |
| **QUESTION-118** | Mutant Flatworld Explorers | 座標模擬、方向轉換、scent 機制 |
| **QUESTION-272** | TEX Quotes | 字元掃描、引號交替替換 |
| **QUESTION-299** | Train Swapping | 相鄰交換次數、反轉數 |
| **QUESTION-490** | Rotating Sentences | 文字矩陣旋轉、補空白對齊 |

---

## 交付檔案清單

```text
weeks/week-03/solutions/1111405040/
├── question_100.py              Collatz 最大週期長度
├── question_118.py              機器人移動與掉落判定
├── question_272.py              雙引號轉換為 TeX 引號
├── question_299.py              最少相鄰交換次數
├── question_490.py              文字順時針旋轉 90 度
├── tests/
│   ├── test_question_100.py     5 個測試函式
│   ├── test_question_118.py     3 個測試函式
│   ├── test_question_272.py     3 個測試函式
│   ├── test_question_299.py     5 個測試函式
│   └── test_question_490.py     3 個測試函式
├── TEST_CASES.md                測試案例與覆蓋說明
├── TEST_LOG.md                  測試執行紀錄
├── AI_USAGE.md                  AI 協助與人工驗證說明
└── README.md                    本檔案
```

**總計**：5 個解題檔、5 個測試檔、4 份文件、19 個測試函式

---

## 核心實作

### QUESTION-100：The 3n + 1 Problem

**題目重點**：對每組 `i, j`，找出區間 `[min(i, j), max(i, j)]` 的最大 cycle length。

**核心作法**：
```python
def collatz_cycle_length(n, cache):
    original = n
    path = []
    while n not in cache:
        path.append(n)
        n = 3 * n + 1 if n % 2 else n // 2
    length = cache[n]
    for value in reversed(path):
        length += 1
        cache[value] = length
    return cache[original]
```

**測試覆蓋**：5 個（基底、已知值、區間、反向輸入、範例整合）

---

### QUESTION-118：Mutant Flatworld Explorers

**題目重點**：模擬多台機器人在邊界內移動，處理 LOST 與 scent。

**核心作法**：
- 使用方向映射處理 `L` / `R`。
- `F` 前進時先判斷是否越界。
- 若越界且當前座標已有 scent，忽略該次前進。
- 若越界且無 scent，機器人標記 LOST 並留下 scent。

**測試覆蓋**：3 個（scent 機制、官方範例、重複掉落保護）

---

### QUESTION-272：TEX Quotes

**題目重點**：將輸入中的 `"` 依序替換為 `` 與 ''。

**核心作法**：
- 維護 `opening` 布林值。
- 每遇到一個 `"` 就交替輸出開/關引號。
- 其他字元與換行原樣保留。

**測試覆蓋**：3 個（單行、多行、無引號）

---

### QUESTION-299：Train Swapping

**題目重點**：計算最少相鄰交換次數。

**核心作法**：
- 以 bubble-sort 風格計數交換次數。
- 相鄰交換的最少次數即反轉數。
- 輸出句型固定為 `Optimal train swapping takes S swaps.`

**測試覆蓋**：5 個（已排序、反向、基本案例、多測資、`L=0`）

---

### QUESTION-490：Rotating Sentences

**題目重點**：將多行文字順時針旋轉 90 度。

**核心作法**：
- 先以最長行長度將各行右補空白。
- 按欄位由上到下（旋轉後為由左到右）組合字元。
- 每行結果 `rstrip()` 去除右側補位空白。

**測試覆蓋**：3 個（基本旋轉、不等長行、空輸入）

---

## 測試與驗證

### 單元測試

```bash
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

結果：
- 測試總數：19
- 通過：19
- 失敗：0

### 手動範例驗證

五題皆以題目範例輸入執行，輸出與預期一致。
詳細內容記錄於 `TEST_LOG.md`。

---

## 執行方式

### 方法 1：執行全部測試

```bash
cd weeks/week-03/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 方法 2：執行單一題目

```bash
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_100.py < input.txt
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_118.py < input.txt
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_272.py < input.txt
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_299.py < input.txt
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe question_490.py < input.txt
```

---

## 學習重點

1. 將題目敘述拆解為可測試函式。
2. 先驗證輸出格式，再調整演算法細節。
3. 對邊界情況建立明確測試（如反向區間、空輸入、`L=0`）。
4. 保持程式可讀性與可維護性（函式分工、命名一致）。
