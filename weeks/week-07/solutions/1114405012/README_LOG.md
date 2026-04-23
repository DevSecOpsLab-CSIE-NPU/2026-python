# Week 07 測試紀錄（可繳交版）

此資料夾包含五題的測試紀錄，每題一份合併檔：
- `test_<題號>.txt`

每份檔案內已依序整理三個區塊：
- 一般版測試結果
- easy 版測試結果
- hand 版測試結果

題號清單：
- 10062
- 10071
- 10093
- 10101
- 10170

## 測試方式

以各題目資料夾內的 `test_<題號>.py` 執行 `unittest -v`：
- 一般版：`python3 -m unittest test_<題號>.py -v`
- easy 版：`SOLUTION_FILE=<題號>-easy.py python3 -m unittest test_<題號>.py -v`
- hand 版：`SOLUTION_FILE=<題號>-hand.py python3 -m unittest test_<題號>.py -v`

## 結果

本次整理後，`log/` 內共 5 份合併紀錄，內容皆為 `OK`（全部通過）。

