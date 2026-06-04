# test_log

## 題目
平方數計數（UVA 11461 簡化）

## 測試指令
python -m unittest test_square_counter.py -v

## 紅燈紀錄
階段：尚未建立 square_counter.py 時
結果：FAILED
關鍵錯誤：ModuleNotFoundError: No module named 'square_counter'
說明：先完成測試再實作，先紅燈符合 TDD。

## 綠燈紀錄
階段：建立 square_counter.py 並完成 count_squares 後
結果：OK
摘要：Ran 4 tests in 0.001s
通過測試：
- test_basic_range_1_to_10
- test_edge_single_point_square
- test_no_square_in_range
- test_invalid_input_raises

## 備註
例外案例已涵蓋 a > b 時應拋出 ValueError。
