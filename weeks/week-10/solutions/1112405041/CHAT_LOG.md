# CHAT_LOG.md — Week 10 開發訪談記錄

## 2026/06/20 Session

### 開發目標
- 完成 Week 10 HOMEWORK.md Task 1（CSV→JSON）+ Task 2（JSON→XML）+ Task 3（長條圖比較）
- 比照 Week 16/17 的五階段 TDD 紀律（test: → feat: 交替）
- 學號：1112405041，目錄：`weeks/week-10/solutions/1112405041/`

### 階段記錄

#### Stage 1 — @timeit 裝飾器
- 先在兩個 task 檔案共用同一個 `@timeit` 裝飾器
- 用 `functools.wraps` 保留原函式 metadata，`time.perf_counter` 計時

#### Stage 2 — Task 1：CSV → JSON
- **read_csv**：用 csv.DictReader 實作，檔案不存在讓 Python 自然拋錯
- **filter_by_admission**：根據 admission 欄位篩選指定入學方式
- **count_by_dept**：依科系（dept）計數，保留空字串科系（用 `is not None` 而非 `if dept:`）
- **write_json**：用 json.dump 輸出，自動建立所需目錄
- 遇到 bug：write_json 簽名第一次少寫 filepath 參數，測試直接報 TypeError

#### Stage 3 — Task 2：JSON → XML
- **read_json**：json.load 讀檔，malformed JSON 時拋自訂 `JSONReadError`
- **build_xml_tree**：用 xml.etree.ElementTree 從 list 建出 XML 樹
- 遇到 bug：AI 給的程式假設 data 是 `{"students": [...]}`，但 read_json 回傳純 list，執行後 AttributeError，修正為直接 iter list
- **write_xml**：ElementTree.indent + tree.write 輸出

#### Stage 4 — Task 3：視覺化比較
- **plot_comparison**：用 matplotlib 畫水平長條圖，比較各操作耗時
- 存入 timing_comparison.png

#### Stage 5 — 安全掃描
- 將各檔案的 `import os` 搬到檔案最上方（符合 PEP8 模組層級 import）
- count_by_dept 加入 type annotation（`data: dict[str, int]`）確保傳入型別正確
- 用 `is not None` 取代 `if dept:` 避免空字串被跳過
- 確認 write_json 使用 json 模組而非 pickle

### 測試結果
最終 29 個測試全部通過，三支 task 腳本均可獨立執行產出結果。
