# AI_LOG

## 題目
UVA 11417 GCD：實作 `sum_of_gcd(n)`，計算
`sum(gcd(i, j) for 1 <= i < j <= n)`。

## 與 AI 討論後拆出的測試案例
1. `n = 2`：只有一組 `(1,2)`，答案應為 `1`。
2. `n = 10`：題目常見範例，答案應為 `67`。
3. edge case `n = 1`：沒有任何 `(i,j)` 配對，答案應為 `0`。
4. `n = 5`：手算驗證中小型案例，答案應為 `11`。

## TDD 流程紀錄
- 先建立 `test_gcd.py`，含上述 4 個測試。
- 紅燈驗證：因尚未建立 `gcd.py`，執行 `python -m unittest test_gcd.py -v` 出現 `ModuleNotFoundError: No module named 'gcd'`。
- 建立 `gcd.py` 並實作 `sum_of_gcd`。
- 綠燈驗證：4 個測試全部 `OK`。

## 主要實作
- 使用 `math.gcd`。
- 兩層迴圈列舉所有 `1 <= i < j <= n`。
- 將每組 `gcd(i, j)` 加總回傳。
- 若 `n < 1`，拋出 `ValueError`。

## Commit 紀錄
1. `test: add failing tests for UVA 11417 GCD`
2. `feat: implement UVA 11417 GCD`
