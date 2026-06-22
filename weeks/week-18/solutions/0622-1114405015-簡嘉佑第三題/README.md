# 第三題：任意進位的數字根

## 題意整理
- 讀入多筆十進位整數 x（每行一筆），直到 EOF。
- 先把 x 視為某個 base 的數字，做「各位數字相加」。
- 若結果仍不是一位數（在該 base 下），就重複上述步驟。
- 最後輸出該數字根（以十進位整數輸出）。

## 本題使用的 base
- 學號：1114405015
- 本份解答採用 base = 7

## 範例（用本題 base=7）
輸入：
- 0
- 8
- 63

輸出：
- 0
- 2
- 3

說明：
- 8(10) = 11(7)，1+1=2
- 63(10) = 120(7)，1+2+0=3

## 檔案說明
- question_3_solution.py：主解答（含 solve/main）
- question_3_solution-easy.py：易記版（手打友善）
- test_question_3.py：unittest 測試
- test_input.txt：測試輸入
- test_output.txt：預期輸出
- AI_LOG.md：AI 使用紀錄

## 執行方式

主程式：
python question_3_solution.py < test_input.txt

簡化版：
python question_3_solution-easy.py < test_input.txt

測試：
python -m unittest test_question_3.py -v

## 複雜度
- 單筆資料：O(k * d)
  - d：該次拆位數量
  - k：重複相加輪數（通常很小）
- 額外空間：O(1)
