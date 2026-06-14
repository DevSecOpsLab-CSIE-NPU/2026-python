# Week 13 作業說明（1114405001）

本資料夾完成 Week 13 視覺化作業兩個任務：

- Task 1：112/113/114 三年各系招生人數並排長條圖
- Task 2：109-114 來源縣市熱力圖（以郵遞區號前三碼映射）

## 檔案結構

- `task1_grouped_bar.py`：Task 1 主程式與函式
- `task2_zipcode_heatmap.py`：Task 2 主程式與函式
- `tests/test_task1.py`：Task 1 單元測試
- `tests/test_task2.py`：Task 2 單元測試
- `output/task1.png`：Task 1 圖檔
- `output/task2.png`：Task 2 圖檔
- `TEST_LOG.md`：Red -> Green 測試紀錄
- `REPORT.md`：圖表分析心得
- `AI_USAGE.md`：AI 協作紀錄

## 執行方式

在本資料夾執行：

```bash
python task1_grouped_bar.py
python task2_zipcode_heatmap.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## 函式介面

- `load_year(year: int, data_dir: Path) -> dict[str, int]`
- `get_top_depts(year_data: dict[int, dict[str, int]], top_n: int = 8) -> list[str]`
- `load_county_counts(year: int, data_dir: Path) -> dict[str, int]`
- `get_top_counties(all_years: dict[int, dict[str, int]], top_n: int = 10) -> list[str]`
- `zip_to_county(zipcode: str) -> str`
