# AI_LOG

## 我改了什麼

- 完成 `timeit` 裝飾器與測試（包含 `repeat < 1` 要 `raise ValueError`）
- 新增 `linear_search`、`binary_search` 以及基本測試
- 新增 `benchmark_search.py` 做效能量測，並把評估寫到 `README.md`

## AI 反問我什麼 / 我怎麼回答

- 問：`binary_search` 遇到未排序資料要怎麼處理？
- 答：在 docstring 註明前提為已排序，未排序資料結果不保證正確。

- 問：`repeat` 要如何呈現結果？
- 答：每次耗時放進 `records`，本次平均放進 `last_elapsed`。

## 驗收標準

- `python -m unittest -v` 全綠
- `benchmark_search.py` 能輸出 linear 與 binary 的 records 與平均值
