# 作業完成報告 - Week 02 回家作業

## 完成狀態 ✓

- [x] **Task 1: Sequence Clean** - 實作序列去重、排序、過濾
- [x] **Task 2: Student Ranking** - 實作複合規則排序
- [x] **Task 3: Log Summary** - 實作統計和計數
- [x] **測試骨架** - 30個測試函式（每題12/9/9個）
- [x] **文檔完成** - README / TEST_CASES / TEST_LOG / AI_USAGE

---

## 執行方式

### 環境要求

```
Python 版本：3.7+（推薦 3.9 或以上）
依賴：無（使用Python內建的unittest、collections）
```

### 程式執行

#### Task 1：序列清理
```bash
python task1_sequence_clean.py
```
**執行結果**：輸出預設測試案例的結果
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

#### Task 2：學生排名
```bash
python task2_student_ranking.py
```
**執行結果**：輸出預設測試案例的前3名排序結果
```
eva 92 20
zoe 92 21
bob 88 19
```

#### Task 3：日誌統計
```bash
python task3_log_summary.py
```
**執行結果**：輸出使用者事件統計和最常見動作
```
bob 4
alice 3
chris 1
top_action: login 3
```

### 測試執行

運行所有單元測試（30個測試）：
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

預期結果：
```
Ran 30 tests in 0.005s

OK
```

運行特定任務測試：
```bash
python -m unittest tests.test_task1 -v
python -m unittest tests.test_task2 -v
python -m unittest tests.test_task3 -v
```

### 交互式測試（選擇性）

可在Python REPL中測試單個函式：
```python
from task1_sequence_clean import process_sequence, format_output
result = process_sequence("5 3 5 2 9 2 8 3 1")
print(format_output(result))
```

---

## 資料結構選擇理由

### Task 1：Sequence Clean

**選擇**：`set`（用於去重追蹤）+ `list`（存儲結果）

**理由**：set提供O(1)的成員檢查，配合list保留插入順序。這種方式既高效（時間O(n)）又易理解，符合「去重但保留順序」的需求。

---

### Task 2：Student Ranking

**選擇**：`Student`類別 + `lambda tuple`複合排序鍵

**理由**：Student類別提升代碼語義性（比tuple[0]/tuple[1]易讀），tuple作為key利用字典序自動實現多層排序，無需複雜的自定義comparator。

---

### Task 3：Log Summary

**選擇**：`Counter`（計數）+ `dict`（儲存結果）

**理由**：Counter直接支援計數和most_common()，比defaultdict更簡潔；sorted()配合tuple key實現複合排序（事件數、名稱），避免複雜的嵌套dict。

---

## 遇到的錯誤與修正

### 錯誤案例：Task 2的排序順序反向

**發生時刻**：第一次實作rank_students()時

**錯誤代碼**：
```python
# 錯誤：age應遞增但寫成遞減
key=lambda s: (-s.score, -s.age, s.name)
```

**症狀**：
- 同分的學生按age遞減排序（老的排前面）
- 測試失敗：bob(19歲) 應在alice(20歲)前面，但結果反了

**修正方式**：
- 移除age前的負號，改為 `key=lambda s: (-s.score, s.age, s.name)`
- 理由：age本就應遞增（小到大），不需負號

**驗證**：
```bash
python -m unittest tests.test_task2.test_rank_students_secondary_sort -v
# 從FAIL變成OK
```

**學到的教訓**：複合排序時，明確區分哪層遞增/遞減。負號的意義是「反轉順序」，不是「每層都用」。

---

## Red → Green → Refactor 過程

### Task 1：Sequence Clean

#### Red 階段
- 測試先寫好：12個測試（4個函式 × 3個案例）
- 預期失敗：ImportError（模組不存在）
- 輸出：0 passed, 12 failed

#### Green 階段
- 實作基本函式：`deduplicate`, `sort_asc`, `sort_desc`, `filter_evens`
- 每個函式單一職責，直接寫最簡實現
- 所有測試通過（12 passed）

#### Refactor 階段
- 添加`process_sequence()`和`format_output()`整合流程
- 添加型態提示（遵循PEP 484）
- 添加文件字串說明每個函式用途
- 驗證測試仍全綠✓

### Task 2：Student Ranking

#### Red 階段
- 9個測試涵蓋：解析資料、基本排序、複合規則（同分、同齡）
- 預期失敗：ImportError（Student類別不存在）
- 輸出：0 passed, 9 failed

#### Green 階段
- 先實作`Student`類別和`parse_students()`解析
- 簡單實作`rank_students()`用sorted()
- 初版成功通過大部分測試，但age排序有誤（見上面的錯誤案例）
- 修正age排序鍵的負號後，9個測試全過

#### Refactor 階段
- 提升代碼可讀性：提取`process_ranking()`函式
- 添加__repr__便於調試輸出
- 驗證測試仍全綠✓

### Task 3：Log Summary

#### Red 階段
- 9個測試涵蓋：計數、top action、邊界情況（空輸入）
- 預期失敗：ImportError（函式不存在）
- 輸出：0 passed, 9 failed

#### Green 階段
- 實作`count_user_actions()`用Counter
- 實作`find_top_action()`用Counter.most_common()
- 簡單實作`process_logs()`完整流程
- 初版測試大部分通過，但邊界情況（m=0）需處理

#### Refactor 階段
- 添加邊界檢查：`if m == 0` 提早返回
- 清理輸出格式，確保無action時輸出"none"
- 優化排序邏輯，確保同數時名稱字母序遞增
- 驗證測試仍全綠✓

---

## 測試結果總結

### 執行次數
- **第一次（Red）**：0 passed, 30 failed（在實作前）
- **第二次（Green）**：30 passed, 0 failed（實作+修正後）
- **最終驗證**：30 passed, 0 failed✓

### 測試覆蓋
- **正常情況**：10個測試（每題3-4個）
- **邊界情況**：9個測試（空、單一、極端値）
- **反例/複雜**：11個測試（同分、複合條件、順序）
- **總計**：30個測試函式

### 品質指標
- 代碼行數：~100行（實作）+ ~200行（測試）
- 循環複雜度：低（主要邏輯都在sorted()和Counter)
- 測試通過率：100%✓

---

## 自評與反思

### 優點
1. ✓ 遵循TDD流程（先寫測試，再實作，最後重構）
2. ✓ 測試案例設計完整（包括邊界和反例）
3. ✓ 代碼簡潔可讀（利用Python內建工具，避免重複邏輯）
4. ✓ 文檔齊全（README、TEST_CASES、TEST_LOG、AI_USAGE）

### 改進空間
1. 可加入更多異常處理（如輸入格式驗證）
2. Task 2可支援可變k值（目前流程固定）
3. Task 3可添加時間序列分析（目前只統計計數）

### 學習要點
1. tuple排序的優雅性（優於多次sorted()或自定義comparator）
2. Counter的功能與限制（計數強，但不自動排序）
3. 批判性使用AI（驗證建議，拒絕不適合的模式）

---

## 文件清單

```
weeks/week-02/solutions/1114405048/
├── task1_sequence_clean.py       # Task 1實作
├── task2_student_ranking.py      # Task 2實作
├── task3_log_summary.py          # Task 3實作
├── tests/
│   ├── test_task1.py             # 12個Test Case
│   ├── test_task2.py             # 9個Test Case
│   └── test_task3.py             # 9個Test Case
├── TEST_CASES.md                 # 15組測資設計文檔
├── TEST_LOG.md                   # 測試執行日誌（Red → Green）
├── AI_USAGE.md                   # AI使用記錄與反思
└── README.md                     # 本檔案
```

---

## 提交檢查清單

- [x] 所有Python檔案可執行（無語法錯誤）
- [x] 所有測試通過（30/30）
- [x] 測試骨架由學生自行撰寫（非複製）
- [x] 未修改禁止路徑（QUESTION-*.md、week-02/README.md等）
- [x] 包含完整文檔（README、TEST_CASES、TEST_LOG、AI_USAGE）
- [x] 分支與PR符合規範（submit/week-02）

---

## 聯繫與問題

如使用過程中遇到問題，可參考：
- `AI_USAGE.md`：了解實作中的設計決策
- `TEST_CASES.md`：查看各類測資範例
- `TEST_LOG.md`：追蹤測試演進過程

