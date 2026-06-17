# AI 開發日誌 (AI_LOG.md)
日期：2026-06-17

## 任務摘要
- 任務一：timeit 裝飾器（走完整 TDD：先放 test_timing.py 紅燈，再實作 timing.py 綠燈）
- 任務二：搜尋效能輕量評估（撰寫 search.py 與 eval_search.py，使用自製 timeit 測時）

## 我改了什麼
- 新增：test_timing.py（紅燈，≥3 個 test case，含 edge case）
- 新增：timing.py（綠燈實作）
- 新增：search.py（linear_search / binary_search）
- 新增：eval_search.py（測時與簡易輸出）
- 新增：README.md（評估結論與執行說明）
- 新增：本檔 AI_LOG.md（紀錄 AI 與決策）

## AI 反問我什麼 / 我怎麼回答
- AI: repeat 是要取每次執行的平均、最小還是中位數？  
  我答: 取平均（average），因為要反映一般耗時情況。
- AI: repeat 小於 1 的行為是 raise 還是 assert？  
  我答: 使用 raise ValueError（題目要求不可用 assert）。
- AI: records 應該每次呼叫重新建立還是累積？  
  我答: 累積（append 本次 repeat 的各次耗時到 wrapper.records）。
- AI: 裝飾器是否要支援不帶括號的用法 `@timeit`？  
  我答: 支援（同時支援 @timeit、@timeit() 與 @timeit(repeat=...)）。
- AI: 裝飾器在呼叫時是否可以 print？  
  我答: 不可 print（規格說明）。
- AI: binary_search 收到未排序資料時要怎麼處理？  
  我答: 直接 raise ValueError（避免修改傳入資料或回傳錯誤索引）。
- AI: binary_search 可否修改傳入 data？  
  我答: 不可修改傳入的 data（規格要求）。
- AI: 評估時是否把排序成本計入？  
  我答: 要把排序成本單獨測量，並列出 sort + binary 的合計以便比較。

## 測試 / 驗證流程
- 1) 放入 test_timing.py → pytest（應紅燈，因為尚無 timing.py）→ commit "test:"  
- 2) 實作 timing.py → pytest（綠燈）→ commit "feat:"  
- 3) 跑 eval_search.py 檢查搜尋時間序列與排序成本，並記錄 README 結論

## 備註
- 若要重現測試或評估：在 VS Code 終端機執行  
  cd d:\2026-python\weeks\week-17\solutions\1114405028  
  pytest -q （測試）  
  python eval_search.py（