# Week 12 測試紀錄

## 開發流程
1. 先依題意整理每題需要的核心函式。
2. 先為每題建立 `unittest` 測試。
3. 補上 `solve()` 與輸入輸出格式處理。
4. 執行整體測試並修正格式細節。

## 測試重點
- `10812`：檢查無解條件與正常回推
- `10908`：檢查中心擴張與邊界停止條件
- `10922`：檢查 9-degree 計算與輸出句型
- `10929`：檢查大數字字串的 11 倍數判斷
- `10931`：檢查二進位轉換與 parity 計算

## 執行指令
```powershell
cd weeks/week-12/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

## 結果
- 5 份測試檔
- 20 個測試函式
- 預期全部通過
