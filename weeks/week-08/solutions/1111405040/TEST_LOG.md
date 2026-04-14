# Week 08 測試紀錄

## 開發流程
1. 先閱讀 `week-08/README.md`，確認需完成 5 題。
2. 檢查 `QUESTION-*.md` 後，發現部分題目內容與 UVA 題號不一致。
3. 以 README 題號清單與正式 UVA 題意為準，先建立測試。
4. 完成 5 題解法。
5. 執行測試，修正測試案例中的預期值錯誤。
6. 補上 README、TEST_CASES、TEST_LOG、AI_USAGE。

## 第一次測試
執行指令：

```powershell
cd weeks/week-08/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

結果：
- 16 個測試通過
- 1 個測試失敗

失敗原因：
- `QUESTION-10193` 的第三組測試原本使用 `111` 與 `11`。
- 兩者分別為十進位 7 與 3，最大公因數為 1。
- 測試預期誤寫為 love，因此修正成 `110` 與 `100`。

## 修正後測試
再次執行同一指令，結果如下：

```text
Ran 17 tests in 0.001s

OK
```

## 結論
- 5 題解法完成。
- 17 個測試案例全部通過。
- 本次變更範圍只在 `weeks/week-08/solutions/1111405040/`。
