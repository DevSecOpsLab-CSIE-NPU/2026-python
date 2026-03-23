# TEST_CASES

## Case 1 - UVA 100 基本範例
- 檔案：`uva100.py`
- 輸入：
  - `1 10`
  - `100 200`
  - `201 210`
  - `900 1000`
- 預期結果：
  - `1 10 20`
  - `100 200 125`
  - `201 210 89`
  - `900 1000 174`
- 實際結果：符合預期
- PASS/FAIL：PASS

## Case 2 - UVA 100 反向區間
- 檔案：`uva100.py`
- 輸入：`10 1`
- 預期結果：`10 1 20`
- 實際結果：符合預期
- PASS/FAIL：PASS

## Case 3 - UVA 118 經典範例
- 檔案：`uva118.py`
- 輸入：
  - `5 3`
  - `1 1 E`
  - `RFRFRFRF`
  - `3 2 N`
  - `FRRFLLFFRRFLL`
  - `0 3 W`
  - `LLFFFLFLFL`
- 預期結果：
  - `1 1 E`
  - `3 3 N LOST`
  - `2 3 S`
- 實際結果：符合預期
- PASS/FAIL：PASS

## Case 4 - UVA 118 scent 方向差異
- 檔案：`uva118.py`
- 輸入：自製案例（同座標不同方向）
- 預期結果：不同方向不共享 scent，必要時仍可 LOST
- 實際結果：符合預期
- PASS/FAIL：PASS

## Case 5 - UVA 272 單行引號
- 檔案：`uva272.py`
- 輸入：`"To be or not to be,"`
- 預期結果：``To be or not to be,''
- 實際結果：符合預期
- PASS/FAIL：PASS

## Case 6 - UVA 272 多行混合內容
- 檔案：`uva272.py`
- 輸入：多行文字含偶數個 `"`
- 預期結果：引號交替替換，其餘字元不變
- 實際結果：符合預期
- PASS/FAIL：PASS

## Case 7 - UVA 299 交換次數
- 檔案：`uva299.py`
- 輸入：
  - `1`
  - `3`
  - `3 1 2`
- 預期結果：`Optimal train swapping takes 2 swaps.`
- 實際結果：符合預期
- PASS/FAIL：PASS

## Case 8 - UVA 490 旋轉句子
- 檔案：`uva490.py`
- 輸入：
  - `HELLO`
  - `WORLD`
- 預期結果：順時針旋轉 90 度後之矩陣輸出
- 實際結果：符合預期
- PASS/FAIL：PASS
