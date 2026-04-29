# Week 03 - Question 299 (UVA 299 / Train Swapping) 測試紀錄

## 測試日期
2026-04-16

## 測試結果：PASSED ✓

### 問題描述
計算將火車車廂從任意順序排列成 1~L 順序所需的最少相鄰交換次數。
此數值等於陣列中的「逆序對」數量。

### 測試輸入
```
3
3
1 3 2
4
4 3 2 1
6
1 2 3 4 5 6
```

### 預期輸出
```
Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 0 swaps.
```

### 實際輸出
```
Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 0 swaps.
```

### 比對結果
| 測項 | 車廂順序 | 逆序對 | 預期 | 實際 | 結果 |
|------|----------|--------|------|------|------|
| 1 | 1 3 2 | (3,2) | 1 | 1 | ✓ PASS |
| 2 | 4 3 2 1 | 6對 | 6 | 6 | ✓ PASS |
| 3 | 1 2 3 4 5 6 | 0 | 0 | 0 | ✓ PASS |

## 關鍵測試點
1. **完全逆序** [4 3 2 1]：逆序對數量 = 6 = n*(n-1)/2
2. **已排序** [1 2 3 4 5 6]：逆序對數量 = 0
3. **部分亂序** [1 3 2]：逆序對數量 = 1

## 結論
所有測試案例均通過，程式正確計算逆序對數量（最少交換次數）。
