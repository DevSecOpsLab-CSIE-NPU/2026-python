# Week 08 手打程式測試 LOG

**測試日期**：2026-04-16  
**測試指令**：`python -m unittest test_week08 -v`

---

## 測試結果

```
test_10189_minesweeper (test_week08.TestWeek08Hand.test_10189_minesweeper) ... ok
test_10190_rain (test_week08.TestWeek08Hand.test_10190_rain) ... ok
test_10193_arctan (test_week08.TestWeek08Hand.test_10193_arctan) ... ok
test_10221_satellites (test_week08.TestWeek08Hand.test_10221_satellites) ... ok
test_10222_keyboard (test_week08.TestWeek08Hand.test_10222_keyboard) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.244s

OK
```

---

## 各題測試輸入與輸出

### 10189 — Minesweeper（踩地雷）

**輸入** (`test10189.txt`):
```
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

**輸出**:
```
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

---

### 10190 — 雨傘遮雨

**輸入** (`test10190.txt`):
```
2 10 5 3
0 3 2
5 4 1
```

**輸出**:
```
62.50
```

---

### 10193 — 反正切分解

**輸入** (`test10193.txt`):
```
1
```

**輸出**:
```
5
```

說明：`arctan(1/1) = arctan(1/2) + arctan(1/3)`，b+c = 2+3 = 5

---

### 10221 — Satellites（衛星弧長與弦長）

**輸入** (`test10221.txt`):
```
500 30 deg
700 60 min
200 45 deg
```

**輸出**:
```
3633.775503 3592.408346
124.616509 124.614927
5215.043805 5082.035982
```

---

### 10222 — Decode the Mad man（鍵盤解碼）

**輸入** (`test10222.txt`):
```
tyuy
```

**輸出**:
```
were
```

說明：`tyuy` 是 `were` 往右偏移 3 格後的結果，解碼回 `were`
