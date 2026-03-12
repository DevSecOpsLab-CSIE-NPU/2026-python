# TEST_LOG

## Run 1 - Red（失敗）

- 執行指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 測試總數：13
- 通過數：12
- 失敗數：1
- 失敗到通過修改：
  - 初版把 `scent` 寫成 `(x, y)`，導致同格不同方向也被阻擋。
  - 修正為 `(x, y, dir)` 後，方向差異測試轉綠。

## Run 2 - Green（全通過）

- 執行指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 測試總數：13
- 通過數：13
- 失敗數：0
- 從失敗到通過修改：
  - 更新 scent 判斷邏輯後，重跑測試全數通過。
