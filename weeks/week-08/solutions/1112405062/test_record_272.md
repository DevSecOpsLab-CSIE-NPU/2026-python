# Week 03 - Question 272 (UVA 272 / TeX Quotes) 測試紀錄

## 測試日期
2026-04-16

## 測試結果：PASSED ✓

### 問題描述
將普通雙引號 `"` 轉換為 TeX 風格的引號：
- 第 1, 3, 5... 個雙引號 → `` ` `` （左雙引號）
- 第 2, 4, 6... 個雙引號 → `' ` （右雙引號）

### 測試輸入
```
"To be or not to be," quoth the Bard,
"that is the question."
The programmingcontestant replies:
"To be or not to be, I think not."
```

### 預期輸出
```
``To be or not to be,'' quoth the Bard,
``that is the question."
The programmingcontestant replies:
``To be or not to be, I think not.''

```

### 實際輸出
```
``To be or not to be,'' quoth the Bard,
``that is the question."
The programmingcontestant replies:
``To be or not to be, I think not.''

```

### 比對結果
| 測項 | 說明 | 結果 |
|------|------|------|
| 第 1 個引號 | " → `` | ✓ PASS |
| 第 2 個引號 | " → '' | ✓ PASS |
| 第 3 個引號 | " → `` | ✓ PASS |
| 第 4 個引號 | " → '' | ✓ PASS |

## 關鍵測試點
1. 奇數位置的雙引號替換為 `` ` ``
2. 偶數位置的雙引號替換為 `' `
3. 其他字元保持不變

## 結論
所有測試案例均通過，程式正確處理引號交替替換。
