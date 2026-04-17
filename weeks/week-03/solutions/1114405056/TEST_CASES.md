# 測試案例文件

**學號**：1114405056  
**姓名**：尤靖崵

---

## UVA 100 - The 3n+1 Problem

### 官方範例
| 輸入 | 輸出 |
|------|------|
| `1 10` | `1 10 20` |
| `100 200` | `100 200 125` |
| `201 210` | `201 210 89` |
| `900 1000` | `900 1000 174` |

### 邊界測試
| 輸入 | 輸出 | 說明 |
|------|------|------|
| `10 1` | `10 1 20` | 輸入順序顛倒 |
| `22 22` | `22 22 16` | 單一數字 |
| `500 600` | `500 600 137` | 較大區間 |

---

## UVA 118 - Mutant Flatworld Explorers

### 官方範例
**輸入**：
```
4 8
(0, 2, E) FLFRFRFRF
(1, 0, S) FFLJFLFL
(3, 2, N) FFLLFFFFFLFLFL
```

**輸出**：
```
(1, 1, E)
(0, 3, W) LOST
(2, 3, S)
```

### 邊界測試
- 無氣味時機器人墜落後後續機器人繼續執行
- 有氣味位置忽略會墜落的指令

---

## UVA 272 - TeX Quotes

### 官方範例
**輸入**：
```
"To be or not to be," quoth the Bard, "that
is the question".
The programming contestant replied: "I must disagree.
To me the enobling force of my life is the promise that one day I will work
on a real computer.  I really not kidding!"
```

**輸出**：
```
``To be or not to be,'' quoth the Bard, ``that
is the question''.
The programming contestant replied: ``I must disagree.
To me the enobling force of my life is the promise that one day I will work
on a real computer.  I really not kidding!''
```

### 邊界測試
| 輸入 | 輸出 | 說明 |
|------|------|------|
| `"a" "b"` | ` ``a'' ``b''` | 多對引號 |
| 無引號文字 | 原樣輸出 | 無引號不變 |

---

## UVA 299 - Train Swapping

### 官方範例
**輸入**：
```
3
3
1 2 3
4
4 3 2 1
5
2 4 1 3 5
```

**輸出**：
```
Optimal train swapping takes 0 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 3 swaps.
```

### 邊界測試
| 序列 | 逆序對數 | 說明 |
|------|----------|------|
| `[2, 1]` | 1 | 兩元素反序 |
| `[6, 5, 4, 3, 2, 1]` | 15 | 完全反序 C(6,2) |
| `[1]` | 0 | 單元素 |

---

## UVA 490 - Rotating Sentences

### 官方範例
**輸入**：
```
HELLO
WORLD
```

**輸出**：
```
WH
OE
RL
LL
DO
```

### 邊界測試
| 輸入 | 輸出 | 說明 |
|------|------|------|
| `ABC` (單行) | `C`, `B`, `A` (三行) | 單行轉多列 |
| 長度不等的行 | 補空格後旋轉 | 不等長行處理 |
