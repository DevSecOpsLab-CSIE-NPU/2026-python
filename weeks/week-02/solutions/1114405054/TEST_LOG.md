# TEST_LOG

## Run 1 - Red

- 指令:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 摘要:
  - 測試總數: 9
  - 通過數: 7
  - 失敗數: 2

- 失敗原因:
  - Task 2 的同分排序沒處理 age 與 name。
  - Task 3 的 `m=0` 沒有正確輸出 `top_action`。

- 修正說明:
  - Task 2 改為 `sorted(..., key=lambda s: (-s.score, s.age, s.name))`。
  - Task 3 補上空輸入預設輸出邏輯。

## Run 2 - Green

- 指令:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 摘要:
  - 測試總數: 9
  - 通過數: 9
  - 失敗數: 0

- 最終結果:
  - All tests passed.