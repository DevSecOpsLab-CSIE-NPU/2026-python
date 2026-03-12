# TEST_LOG

日期：2026-03-12

## Run 1（Red）

- 指令：

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

- 結果摘要：
  - 總數：0
  - 通過：0
  - 失敗：1（測試啟動失敗）
  - 主要錯誤：`ImportError: Start directory is not importable: 'tests'`

- 從失敗到通過的修改：
  - 建立 `tests/` 目錄與 `tests/__init__.py`。
  - 補上 `robot_core.py`、`test_robot_core.py`、`test_robot_scent.py`。

## Run 2（Green）

- 指令：

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

- 結果摘要：
  - 總數：12
  - 通過：12
  - 失敗：0
  - 結論：`OK`

- 這次通過前的關鍵修正：
  - 完成 `LOST + scent` 邏輯與方向判斷。
  - 補齊「LOST 後停止執行」與「同格不同方向」測試案例。
