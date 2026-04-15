# 手寫程式測試日誌（QUESTION-10189）

日期：2026-04-15
程式：`solution_10189_simple.py`

## 測試環境
- OS: Windows
- Python 啟動方式：`py -3`（若無則可改 `python`）

## 測試命令
```powershell
Get-Content .\input_sample.txt | py -3 .\solution_10189_simple.py
Get-Content .\input_1x1_empty.txt | py -3 .\solution_10189_simple.py
Get-Content .\input_1x1_mine.txt | py -3 .\solution_10189_simple.py
```

## Case 1：題目範例（多組）
### 輸入
```text
4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
```

### 程式輸出
```text
Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100
```

### 結果
- 與題目預期一致（Pass）

## Case 2：最小無雷案例
### 輸入
```text
1 1
.
0 0
```

### 程式輸出
```text
Field #1:
0
```

### 結果
- 輸出正確（Pass）

## Case 3：最小有雷案例
### 輸入
```text
1 1
*
0 0
```

### 程式輸出
```text
Field #1:
*
```

### 結果
- 輸出正確（Pass）

## 總結
- 3 / 3 測試通過。
- 多組輸出格式與空行規則正確。
