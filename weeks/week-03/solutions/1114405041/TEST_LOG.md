# TEST_LOG

## Run 1 (Red)
- 日期：2026-03-24
- 指令：`python uva118.py < sample_118.txt`
- 結果：1 個案例輸出與預期不符（scent 分支未正確略過危險 F）
- 狀態：FAIL
- 修正：調整 `uva118.py` 的越界流程，先判斷 `(x, y, dir)` 是否在 scent；若存在則忽略該步，否則標記 LOST。

## Run 2 (Green)
- 日期：2026-03-24
- 指令：
  - `python uva100.py < sample_100.txt`
  - `python uva118.py < sample_118.txt`
  - `python uva272.py < sample_272.txt`
  - `python uva299.py < sample_299.txt`
  - `python uva490.py < sample_490.txt`
- 結果：5 題輸出皆符合預期案例
- 狀態：PASS
- 說明：完成 Week 03 指定 5 題程式與文件補齊。
