# TEST_LOG

## Run 1 (Red)

- 執行指令:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 測試摘要:
  - 測試總數: 3
  - 通過數: 0
  - 失敗數: 3（ImportError）

- 失敗原因與修正（1~2 句）:
  - 三個測試檔都無法匯入 `task1_sequence_clean`、`task2_student_ranking`、`task3_log_summary`，因為先寫測試時實作檔尚未建立。
  - 補上三個 task 模組與必要函式後，重新執行測試。

## Run 2 (Green)

- 執行指令:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 測試摘要:
  - 測試總數: 10
  - 通過數: 10
  - 失敗數: 0

- 從失敗到通過的關鍵修改（1~2 句）:
  - 依照規格實作三題核心函式，並將 I/O 與邏輯分離，讓測試可直接驗證邏輯。
  - 補齊邊界處理（空輸入、同分排序、action 同次數 tie-break）後全部通過。
