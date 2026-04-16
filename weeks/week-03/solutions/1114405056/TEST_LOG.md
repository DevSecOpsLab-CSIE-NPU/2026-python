# TEST_LOG

日期：2026-04-16

## Run 1（Red）

- 指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 結果摘要：
  - 總數：0
  - 通過：0
  - 失敗：1（測試啟動失敗）
  - 主要錯誤：`ImportError: Start directory is not importable: 'tests'`

- 從失敗到通過的修改：
  - 建立 `tests/` 目錄與 `tests/__init__.py`。
  - 補上 `robot_core.py`、`tests/test_robot_core.py`、`tests/test_robot_scent.py`。

## Run 2（Red - 邏輯修正）

- 指令同上
- 結果摘要：
  - 總數：17
  - 通過：16
  - 失敗：1（`test_sample_case_robot3`）
  - 主要錯誤：`AssertionError: True is not false`（robot3 誤觸 robot2 的 scent）

- 從失敗到通過的修改：
  - 測試中補上 robot2 的執行步驟，讓 scent 狀態符合題目原意。

## Run 3（Green）

- 指令同上
- 結果摘要：
  - 總數：17
  - 通過：17
  - 失敗：0
  - 結論：`OK`

- 這次通過前的關鍵修正：
  - 完成 `LOST + scent` 邏輯與方向判斷。
  - 補齊「LOST 後停止執行」與「同格不同方向」測試案例。
