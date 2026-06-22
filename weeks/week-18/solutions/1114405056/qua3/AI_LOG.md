# 題目三 任意進位的數字根 (Digital Root)

## 開發前思考

根據開工檢查表，我需要實現：

1. **函式簽名**：`digital_root_base(n, base)`
   - 接收十進位大整數 N 與進位基底 base
   - 回傳該數字在該進位底下的數字根

2. **輸入邊界**：多組測試資料
   - 每一行有兩個整數 N 和 Base
   - 當讀到 N = 0 且 Base = 0 時代表輸入結束

3. **例外處理**：
   - 防範讀到空行或格式錯誤爆 `ValueError`
   - 遵守 OpenSSF 安全規範，用特定的 `except` 捕捉

4. **Edge Case**：
   - N 本身就小於 Base
   - 剛好是 Base - 1 的倍數

我的學號末兩碼為 56，個位數 u = 6，所以 BASE = 9。

### 快速計算方法

發現數字根有一個快速計算公式：
```
if n == 0:
    return 0
else:
    return 1 + (n - 1) % (base - 1)
```

這是因為在進位 base 下，
數字 N 的各位數之和與 N 本身在模 (base-1) 的意義下同餘。

## 驗收標準確認

✓ 輸入 9 9 ➔ 輸出 1（9 在九進位是 10 ➔ 1+0=1）
- 驗證：1 + (9 - 1) % (9 - 1) = 1 + 8 % 8 = 1 + 0 = 1 ✓

✓ 輸入 80 9 ➔ 輸出 8（80 在九進位是 88 ➔ 8+8=16 ➔ 16 在九進位是 17 ➔ 1+7=8）
- 驗證：1 + (80 - 1) % (9 - 1) = 1 + 79 % 8 = 1 + 7 = 8 ✓

## Red 階段

我先建立測試檔 `test_q3_digital_root.py`，
在尚未加入主程式時執行測試，
結果為失敗。
失敗原因是 `q3_digital_root.py` 尚未存在，
符合先建立測試再完成實作的流程。

測試包含：
- 基本測試：8 in base 8
- 複雜測試：63 in base 8
- Edge Case：5 in base 8（5 < 8）
- Edge Case：14 in base 8（7 的倍數）
- 多行輸入測試

## Green 階段

我加入 `q3_digital_root.py` 後重新執行測試，
`py -m unittest test_q3_digital_root.py` 通過。
另外也用範例輸入確認輸出格式正確。

通過結果：

```text
Ran 6 tests
OK
```

## 例外處理確認

✓ 防範空行：使用 `if not line.strip()` 跳過
✓ 防範格式錯誤：檢查 `len(parts) != 2` 並拋出 `ValueError`
✓ 捕捉異常：使用特定的 `except ValueError` 和 `except EOFError`

## Commit 紀錄

本題提交紀錄：

```text
test(q3): add failing test
feat(q3): implement digital root solution
docs(q3): update development log and README
```

本題沒有發現需要額外修正的明顯錯誤。

## PR 紀錄

Branch：

```text
0622-1114405056-Digital_Root
```

PR Title：

```text
第3題0622 1114405056 Digital Root
```

PR Base / Compare：

```text
Base: main
Compare: 0622-1114405056-Digital_Root
```

PR 說明會包含 What、Why、Test 三個部分，
並列出 sample 測試、edge case 測試與最終驗證結果。
