# AI_LOG.md — 期末考（Week 18）

## 題目一：資料清理 (Data Cleaning)

### 5 步驟流程記錄

| 步驟 | 說明 | 狀態 |
|------|------|------|
| ① 設計測試 | 設計 3 組測試（一般、無偶數 NONE、單一負偶數邊界） | ✅ |
| ② 寫程式並跑測試 | 寫出 `D2_easy.py` 並通過 3 組測試 | ✅ |
| ③ 加中文註解 | `D2_easy.py` 每行關鍵邏輯加上中文註解 | ✅ |
| ④ 製作簡易版 | 產出 `D2-easy.py`（邏輯乾淨、變數直覺、`dict.fromkeys` 去重） | ✅ |
| ⑤ 加詳細註解 | 加入 docstring、時間 O(N log N)／空間 O(N) 複雜度說明 | ✅ |

### 手打版

`D2-handwritten.py` — 變數名稱與迴圈改為 basic 風格，無註解，通過全部測試。

### TDD 紅綠燈 Commit

```
508f2be test: add failing tests for Data Cleaning  ← 紅燈（3 FAILED）
65ddfad feat: implement Data Cleaning               ← 綠燈（3 passed）
```

Sample Input：`8\n4 7 4 2 9 2 6 7` → 預期輸出 `2 4 6` ✅（學號末碼 8 → D=2）

---

## 題目二：凱撒密碼 (Caesar Cipher)

### 解題重點

| 項目 | 說明 |
|------|------|
| 位移量 SHIFT | 學號末碼 8 → (8 % 4) + 2 = 2？不，本題直接代入 SHIFT = 9（老師指定） |
| 輸入方式 | `sys.stdin.read().splitlines()` 讀到 EOF |
| 大小寫處理 | 大寫 A-Z 循環，小寫 a-z 循環 |
| 非字母處理 | 空白、數字、標點原樣保留 |
| 時間複雜度 | O(N)，N = 總字元數 |
| 空間複雜度 | O(N) |

### 測試案例（5 組）

| 測試 | 輸入 | 預期輸出 | 結果 |
|------|------|----------|------|
| Sample | `Hello, NPU!` / `abc XYZ` | `Qnuux, WYD!` / `jkl GHI` | ✅ |
| 空字串 | `""` | `""` | ✅ |
| 非字母 | `123 !@#` | `123 !@#` | ✅ |
| 小寫繞圈 | `z` | `i` (z→i, shift 9) | ✅ |
| 大寫繞圈 | `Z` | `I` (Z→I, shift 9) | ✅ |

### TDD 紅綠燈 Commit

```
7d28208 test: add failing tests for Caesar Cipher  ← 紅燈（4 FAILED）
3f382f2 feat: implement Caesar Cipher               ← 綠燈（5 passed）
```

---

## 完整檔案清單

```
weeks/week-18/solutions/48/
├── D2_easy.py            ← 資料清理：簡易版含中文註解
├── D2-easy.py             ← 資料清理：AI 簡易版含詳細註解與複雜度
├── D2-handwritten.py      ← 資料清理：手打版（無註解）
├── test_D2.py             ← 資料清理：測試程式
├── test_D2.log            ← 資料清理：pytest LOG
├── test_D2-handwritten.log ← 資料清理：手打版測試 LOG
├── C2_easy.py            ← 凱撒密碼：含實作與中文註解
├── C2-easy.py             ← 凱撒密碼：AI 詳細註解版（含 docstring、複雜度）
├── C2-handwritten.py      ← 凱撒密碼：手打版（無註解）
├── test_C2.py             ← 凱撒密碼：測試程式（5 cases）
├── test_C2.log            ← 凱撒密碼：pytest LOG
├── test_C2-handwritten.log ← 凱撒密碼：手打版測試 LOG
└── AI_LOG.md              ← 本檔案
```

## TDD 紅綠燈 Commit 一覽（按時間順序）

```
508f2be test: add failing tests for Data Cleaning   ← D1 紅燈
65ddfad feat: implement Data Cleaning                ← D1 綠燈
8acc8a1 chore: add AI log, easy version, and handwritten version  ← D1 其餘檔案
53aa902 chore: add test log files                   ← D1 LOG
7d28208 test: add failing tests for Caesar Cipher   ← D2 紅燈
3f382f2 feat: implement Caesar Cipher                ← D2 綠燈
```
