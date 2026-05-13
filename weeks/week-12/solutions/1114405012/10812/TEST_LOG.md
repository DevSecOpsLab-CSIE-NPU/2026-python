# 10812 測試紀錄

## 2026-05-13

### 第一次執行

指令：

```bash
/Library/Developer/CommandLineTools/usr/bin/python3 -m unittest test_question_10812.py -v
```

結果摘要：

```text
Ran 6 tests in 0.105s

FAILED (failures=2)
```

說明：

- `test_impossible_due_to_odd_sum` 的測資選錯，`20 10` 其實是合法解。
- `test_multiple_cases_in_one_input` 也因此混入了錯誤反例。

### 第二次執行

指令：

```bash
/Library/Developer/CommandLineTools/usr/bin/python3 -m unittest test_question_10812.py -v
```

結果摘要：

```text
Ran 6 tests in 0.103s

OK
```

說明：

- 已改用真正的奇數和案例 `21 10`。
- 所有測試案例皆通過。