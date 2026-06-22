# AI_LOG

## Q1 Data Cleaning

### 我問 AI 什麼

我請 AI 依照學號參數 `D=3`，分析資料清理題的函式簽名、輸入邊界、例外、edge case、測試與實作方式。

### AI 建議什麼

AI 建議把流程拆成 `dedupe_keep_order`、`filter_divisible`、`clean_numbers`、`solve`，先測試去重保序，再測試篩選與排序，並補 `NONE`、負數、0、多組測資與 `n=1`。

### 我如何修改

我確認 D 是 3，補了數量不符合 `n`、`d=0`、缺少資料列的例外檢查。也確認 EOF 與 `n=0` 結束行為正確，輸出不會多出空白。

## Q2 Caesar Cipher

### 我問 AI 什麼

我請 AI 依照 `SHIFT=10` 完成 Caesar cipher，並確認大小寫循環、非英文字保留與空行處理。

### AI 建議什麼

AI 建議先寫 `shift_char` 測單一字元，再用 `caesar_line` 與 `solve` 測整行和多行 EOF。測試要包含 `z/Z` wraparound、標點、空白、數字與空行。

### 我如何修改

我確認 `shift` 先對 26 取餘數，讓大於 26 的 shift 也正常。`solve` 使用 `splitlines()` 保留中間空行，並讓一行輸入對應一行輸出。

## Q3 Digital Root in Base

### 我問 AI 什麼

我請 AI 依照 `base=6` 設計任意進位數字根，特別確認輸入 0 不是結束，而是要輸出 0。

### AI 建議什麼

AI 建議拆成 `to_base_digits`、`digit_sum_in_base`、`digital_root_in_base`、`solve`，並驗證合法 base 集合、負數例外、大數與多行 EOF。

### 我如何修改

我確認 base 是 6，補了合法 base 檢查與負數 `ValueError`。測試時我重新用 base-1 規則檢查大數，發現 `1_000_000_000` 的 base 6 數字根應是 5，因此修正手算期望值，確保測試符合規格。

## Q4 Search Performance

### 我問 AI 什麼

我請 AI 依照 `K=129` 完成 linear search、binary search、timeit benchmark、比較次數與 radar.png 產生。

### AI 建議什麼

AI 建議搜尋函式回傳 `(found, idx, cmp)`，benchmark 另回傳 timeit 秒數，雷達圖比較搜尋速度、比較次數、是否需要排序、實作簡易度與最壞情況效率。

### 我如何修改

我確認 K 是 129，補了空陣列、單一元素、找不到、K 在第一個和最後一個的 edge case。也確認 `q4/assets/radar.png` 可以由 `create_radar_chart` 產生，並用 unittest 檢查檔案存在且大小大於 0。

## TDD 與整體檢查

- 我先建立 `test_*.py`，在尚未實作時確認 Red。
- 我完成 `q1.py` 到 `q4.py` 後確認 Green。
- 我檢查 EOF、多組輸入、空行、edge case 與例外處理。
- 我調整 Q4 輸出格式，包含 `FOUND/NOT FOUND`、`idx`、`cmp`、timeit 秒數與較快策略。
- 我確認 unittest 全部通過。
- 我確認 radar.png 能產生。
