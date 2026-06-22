# Question 1

- 學號末位 `u = 7`
- 依題目規則計算整除數 `D = u % 4 + 2 = 3`
- 輸入含多組資料，每組以 `n` 和 `n` 個整數表示，遇到 `n=0` 結束
- 依序去重，保留第一個出現的數值
- 只保留能被 `D` 整除的數字
- 最後由小到大排序，若無符合輸出 `NONE`

## 執行方式

```bash
python main.py < input.txt
```

## 測試

```bash
python test_main.py
```
