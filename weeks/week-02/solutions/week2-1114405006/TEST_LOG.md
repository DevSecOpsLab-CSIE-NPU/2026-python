# Test Log

## Red

- 執行指令：`python -m unittest discover -s tests -p "test_*.py" -v`
- 測試總數：15
- 通過數：0
- 失敗數：15
- 修改摘要：先以 `NotImplementedError` 建立最小骨架，確認三題的測試都會失敗，作為 Red 階段的證據。

## Green

- 執行指令：`python -m unittest discover -s tests -p "test_*.py" -v`
- 測試總數：15
- 通過數：15
- 失敗數：0
- 修改摘要：補上三題的解析、排序、統計與格式化邏輯，並處理空輸入與 top-k 輸出格式。
