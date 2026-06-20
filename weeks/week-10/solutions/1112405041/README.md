# Week 10 作業 — 資料格式轉換

## 完成項目
- [x] Task 1：CSV → JSON 轉換
- [x] Task 2：JSON → XML 轉換
- [x] Task 3：視覺化比較

## 執行方式
```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## @timeit 裝飾器說明
@timeit 是一個自製的計時裝飾器，包在原函式外層自動記錄執行時間。實作上我用 functools.wraps 保留原函式中繼資料，並在執行前後用 time.perf_counter 計算秒數，最後將結果 print 出來。這樣不用在每個函式裡面手動寫計時邏輯，直接加一行 @timeit 就好。

## 遇到的 bug 與修正
最讓我卡住的是 task2 的 build_xml_tree 需要從巢狀 dict 建出 XML 結構。我一開始直接對 data["students"] 做迴圈，但忘記 data 本身就是 list（read_json 回傳的就是 list，沒有 "students" 鍵），結果 AttributeError 才知道結構不對，改成直接 iter 傳入的 list 就解決了。
