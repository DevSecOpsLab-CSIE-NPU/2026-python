# TEST_LOG - A01 資料清理

## 紅燈階段

**執行指令：**
```
python -m unittest test_A01.py -v
```

**結果：**
```
Ran 10 tests in 0.004s
FAILED (errors=10)
```

**修改前狀態：** `clean_data` 只有 `raise NotImplementedError`，所有測試都 ERROR。

---

## 綠燈階段

**執行指令：**
```
python -m unittest test_A01.py -v
```

**結果：**
```
Ran 10 tests in 0.000s
OK
```

**修改內容：** 實作 `clean_data`：set + loop 去重保序 → list comprehension 整除篩選 → sorted 升冪排序。
