# AI 使用說明

## 使用目的

本次 AI 主要協助以下工作：

1. 整理 `week-05/game_design` 六個階段的需求。
2. 協助規劃模組切分與測試範圍。
3. 依照 TDD 流程，先建立測試，再補對應實作。
4. 整理 README、測試案例說明與測試紀錄文件。

---

## 使用方式

本次互動過程中，AI 提供的協助包含：

1. 將 `p1~p6` 的需求整理為可實作的模組結構。
2. 先建立 `unittest` 測試案例，讓開發順序符合先測試後實作。
3. 實作遊戲核心邏輯與簡化 UI 結構。
4. 針對測試結果調整程式與測試細節。
5. 補齊作業說明文件。

---

## 人工確認內容

以下項目都有再人工確認：

1. 牌型規則是否與本次設計一致。
2. 首回合梅花 3 的限制是否有落實。
3. pass 三次後是否會重置牌桌。
4. AI 是否能在無互動輸入時完成整局遊戲。
5. README 與測試文件內容是否與實際程式一致。

---

## 驗證方式

實際驗證方式如下：

```powershell
cd weeks/week-05/solutions/1111405040/bigtwo
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe main.py
```

---

## 使用原則

1. AI 生成內容不直接當作最終答案，仍以實際測試結果為準。
2. 文件描述以實際實作與實際執行結果為準。
3. 若測試與假設不一致，優先修正錯誤假設，再重新驗證。
