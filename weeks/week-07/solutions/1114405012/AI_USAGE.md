# AI 使用說明

以下是建議給 AI 的工作流程（可直接貼到對話中）：

1. 先讀題目檔（`QUESTION-xxxx.md`），產生三個版本：
   - 一般版（`xxxx.py`）
   - easy 版（`xxxx-easy.py`）
   - 手打版（`xxxx-hand.py`）
2. 為該題建立單元測試（`test_xxxx.py`）。
3. 依序跑三次測試並把輸出存成文字檔：
   - `python3 -m unittest test_xxxx.py -v > ../log/test_xxxx_base.txt 2>&1`
   - `SOLUTION_FILE=xxxx-easy.py python3 -m unittest test_xxxx.py -v > ../log/test_xxxx_easy.txt 2>&1`
   - `SOLUTION_FILE=xxxx-hand.py python3 -m unittest test_xxxx.py -v > ../log/test_xxxx_hand.txt 2>&1`
4. 把三份測試結果合併為一份可繳交檔案：
   - `../log/test_xxxx.txt`
5. 檢查合併後檔案需包含三段標題：
   - 一般版
   - easy 版
   - hand 版

## 範例提示詞

「讀 `weeks/week-07/QUESTION-10062.md`，幫我產生 `10062.py`、`10062-easy.py`、`10062-hand.py`、`test_10062.py`，跑完三版測試，並把結果整理到 `log/test_10062.txt`。」
