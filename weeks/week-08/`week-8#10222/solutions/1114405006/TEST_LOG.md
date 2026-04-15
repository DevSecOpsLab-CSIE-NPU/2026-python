# 手寫程式測試日誌（QUESTION-10222）

日期：2026-04-15
程式：solution_10222_simple.py

## 測試環境
- OS: Windows
- Python 啟動方式：py -3（若無則可用 python）

## 測試命令
```powershell
Get-Content input_sample.txt | py -3 .\solution_10222_simple.py
```

## 測試輸入
```text
r
O S, GOMR YPFSU/
R;/
```

## 預期輸出
```text
e
I AM FINE TODAY.
EL.
```

## 程式實際輸出
```text
e
I AM FINE TODAY.
EL.
```

## 結果
- 全部輸出與預期一致（Pass）
- 測試通過：1 / 1
- 已驗證大小寫、空白與符號解碼。
