# TIMING_REPORT

## 執行結果

```text
[timeit] read_csv 耗時 0.058529s
[timeit] write_json 耗時 0.002363s
[timeit] read_json 耗時 0.014762s
[timeit] write_xml 耗時 0.001898s
```

## 問題回答

1. 最耗時的是 `read_csv()`，因為它要逐列解析整份 CSV，而且還要把每一列轉成字典。
2. `read_csv()` 比 `read_json()` 慢，這和一般情況一致，因為 JSON 解析通常比逐列 CSV 讀取更直接。
3. `write_xml()` 在這次資料量下比 `write_json()` 快，因為輸出的 XML 結構很小，而且這裡的 JSON 寫出還要做格式化縮排。
4. 如果資料筆數從 100 增加到 10000，四個函式的耗時都會上升；其中 `read_csv()` 和 `write_xml()` 會比較明顯，因為它們都需要處理每一列資料。