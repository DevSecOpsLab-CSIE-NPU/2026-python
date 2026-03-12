# TEST_LOG

## Run 1 - Red

- 執行指令：`python3 -m unittest discover -s tests -p "test_*.py" -v`
- 測試總數：3
- 通過數：0
- 失敗數：3（3 個 import error）
- 摘要：

```text
test_task1 ... ERROR
test_task2 ... ERROR
test_task3 ... ERROR
Ran 3 tests
FAILED (errors=3)
```

- 從失敗到通過的修改（1~2 句）：
  當時僅有測試檔，尚未建立三個主程式模組，導致 `ModuleNotFoundError`。新增 `task1_sequence_clean.py`、`task2_student_ranking.py`、`task3_log_summary.py` 並補齊 `solve()` 與核心函式後進入下一次測試。

---

## Run 2 - Green

- 執行指令：`python3 -m unittest discover -s tests -p "test_*.py" -v`
- 測試總數：9
- 通過數：9
- 失敗數：0
- 摘要：

```text
Ran 9 tests
OK
```

- 從失敗到通過的修改（1~2 句）：
  依規格完成排序、去重、計數與邊界條件處理，並統一輸出格式。補齊後 9 個測試（正常、邊界、反例）全數通過。
