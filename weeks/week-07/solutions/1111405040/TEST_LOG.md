# Week 07 測試紀錄

## 開發流程
1. 先根據 `week-07/README.md` 的題號清單整理正確題意。
2. 先撰寫 5 份 `unittest` 測試檔。
3. 再完成正式版與簡單版程式。
4. 執行全部測試，修正失敗案例。
5. 最後補上 README、測試案例說明與 AI 使用紀錄。

## 第一次測試結果
執行指令：

```powershell
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s weeks/week-07/solutions/1111405040/tests -p "test_*.py" -v
```

結果摘要：
- 其餘題目通過。
- `UVA 10170` 的大數測試失敗。

失敗原因：
- 問題不在程式邏輯，而是測試中手動填寫的大數預期值寫錯。
- 重新用等差級數公式驗算後，正確答案應為 `1414249`。

## 修正後測試結果
再次執行同一指令，結果如下：

```text
Ran 21 tests in 0.002s

OK
```

## 結論
- 5 題正式版程式完成。
- 5 題簡單版程式完成。
- 21 個測試案例全部通過。
- 本次變更範圍僅在 `weeks/week-07/solutions/1111405040/`。
