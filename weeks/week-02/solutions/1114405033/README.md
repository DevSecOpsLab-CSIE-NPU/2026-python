
## 1. 完成題目清單 (Task 1/2/3)
本週所有作業目標已全數達成，並通過所有單元測試：
-  **Task 1: Sequence Clean**
    - 成功實作輸入字串解析、數值去重
    - 達成降序排序與偶數篩選邏輯。
-  **Task 2: Student Ranking**
    - 成功實作複雜的多重條件排序機制
    - 確保分數、年齡與名字字母序的權重正確。
-  **Task 3: Log Summary**
    - 成功解析日誌格式並進行頻率統計
    - 達成 Top-N 使用者與最頻繁行為的提取邏輯

---

## 2. 執行方式 
     Windows 11 環境下完成

- **Python 版本**: 3.14
- **專案結構說明**: 
  程式位於 weeks/week-02/solutions/1114405033/ 目錄
- **程式執行指令**:
  ```powershell
  # 執行 Task 1
  python task1_sequence_clean.py
  # 執行 Task 2
  python task2_student_ranking.py
  # 執行 Task 3
  python task3_log_summary.py
  3. 資料結構選擇理由在開發過程中，針對不同情境選擇了最合適的資料結構以優化效能：
  #Task 1 - 
  使用 set 與 list 組合:由於題目要求去重（Deduplicate），使用 set (集合) 可以在 $O(n)$ 時間內完成唯一值篩選，其內部的 Hash Map 機制避免了在 list 中反覆查詢導致的 $O(n^2)$ 效能問題。最後轉換回 list 進行排序以符合輸出格式。
  #Task 2 - 
  使用 list 存放 tuple:學生的資料（姓名、分數、年齡）具有強關聯性，將其封裝為一個 tuple 並存入 list 中。tuple 的不可變性（Immutable）確保了在排序演算法執行期間，原始資料不會被意外篡改。
  #Task 3 - 
  使用 dict Hash Table:日誌統計涉及大量的「鍵-值」對應。使用字典（Dictionary）能快速記錄每個使用者或行為出現的次數。在最後尋找最常出現行為時，透過 dict.items() 轉換為列表排序，能在平衡空間與時間複雜度的前提下取得結果。
  #錯誤描述:
    在執行 git commit 指令時，終端機報錯 Author identity unknown，並顯示 fatal: unable to auto-detect email address。這導致本地端的所有修改無法被打包記錄，隨後的 git push 也因此無效。

    #原因分析:
    Git 在首次安裝或在新環境操作時，需要配置全域的使用者資訊（user.email 與 user.name），以便在版本紀錄（Commit Log）中標註作者身份。

    #修正步驟:

    開啟終端機執行：git config --global user.email "你的信箱@example.com"

    執行：git config --global user.name "YourName"

    設定完成後重新執行 git add 與 git commit，問題順利解決
    各題 Red → Green → Refactor 摘要
    #Task 1: 數列清理
    Red (失敗): 初始代碼未考慮輸入字串前後包含多餘空格或只有空格的情況 導致 int() 轉換噴出 ValueError

    Green (通過): 引入 input_str.strip() 預處理 並增加 if not parts: return [] 守護句（Guard Clause）確保邊界條件下的程式穩定性。

    Refactor (重構): 簡化邏輯 將去重 排序與轉型整合為一行清單推導式 提高代碼精簡度

    #Task 2: 學生排名
    Red : 測試案例中 兩名分數相同但年齡不同的學生，排序結果與題目要求的「年齡越小越前面」相反

    Green : 利用 Python sorted() 函數的 key 參數，設計 lambda x: (-x[1], x[2], x[0])。其中分數加負號達成降序，年齡與名字維持正值達成升序

    Refactor : 將輸入邏輯封裝 並處理可能發生的 EOFError 使程式在自動化批改系統中更健壯

    #Task 3: 日誌統計
    Red : 當日誌中存在兩個行為login 與 logou 出現次數完全相同時 程式回傳的結果不具備確定性 未遵循字母序

    Green 通過: 調整排序策略，在比較次數 的同時，將名稱納入排序權重 確保在次數相同時，字母序較前者優先輸出

    Refactor : 改用 collections.Counter 類別處理統計 減少手動維護字典計數的複雜度