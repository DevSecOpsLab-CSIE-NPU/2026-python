# AI_USAGE

本週作業使用 AI 輔助流程：

1. 先閱讀題目檔（QUESTION-11349, 11417, 11461, 12019）。
2. 先產生一般版 `question_xxxxx.py`（繁中註解）。
3. 再產生簡單版 `question_xxxxx-easy.py`（更容易記憶，繁中詳細註解）。
4. 依簡單版手動打出 `qxxxxx-Hand-typed.py`（無註解）。
5. 撰寫 `test_question_xxxxx.py` 與 `test_qxxxxx_hand_typed.py`。
6. 在本機 `.venv` 執行所有測試，並保存測試紀錄。

## 注意事項

- 程式皆可由 stdin 讀入、stdout 輸出。
- 測試以 `unittest` 執行。
- 手打版測試紀錄已集中在根目錄 `TEST_LOG.md`。
