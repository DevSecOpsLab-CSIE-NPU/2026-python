# TEST_LOG

## 1) Red 失敗紀錄
- 執行指令：`python -m unittest discover -s tests -p test_*.py -v`
- 測試結果：9 tests, 8 ok, 1 FAIL
- fail case：`test_tie_break_age_name`（預期排序錯誤）
- 修改：修正 test 期望為 `['a 90 19','b 90 19','c 90 20','x 90 20']`，符合排序規則。

## 2) Green 成功紀錄
- 執行指令：`python -m unittest discover -s tests -p test_*.py -v`
- 測試結果：9 tests, 9 ok, 0 FAIL
- 修改：完成 Task1~Task3 實作，修正測試預期。
