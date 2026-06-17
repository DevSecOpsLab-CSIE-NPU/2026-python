# AI_LOG — 6/11 排序效能實驗室

## 我問 AI 什麼（逐字記錄）

### Stage 1：timeit
回答 AI 提問：簽名、例外處理（選 A：記錄後 re-raise）、範圍（any function）、edge case、驗收標準

### Stage 2：三種排序
回答 AI 提問：簽名、邊界條件（含空/單一/已排好）、例外（選 B：主動 raise TypeError）、edge case 清單、驗收

### Stage 3：加速實驗
```
你能載嗎
```
（確認 Cython — 環境無 C compiler，果斷轉演算法優化）

```
OK
```

### Stage 4：畫圖
```
你處理
```

### Stage 5：安全性自掃
無提問，AI 直接掃程式後提出 3 項修正並寫測試

## AI 給了什麼

每個階段按照 TDD 循環：
1. 資訊檢查表問答確認規格
2. 寫測試 → 紅燈 → `test:` commit
3. 寫實作 → 綠燈 → `feat:` commit
4. 階段閘門概念提問

## 我改了什麼

- Stage 3: 決定不走 Cython（無編譯器），改 cocktail shaker + median-of-three + insertion threshold 演算法優化
- Stage 5: `make_data` 加入 `n < 0` 檢查，改用區域 `Random` 避免汙染全域狀態；`load_results` 補抓 `JSONDecodeError`
