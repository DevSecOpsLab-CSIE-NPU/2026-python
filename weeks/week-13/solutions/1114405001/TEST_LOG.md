# TEST_LOG.md

## Red 階段（先寫測試）

執行指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

結果（摘要）：

- `ModuleNotFoundError: No module named 'task1_grouped_bar'`
- `ModuleNotFoundError: No module named 'task2_zipcode_heatmap'`
- 測試失敗（2 errors）

## Green 階段（完成實作後）

執行指令：

```bash
python task1_grouped_bar.py
python task2_zipcode_heatmap.py
python -m unittest discover -s tests -p "test_*.py" -v
```

結果（摘要）：

- 已成功產生 `output/task1.png`
- 已成功產生 `output/task2.png`
- 10 個測試全部通過（`OK`）
