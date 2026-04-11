# AI_USAGE.md

本文件記錄了本次作業中與 AI (Gemini) 協作的過程、採納的建議以及針對錯誤引導的修正紀錄。

## AI 互動紀錄
1. **問題**: 如何在不使用 `set()` 的情況下對列表去重並保留原始順序？
2. **問題**: Python `sorted()` 函數的 `key` 參數如何處理多個欄位排序？尤其是其中一個欄位需要降序（Desc）時。
3. **問題**: 如何撰寫 `unittest` 案例來測試 `sys.stdin` 的輸入結果與 `sys.stdout` 的輸出？
4. **問題**: 遇到 `IndexError: tuple index out of range` 時，如何根據追蹤碼 (Traceback) 定位錯誤？

## 採納的 AI 建議
* **混合排序技巧**: 採用了在 `key=lambda` 中對數值欄位使用負號（`-x[1]`）來達成降序效果的建議，這讓程式碼非常精簡。
* **強健輸入處理**: 採用了使用 `sys.stdin.read().split()` 來替代 `input()` 的建議，確保處理多筆資料或不規則空白時更穩定。
* **資料結構選用**: 在 Task 3 採用了 `defaultdict(int)` 與 `Counter` 組合，大幅簡化了計數與尋找最多次數動作的邏輯。

## 拒絕的 AI 建議
* **輸入方式**: AI 最初建議使用 `input()` 逐行讀取，但考量到作業可能包含多行或不規則空白，我決定改用 `split()` 解析。
* **測試框架**: AI 建議使用外部套件 `pytest`，但我決定維持使用 Python 內建的 `unittest` 以符合課程要求，避免增加額外環境依賴。

## AI 誤導與修正案例
* **案例描述**: 在實作 Task 2 的排序規則時，AI 提供的 Lambda 範例中索引值超出了 tuple 的範圍（誤寫為 `x[3]`）。
* **問題點**: 執行測試時噴出 `IndexError: tuple index out of range`。這是因為學生資料 tuple 結構為 `(name, score, age)`，索引僅有 0, 1, 2。
* **修正方式**: 我自行追蹤了 `students.append((name, score, age))` 的結構，確認姓名位於索引 `0`，並將排序邏輯修正為 `key=lambda x: (-x[1], x[2], x[0])`，隨後測試順利通過。