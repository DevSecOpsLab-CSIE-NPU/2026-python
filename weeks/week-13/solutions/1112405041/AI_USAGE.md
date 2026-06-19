# AI 使用記錄

## 我問 AI 什麼
> 每則提示詞逐字記錄

1. look week 15 16 17 progress looking+style its? +Agent.md and 應用到 week 13  homework.md
2. 我觀察到的 weeks 15-17 風格關鍵點 (不可以是關鍵 是整串開發類似流程 套用在 week 13 HOMEWORK.MD STYLE ✅ TDD 紅燈→綠燈（test: → feat: commit）
✅ 5 階段結構（timeit → 功能實作 → benchmark → 畫圖 → 安全自掃）
✅ raise 不 assert、with 開檔、functools.wraps
✅ 型別註記、共用測試用 subTest
✅ 禁止 print 在工具函式內
✅ AI 協作協議（檢查表五項、先紅再綠、階段閘門、訪談摘要） (掃毒)( 或你再觀察 )
3.   然後我只要做  Week 13 回家作業：招生資料視覺化分析
4. 先把難度降到最簡單 反正老師 可以 讓你先教我 再開始做?(  他的 很限制 人性化 ( 還有請快速在你的免費額度內做完.....(這是第一要求() 他也要訪談模式 (就是這個 複雜疊加態)
5. year 只能是 109~114（CSV 檔名範圍） (可以0啊 程式跑得動就好 0跟負數都行語法正確都行) 但不符合老師要求 0分 (還有 可以問我有深度的 但是要講原理 這樣老師才知道我懂了
6.yt 過程link https://youtu.be/TtHutKgIgKM?si=yc6z4OkJ3gf9opn8
7.過程中我也學到很多概念 程式的引用 但是實戰可能還是要多查資料 
## AI 給了什麼
> 產出了 程式碼  我則是進行審查
協助我commit 確認 提示我該做甚麼

（你填）

## 我改了什麼
> 我針對AI 建議 修改了中文產圖細節


1. Stage 1 測試：把 DATA_DIR 從 4 層修正為 6 層 .parent，因為測試檔在 tests/ 子目錄
2. Stage 2 測試：把 test_get_top_depts_includes_popular 的系名從「應用外語系」改為「資訊工程系」


## AI 反問我什麼 / 我怎麼回答
> 逐項記下 AI 問的規格問題與你的決定

- AI 問「load_year 例外行為要 raise 還是回傳空 dict？」→ 我答：raise ValueError
- AI 問「同名系所重複要合併還是報錯？」→ 我答：合併人數
- AI 問了我很多問題 包括程式概念題 我答：因為我希望 先懂再做 造成 上下文視窗有點長 不好整理 


