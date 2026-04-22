# Week 10 solutions for 1114405012

這個資料夾整理 week-10 的 5 題練習成果，包含正式版、`-easy` 版、單元測試與測試紀錄。

## 檔案清單

- [10226.py](10226.py) / [10226-easy.py](10226-easy.py) / [10226-hand.py](10226-hand.py) / [test_10226.py](test_10226.py) / [test_record_10226.txt](test_record_10226.txt)
- [10235.py](10235.py) / [10235-easy.py](10235-easy.py) / [10235-hand.py](10235-hand.py) / [test_10235.py](test_10235.py) / [test_record_10235.txt](test_record_10235.txt)
- [10242.py](10242.py) / [10242-easy.py](10242-easy.py) / [10242-hand.py](10242-hand.py) / [test_10242.py](test_10242.py) / [test_record_10242.txt](test_record_10242.txt)
- [10252.py](10252.py) / [10252-easy.py](10252-easy.py) / [10252-hand.py](10252-hand.py) / [test_10252.py](test_10252.py) / [test_record_10252.txt](test_record_10252.txt)
- [10268.py](10268.py) / [10268-easy.py](10268-easy.py) / [10268-hand.py](10268-hand.py) / [test_10268.py](test_10268.py) / [test_record_10268.txt](test_record_10268.txt)

## 方向摘要

- 10226：DFS 產生合法排列，並輸出和前一個排列不同的部分。
- 10235：用 profile DP 計算格子上的封閉蛇環數量。
- 10242：SCC 壓縮後在 DAG 上做最大值 DP。
- 10252：曼哈頓距離分別對 x / y 取中位數區間。
- 10268：反向 DP 計算最多可覆蓋樓層數，超過 63 次則輸出指定訊息。