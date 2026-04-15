# 手寫程式測試日誌（QUESTION-10190）

日期：2026-04-15
程式：`solution_10190_simple.py`

## 測試環境
- OS: Windows
- Python 啟動方式：`py -3`（若無則可用 `python`）

## 測試命令
```powershell
Get-Content input_sample.txt | py -3 .\solution_10190_simple.py
```

## 測試輸入
```text
81 3
100 10
22 2
10 1
1 5
```

## 預期輸出
```text
81 27 9 3 1
100 10 1
Boring!
Boring!
Boring!
```

## 程式實際輸出
```text
81 27 9 3 1
100 10 1
Boring!
Boring!
Boring!
```

## 結果
- 全部輸出與預期一致（Pass）
- 測試通過：1 / 1
