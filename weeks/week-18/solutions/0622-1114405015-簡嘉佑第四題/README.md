# 第四題：二分搜尋效能

## 1. 題目重點
本題要比較線性搜尋與二分搜尋在同一組資料上的表現，並回報：
1. 二分搜尋是否找到 K，與比較次數 cmp。
2. timeit 的線性搜尋與二分搜尋耗時。
3. 誰比較快。
4. 雷達圖 assets/radar.png 與多維度解讀。

本份作答使用：
- 學號末兩碼：15
- 搜尋目標：K = 100 + 15 = 115

## 2. 輸入方式
### 模式 A（依題目格式）
- 第 1 行：m
- 第 2 行起：m 個整數（若跨行也可）

程式會：
- 取前 m 個數字
- 若非升冪，會排序成升冪

### 模式 B（未提供有效輸入）
若沒有有效輸入，程式自動建立大型升冪陣列：
- arr = [0, 1, 2, ..., 199999]

這樣可確保 timeit 能看出效能差異。

## 3. 輸出格式
程式輸出文字格式如下：
- FOUND idx cmp=次數
  或
- NOT FOUND cmp=次數
- linear: t 秒
- binary: t 秒
- => xxx faster

其中 cmp 是演算法比較次數，不是時間。

## 4. 主要檔案
- question_4_solution.py：主程式（搜尋 + timeit + 產圖）
- plot_radar.py：雷達圖繪製
- test_question_4.py：單元測試

## 5. 執行方式
### 5.1 直接執行（自動建資料）
python question_4_solution.py

### 5.2 依題目格式輸入
python question_4_solution.py < test_input.txt

### 5.3 執行測試
python -m unittest test_question_4.py -v

## 6. 測試資料
test_input.txt 內容：
20
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 115 200 500 1000

預期重點：
- 會 FOUND（因為包含 115）
- binary 通常比 linear 快

## 7. 複雜度
- 線性搜尋：
  - 時間 O(n)
  - 空間 O(1)
- 二分搜尋：
  - 時間 O(log n)
  - 空間 O(1)

## 8. 雷達圖設計與正規化
檔案：assets/radar.png

維度（0..10，分數越高越好）：
1. speed：速度潛力
2. no_sort_required：不需先排序
3. implementation_simple：實作簡單
4. worst_case_cmp：最差比較次數表現
5. scalability：資料變大時的延展性

本作答給分：
- linear = [4, 10, 9, 2, 3]
- binary = [10, 3, 7, 10, 10]

解讀重點：
- linear 在「不需排序」與「實作直覺」有優勢。
- binary 在「速度」「最差比較次數」「可擴展性」明顯更好。
- 沒有絕對贏家：若資料未排序且只查少量次，linear 仍可能是實務好選擇。

## 9. Edge Cases
本份測試含以下 edge case：
1. 目標不存在（NOT FOUND）。
2. 空輸入時自動建陣列。
3. 輸入不是升冪時自動排序後搜尋。

## 10. 交付檔案清單
- question_4_solution.py
- plot_radar.py
- test_question_4.py
- test_input.txt
- test_output_example.txt
- AI_LOG.md
- README.md
- assets/radar.png（執行主程式後產生）
