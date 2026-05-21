# AI_USAGE.md

## 使用工具

- **Claude Code (claude-sonnet-4-6)**：本作業全程由 AI 輔助完成。

## 使用方式說明

1. **需求理解與規劃**：提供 HOMEWORK.md、CSV 檔案結構與參考圖片（V01/V02/V03），請 AI 規劃 TDD 流程與檔案架構。
2. **測試撰寫（Red Phase）**：AI 根據作業規格自動產生 `test_task1.py` 與 `test_task2.py` 共 10 個測試函式，確認測試在無實作時全部失敗（10 errors）。
3. **實作撰寫（Green Phase）**：AI 實作 `task1_grouped_bar.py` 與 `task2_zipcode_heatmap.py`，過程中修正路徑層數（4層→5層）與 `get_top_depts` 截斷邏輯，最終 10 個測試全部通過。
4. **Task 3 儀表板**：AI 閱讀 V03 參考圖佈局，使用 `plt.subplots(2,2)` 實作四象限綜合看板，包含趨勢折線、入學方式圓餅、各系長條、多線歷年趨勢，風格對齊參考圖配色（紅系折線、Steel Blue 長條、YlOrRd 熱力圖）。
5. **視覺調整**：AI 參考 V01、V02、V03 的配色、網格線、標題格式進行圖表美化；中文字型自動偵測 Microsoft JhengHei / Arial Unicode MS。
6. **報告撰寫**：AI 根據實際計算結果（食品科學系 28 人跨幅、澎湖縣 6.6%、台中市 15.6%、六年降幅 40%）撰寫 `REPORT.md` 並提出數據推論。

## 反思

AI 在結構化任務（測試→實作→圖表→文件）的效率極高，但路徑計算錯誤等細節仍需驗證。  
資料分析詮釋部分由 AI 提供初稿，建議學習者核對數字並加入自己的觀察視角。
