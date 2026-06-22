# AI_LOG.md — 期末考（Week 18）

## 檔案結構一覽

```
solutions/48/
├── A01_easy.py           ← A區① 資料清理（詳細註解版，D=2）
├── A01_handwritten.py    ← A區① 資料清理（手打版）
├── A01_test.py           ← A區① 測試程式（7 cases）
├── test_A01.log
├── test_A01-handwritten.log
├── C2_easy.py            ← A區② 凱撒密碼（含中文註解，SHIFT=9）
├── C2-easy.py            ← A區② 凱撒密碼（詳細註解版）
├── C2-handwritten.py     ← A區② 凱撒密碼（手打版）
├── test_C2.py            ← A區② 測試程式（5 cases）
├── test_C2.log
├── test_C2-handwritten.log
├── B13_easy.py           ← B區③ Base-13 數字根（含中文註解，BASE=13）
├── B13-easy.py           ← B區③ Base-13 數字根（詳細註解版）
├── B13-handwritten.py    ← B區③ Base-13 數字根（手打版）
├── B13_test.py           ← B區③ 測試程式（9 cases）
├── test_B13.log
├── test_B13-handwritten.log
└── AI_LOG.md
```

---

## A區① — 資料清理 (Data Cleaning)

| 項目 | 說明 |
|------|------|
| D 值 | 學號末碼 8 → 8 % 4 + 2 = **2** |
| 三步驟 | ① 去重（dict.fromkeys）② 篩選 %D==0 ③ 排序 |
| 複雜度 | 時間 O(N log N)／空間 O(N) |

### 測試案例（7 組）

| 測試 | 輸入 | 預期輸出 | 類型 |
|------|------|---------|------|
| sample_1 | `4 7 4 2 9 2 6 7` | `2 4 6` | 題目範例 |
| sample_2 | `1 3 5` | `NONE` | 題目範例 |
| all_even_dup | `2 4 2 6 4 8` | `2 4 6 8` | 重複處理 |
| single_even | `-8` | `-8` | 單一偶數 |
| single_odd | `7` | `NONE` | 單一奇數 |
| negative_even | `-4 6` | `-4 6` | 含負數 |
| multiple_groups | 兩組合併 | `2 4 6` / `NONE` | 多組 |

---

## A區② — 凱撒密碼 (Caesar Cipher) — ✅ 已完成

| 項目 | 說明 |
|------|------|
| SHIFT | **9** |
| 輸入 | `sys.stdin.read().splitlines()` 讀到 EOF |
| 大小寫 | A-Z / a-z 各自循環 |
| 非字母 | 原樣保留 |
| 複雜度 | 時間 O(N)／空間 O(N) |

### Commit 紀錄

```
7d28208 test: add failing tests for Caesar Cipher   ← 🔴
3f382f2 feat: implement Caesar Cipher                ← 🟢
c9538d3 chore: add remaining Caesar Cipher files
```

---

## B區③ — Base-13 數字根 (Digital Root) — 🟢 已綠燈

| 項目 | 說明 |
|------|------|
| BASE | **13**（硬編碼） |
| 核心邏輯 | 轉 13 進位 → 拆位相加 → 重複到 < 13 |
| 特例 | x=0 → 直接輸出 0 |
| 複雜度 | 時間 O(log₁₃ x)／空間 O(1) |

### 驗證範例

```
63 → 63÷13=4 餘11 → 4+11=15 → 15÷13=1 餘2 → 1+2=3 → 輸出 3 ✅
```
