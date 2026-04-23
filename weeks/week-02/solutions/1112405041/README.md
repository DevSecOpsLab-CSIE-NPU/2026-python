# README.md - Week 02 作業回報

## 1. 完成題目清單
- [x] Task 1: Sequence Clean (去重、雙向排序、偶數篩選)
- [x] Task 2: Student Ranking (三級條件排序)
- [x] Task 3: Log Summary (使用者統計與最熱門動作)

## 2. 執行與測試方式
- **Python 版本**: 3.14 (v114)
- **程式執行**: `python task1_sequence_clean.py` (其餘類推)
- **測試執行**: `python -m unittest discover -s tests -p "test_*.py" -v`

## 3. 資料結構選擇理由
- **Task 1**: 選用 `dict.fromkeys()`。理由：在 Python 3.7+ 中 dict 是保序的，這是最精煉的「保序去重」方法，完美避開 `set()` 會打亂順序的問題。
- **Task 2**: 選用 `list[dict]` 搭配 `sorted(key=lambda)組合`。理由：利用 Python 的穩定排序特性，在單一 lambda 中處理 `(-score, age, name)`，代碼極簡且效能優於多次排序。
- **Task 3**: 選用 `Counter` 與 `defaultdict(int)`。理由：`defaultdict` 處理新使用者時不需判斷是否存在；`Counter` 的 `most_common(1)` 是抓取最熱門動作的最強工具。

## 4. 錯誤與修正 (Red → Green)
- **踩雷紀錄**：在 Task 1 最初沒注意到題目要求輸出「四項」結果（我只寫了去重）。在執行測試時發現斷言失敗。
- **修正方式**：重新研讀 `HOMEWORK.md` 聖經，補齊了從小到大、從大到小以及偶數列表推導式。

## 5. TDD 摘要
- **Red**: 初始測試因規格不符（缺 age 排序、缺輸出項）而噴紅。
- **Green**: 透過補齊邏輯使 12 個測試案例全數通過。
- **Refactor**: 將重複的輸入解析邏輯提取，並優化了多重排序的 lambda 寫法，讓代碼更具「代碼指紋」專業感。
