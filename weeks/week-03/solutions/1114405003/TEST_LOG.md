# TEST_LOG

## 1) Red phase（失敗）
- 執行: `python -m unittest discover -s tests -p "test_*.py" -v`
- 結果: 10 tests, 9 passed, 1 failed
- 失敗測試: `test_invalid_command_raises`
- 修正: `Robot.execute` 增加非法命令檢查並拋 `ValueError`。

## 2) Green phase（全部通過）
- 執行: `python -m unittest discover -s tests -p "test_*.py" -v`
- 結果: 10 tests, 10 passed, 0 failed
- 變更: `Robot.execute` 非 `L/R/F` 拋錯，`move_forward` scent 行為通過測試。
