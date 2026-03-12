# 執行和使用指南

**完整的 1114405036 專案執行手冊**

---

## 🚀 快速開始 (5 分鐘)

### 第 1 步：進入專案目錄

```bash
cd solutions/1114405036
```

### 第 2 步：執行主程式

```bash
# 執行序列清理
python task1_sequence_clean.py

# 執行學生排名
python task2_student_ranking.py

# 執行日誌摘要
python task3_log_summary.py
```

### 第 3 步：執行測試

```bash
# 執行主程式測試 (41 tests)
python -m unittest discover -s tests -p 'test_task*.py' -v

# 執行 Bloom 測試 (180 tests)
cd bloom-examples
python -m unittest discover -s tests -p 'test_R*.py' -v
```

---

## 📝 詳細執行指南

### 主程式執行

#### Task 1: 序列清理

```bash
python task1_sequence_clean.py
```

**預期輸出:**
```
Original: [1, 2, 2, 3, 1, 4, 2]
Deduplicated (ordered): [1, 2, 3, 4]
Ascending: [1, 2, 3, 4]
Descending: [4, 3, 2, 1]
Even numbers: [2, 4]
```

**程式碼路徑:** [task1_sequence_clean.py](../task1_sequence_clean.py)

---

#### Task 2: 學生排名

```bash
python task2_student_ranking.py
```

**預期輸出:**
```
Students sorted by (score desc, age asc, name asc):
Student(score=98, age=18, name='Alice')
Student(score=95, age=19, name='Bob')
Student(score=95, age=19, name='Charlie')
...
```

**程式碼路徑:** [task2_student_ranking.py](../task2_student_ranking.py)

---

#### Task 3: 日誌摘要

```bash
python task3_log_summary.py
```

**預期輸出:**
```
User events count: {'user123': 5, 'user456': 3, ...}
Top 2 actions: [('login', 10), ('view', 8)]
```

**程式碼路徑:** [task3_log_summary.py](../task3_log_summary.py)

---

### 測試執行指南

#### 執行主程式的所有測試

```bash
# 詳細模式 (顯示所有測試名稱)
python -m unittest discover -s tests -p 'test_task*.py' -v

# 簡潔模式 (只顯示結果)
python -m unittest discover -s tests -p 'test_task*.py'
```

**測試分布:**
- `test_task1.py` - 12 個測試 (去重、排序、過濾)
- `test_task2.py` - 15 個測試 (排序、平手、邊界)
- `test_task3.py` - 14 個測試 (聚合、邊界)

#### 執行特定測試檔案

```bash
# 執行 Task 1 測試
python -m unittest tests.test_task1 -v

# 執行 Task 2 測試
python -m unittest tests.test_task2 -v

# 執行 Task 3 測試
python -m unittest tests.test_task3 -v
```

#### 執行特定測試類別或方法

```bash
# 執行特定類別
python -m unittest tests.test_task1.TestSequenceClean -v

# 執行特定方法
python -m unittest tests.test_task1.TestSequenceClean.test_deduplicate_basic -v
```

---

### Bloom Examples 測試執行

#### 執行所有 Bloom 測試 (180 tests)

```bash
cd bloom-examples
python -m unittest discover -s tests -p 'test_R*.py' -v
```

#### 按類別執行 Bloom 測試

```bash
# 基礎集合操作 (42 tests)
python -m unittest tests.test_R04_heapq tests.test_R05_priority_queue tests.test_R07_ordered_dict tests.test_R08_dict_minmax -v

# 進階操作 (138 tests)
python -m unittest tests.test_R09_dict_sets tests.test_R10_dedupe tests.test_R11_slice tests.test_R12_counter tests.test_R13_itemgetter tests.test_R14_attrgetter tests.test_R15_groupby tests.test_R16_filtering tests.test_R17_dict_subset tests.test_R18_namedtuple tests.test_R19_generator_aggregate tests.test_R20_chainmap -v
```

#### 執行特定 Bloom 測試

```bash
# Heapq 測試 (R04)
cd bloom-examples
python -m unittest tests.test_R04_heapq -v

# Priority Queue 測試 (R05)
python -m unittest tests.test_R05_priority_queue -v

# 去重測試 (R10)
python -m unittest tests.test_R10_dedupe -v

# ... 以此類推，其他 R11-R20
```

---

### 完整測試套件執行

#### 執行所有 221 個測試

**方案 1: 分步執行**
```bash
# 第 1 步：主程式測試
cd solutions/1114405036
python -m unittest discover -s tests -p 'test_task*.py'

# 第 2 步：Bloom 測試
cd bloom-examples
python -m unittest discover -s tests -p 'test_R*.py'
```

**方案 2: 建立執行指令碼**
```bash
# 建立 run_all_tests.py
cat > run_all_tests.py << 'EOF'
import subprocess
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("=" * 70)
print("執行所有 221 個測試")
print("=" * 70)

# 主程式測試
print("\n1. 執行主程式測試 (41 tests)")
print("-" * 70)
result1 = subprocess.run(
    ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_task*.py"],
    cwd="."
)

# Bloom 測試
print("\n2. 執行 Bloom Examples 測試 (180 tests)")
print("-" * 70)
result2 = subprocess.run(
    ["python", "-m", "unittest", "discover", "-s", "bloom-examples/tests", "-p", "test_R*.py"],
    cwd="."
)

print("\n" + "=" * 70)
print("完成")
print("=" * 70)
EOF

python run_all_tests.py
```

---

## 📚 文檔查閱

所有文檔位於 `docs/` 目錄：

```bash
cd solutions/1114405036/docs
```

### 推薦閱讀順序

1. **INDEX.md** - 開始：了解專案結構
2. **README.md** - 技術細節：設計決策和 TDD 過程
3. **TEST_CASES.md** - 測試設計：了解測試邏輯
4. **TEST_LOG.md** - 測試執行：查看測試過程
5. **AI_USAGE.md** - 開發過程：了解 AI 協作
6. **TEST_REPORT.md** - 簡報：快速 Bloom 概覽
7. **TEST_REPORT_EXTENDED.md** - 深度分析：技術細節

### 快速查找

```bash
# 查看目錄
ls -la docs/

# 查看檔案內容
cat docs/README.md          # TDD 過程
cat docs/TEST_LOG.md        # 測試紀錄
cat docs/AI_USAGE.md        # AI 協作
cat docs/TEST_CASES.md      # 測試設計
```

---

## 🔍 測試輸出解析

### 標準測試輸出

```
test_deduplicate_basic (test_task1.TestSequenceClean)
去重基本功能 ... ok
test_deduplicate_preserves_order (test_task1.TestSequenceClean)
去重保序 ... ok
test_ascending_sort (test_task1.TestSequenceClean)
遞增排序 ... ok
...
----------------------------------------------------------------------
Ran 41 tests in 0.001s

OK
```

### 詳細輸出模式

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

**輸出包括:**
- 類別名稱
- 測試方法名稱
- 測試文件 ... ok/FAIL
- 總測試數
- 執行時間
- 最終結果

---

## 🐛 故障排除

### 測試失敗

**問題:** `ImportError: No module named 'tests'`

**解決:**
```bash
# 確保在正確目錄
cd solutions/1114405036

# 檢查 tests 目錄是否存在
ls tests/

# 確保 tests/__init__.py 存在（如果需要）
touch tests/__init__.py
```

### Python 版本問題

**問題:** 語法錯誤或模組缺失

**檢查:**
```bash
python --version  # 應該是 3.6+

# 運行特定程式進行診斷
python -c "import collections; print('Collections OK')"
python -c "from itertools import groupby; print('Itertools OK')"
```

### 路徑問題

**問題:** `FileNotFoundError` 或相對路徑錯誤

**解決:**
```bash
# 確保在正確目錄運行
pwd  # 檢查當前目錄

# 從根目錄執行
python solutions/1114405036/task1_sequence_clean.py

# 或進入目錄再執行
cd solutions/1114405036
python task1_sequence_clean.py
```

---

## 📊 預期結果

### 所有測試通過

```
Main Project Tests:     41/41 PASS ✅
Bloom Examples Tests:  180/180 PASS ✅
────────────────────────────────
Total:                221/221 PASS ✅

Success Rate: 100%
Execution Time: ~0.065 seconds
```

### 檔案驗證

```bash
# 檢查所有程式檔案存在
ls -la task1_sequence_clean.py task2_student_ranking.py task3_log_summary.py

# 檢查所有測試檔案存在
ls -la tests/test_task*.py
ls -la bloom-examples/tests/test_R*.py

# 檢查所有文檔到位
ls -la docs/*.md
```

---

## 💾 備份和分享

### 備份專案

```bash
# 建立 zip 檔案
zip -r 1114405036_solution.zip solutions/1114405036/

# 建立 tar.gz 檔案
tar -czf 1114405036_solution.tar.gz solutions/1114405036/
```

### 驗證複製後的專案

```bash
# 進入專案目錄
cd solutions/1114405036

# 執行完整測試驗證
python -m unittest discover -s tests -p 'test_task*.py'
cd bloom-examples
python -m unittest discover -s tests -p 'test_R*.py'
```

---

## 📞 常見問題

**Q: 為什麼需要執行兩個測試命令？**
A: 主程式測試在 `tests/` 目錄，Bloom 測試在 `bloom-examples/tests/` 目錄。需要從各自目錄或明確指定路徑。

**Q: 可以一次執行全部 221 個測試嗎？**
A: 可以，使用上述「建立執行指令碼」方案，或分步執行兩個命令。

**Q: 如何修改並重新測試？**
A: 1. 編輯程式檔案
   2. 保存
   3. 重新執行 `python -m unittest discover ...`

**Q: 測試結果應該總是 OK 嗎？**
A: 是的。如果有失敗，表示程式邏輯有問題。檢查 `TEST_LOG.md` 查看預期行為。

---

**最後更新:** 2026-03-12  
**適用版本:** Python 3.6+  
**狀態:** 即時可用 ✅
