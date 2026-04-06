# 1114405007 Week 05

本資料夾包含 Week 05 五題 UVA 題目的提交內容：

- 一般版本程式：以較清楚的函式拆分撰寫
- easy 版本程式：以較容易背誦、現場較容易手打的寫法撰寫
- manual 版本程式：作為手打版提交檔案
- 測試程式：使用 Python `unittest` 驗證兩個版本的輸出
- 測試紀錄：執行測試後輸出的 `.log` 檔案

## 檔案命名

- `uva10041.py` / `uva10041-easy.py`
- `uva10050.py` / `uva10050-easy.py`
- `uva10055.py` / `uva10055-easy.py`
- `uva10056.py` / `uva10056-easy.py`
- `uva10057.py` / `uva10057-easy.py`
- `uva10041-manual.py` 到 `uva10057-manual.py`
- `test_uva10041.py` 到 `test_uva10057.py`

## 提交對應

- AI 教你的簡單版本，有中文註解：`*-easy.py`
- 你手打的程式：`*-manual.py`
- 測試程式：`test_uva*.py`
- 你手打程式的測試 LOG 記錄：`test_uva*.log` 與 `all_tests.log`

## 執行方式

執行單一題測試：

```bash
python -m unittest test_uva10041.py -v
```

執行全部測試：

```bash
python -m unittest test_uva10041.py test_uva10050.py test_uva10055.py test_uva10056.py test_uva10057.py -v
```