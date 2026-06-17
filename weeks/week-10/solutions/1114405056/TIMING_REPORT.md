# TIMING_REPORT

## 執行結果

[timeit] read_csv 耗時 0.001489s  
[timeit] write_json 耗時 0.001527s  
[timeit] read_json 耗時 0.008018s  
[timeit] write_xml 耗時 0.001093s 

## 問題回答

1. 最耗時的是 `read_csv`。主因是 CSV 解析需要逐列讀取與欄位整理，I/O 和字串處理都比較多。
2. `read_csv` 比 `read_json` 慢，這和課堂 U01 的方向一致：結構化 JSON 在讀取時通常能更快被解析。
3. `write_xml` 比 `write_json` 慢。因為 XML 需要建立節點與屬性結構，再序列化成文字，步驟較多。
4. 若資料筆數從 100 增加到 10000，四個函式耗時都會上升，且大致接近線性成長，其中讀寫檔案與結構轉換較重的 `read_csv`、`write_xml` 增幅會更明顯。
