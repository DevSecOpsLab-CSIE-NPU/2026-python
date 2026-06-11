# AI_LOG

## Prompt紀錄

- 你幫我把 Stage 1–5 的測試與實作整理到 `0611/` 根目錄，並補齊缺少的繳交檔案。
- 請幫我依 `0611-sort-lab.md` 的繳交清單檢查 `weeks/week-16/solutions/1114405028` 的內容是否符合。
- 請幫我新增 Stage 4 與 Stage 5 的紅燈 / 綠燈測試，並修補安全性問題。
- 請幫我完成 `README.md`、`AI_LOG.md`、`TEST_LOG.md`。
- 請幫我確認 `assets/benchmark.png` 已生成且目前提交目錄符合清單。
- 請幫我清理多餘的 `stageN` 子目錄和臨時檔案，保留平面 `0611/` 結構。
- 請幫我推送最終內容到 `feature/wk16-0611-1114405028`，並確保每個 stage 都有紅燈與綠燈測試。

## 我改了什麼

- 重構作業目錄，清除多餘 `stage1/`~`stage5/` 子目錄與臨時 notebook 文件。
- 寫好 `timing.py`、`sorts.py`、`benchmark.py`、`plot.py`、`test_security.py` 等核心檔案。
- 補齊 `README.md`、`TEST_LOG.md`，並更新 `TEST_LOG.md` 內容以註明每個 stage 的紅燈與綠燈循環。
- 生成並確認 `assets/benchmark.png` 與 `results.json`。
- 提交並推送最終分支 `feature/wk16-0611-1114405028`。

## 主要結果

- `0611` 根目錄現在只包含必要檔案。
- 所有階段都有對應的測試檔案：`test_timing.py`、`test_sorts.py`、`test_sorts_extra.py`、`test_benchmark.py`、`test_plot.py`、`test_security.py`。
- 成功推送到遠端分支，並保留提交歷史。
