# Question 2

- 學號末位 `u = 7`
- 依題目規則計算位移 `SHIFT = u % 25 + 1 = 8`
- 對每一行文字進行凱撒加密
- 只有英文字母會位移，其他字元（數字、標點、空白）保留不變
- 大寫維持大寫、小寫維持小寫

## 執行方式

```bash
python main.py < input.txt
```

## 測試

```bash
python test_main.py
```
