# AI 使用記錄

## 我問 AI 什麼
> 每則提示詞逐字記錄

1. 「幫我寫 Stage 1 data_loader.py 的測試，包含 load_year、zip_to_county、load_county_counts」
2. 「幫我寫 Stage 1 data_loader.py 的實作」
3. 「幫我寫 Stage 2 analysis.py 的測試和實作」
4. 「幫我寫 Stage 3 plot.py 畫圖」
5. ...

## AI 給了什麼
> AI 回應重點

（你填）

## 我改了什麼
> **重要：你自己判斷修改了什麼**

1. Stage 1 測試：把 DATA_DIR 從 4 層修正為 6 層 .parent，因為測試檔在 tests/ 子目錄
2. Stage 2 測試：把 test_get_top_depts_includes_popular 的系名從「應用外語系」改為「資訊工程系」
3. ...

## AI 反問我什麼 / 我怎麼回答
> 逐項記下 AI 問的規格問題與你的決定

- AI 問「load_year 例外行為要 raise 還是回傳空 dict？」→ 我答：raise ValueError
- AI 問「同名系所重複要合併還是報錯？」→ 我答：合併人數
- ...
