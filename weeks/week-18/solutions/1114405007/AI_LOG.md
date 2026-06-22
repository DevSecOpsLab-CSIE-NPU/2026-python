# AI_LOG.md

## AI 反問我什麼 / 我怎麼回答

### 題1：資料清理
| AI 問 | 我答 |
|-------|------|
| 函式簽名？ | `process_sequence(numbers, D)` → list[int]；`solve(input_text, D)` → str |
| 輸入邊界？ | n ≤ 10⁵，數值 ±10⁹，n=0 結束 |
| 例外處理？ | n=0 直接退出；空行跳過 |
| Edge case？ | 全剔除→NONE；負數/0；全重複 |
| 驗收標準？ | 學號末位 7 → D = (7%4)+2 = 5 |

### 題2：凱撒密碼
| AI 問 | 我答 |
|-------|------|
| 函式簽名？ | `encrypt_line(text, shift)` → str；`solve(input_text, shift)` → str |
| 輸入邊界？ | 多行至 EOF，每行 ≤ 1000 字元 |
| 例外處理？ | 空行原樣保留；非字母不處理 |
| Edge case？ | Z/z 循環回 A/a；整行無字母不變 |
| 驗收標準？ | SHIFT = 8（公式 u%25+1） |

### 題3：數字根
| AI 問 | 我答 |
|-------|------|
| 函式簽名？ | `digit_root(x, base)` → int；`solve(input_text, base)` → str |
| 輸入邊界？ | x ≤ 10⁹，多筆至 EOF |
| 例外處理？ | x=0 數字根=0 |
| Edge case？ | x=0；x<base 直接輸出；10 在 base=11 算一位數 |
| 驗收標準？ | 學號末位 7 → base=11 |

### 題4：二分搜尋
| AI 問 | 我答 |
|-------|------|
| 函式簽名？ | `binary_search(arr, target)` → (idx, cmp)；`linear_search` 同 |
| 輸入邊界？ | 陣列 ≥ 10⁵；K = 100+07 = 107 |
| 例外處理？ | 空陣列 → NOT FOUND cmp=0 |
| Edge case？ | K 在頭/尾；K 大於/小於全部 |
| 驗收標準？ | FOUND/NOT FOUND cmp=N；timeit 兩行+結論 |

## 我問了 AI 什麼（提示詞逐字記錄）
1. 「閱讀 HOMEWORK.md 和 bloom 範例」
2. 「幫我實作我的 D 是 5」
3. 「拆 ≥3 個 test case（含 ≥1 個 edge case），寫測試→確認紅燈→commit，寫實作→跑到綠燈→commit」（每題重複）

## AI 給的建議我有採用
- 去重保序用 set+list（參考 R10-dedupe.py）
- 測試用 unittest 架構
- solve() 設計成可接受字串輸入方便測試
- 數字根用公式 `1+(x-1)%(base-1)`

## AI 給的建議我拒絕
- AI 最初猜測 mapping table 實作 get_D()，改用題目公式修正

## AI 可能誤導但我自行修正的案例
- solve() 空輸入換行處理：修正為有輸出才加換行
- 雷達圖中文標題缺字：改用英文標籤
