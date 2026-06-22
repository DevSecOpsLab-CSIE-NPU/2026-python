# 第 2 題 PR SOP

## Branch

Branch 名稱：

```text
0622-1114405040-洪士閔-q2
```

## Red -> Commit

先建立測試檔，
確認尚未實作時測試失敗。

Commit：

```text
test(q2): add failing test
```

## Green -> Commit

加入 `q2_caesar_cipher.py`，
讓測試通過。

Commit：

```text
feat(q2): implement solution
```

## Push

推送分支：

```bash
git push -u origin 0622-1114405040-洪士閔-q2
```

若主倉庫沒有寫入權限，
改推送到個人 fork。

## PR

PR Title：

```text
第2題0622 1114405040洪士閔
```

## Base / Compare

```text
Base: main
Compare: 0622-1114405040-洪士閔-q2
```

## What

完成第 2 題 Caesar Cipher：

- 使用 `SHIFT = 1`
- 大寫字母循環右移
- 小寫字母循環右移
- 非英文字元保持原樣
- 支援逐行讀取直到 EOF
- 補上測試、README、開發紀錄

## Why

本題練習使用字元編碼轉換，
並確認大小寫字母與非英文字元能依照題目規則分別處理。

## Test

已執行：

```bash
py -m unittest test_q2_caesar_cipher.py
```

測試結果：

```text
Ran 3 tests
OK
```

Sample 測試輸出：

```text
Ifmmp, OQV!
bcd YZA
```

Edge Case 測試輸出：

```text
Aa 123!?
```
