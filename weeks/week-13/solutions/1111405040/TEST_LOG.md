# Week 13 測試紀錄

## 開發流程
1. 先閱讀 `week-13/README.md`，確認本週需要完成的 5 題。
2. 檢查各題 `QUESTION-*.md` 後，發現多份內容與題號不一致。
3. 依題號對應的正式 UVA 題意先撰寫 5 份 `unittest` 測試檔。
4. 完成正式版、簡單版與 hand 版程式。
5. 執行全部測試，修正失敗案例。
6. 最後補上 README、測試案例說明與 AI 使用紀錄。

## 第一次測試結果
執行指令：

```powershell
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s weeks/week-13/solutions/1111405040/tests -p "test_*.py" -v
```

結果摘要：
- 15 個測試案例全部通過。
- 正式版、簡單版與 hand 版輸出一致。

本次沒有額外失敗案例需要修正。

## 修正後測試結果
執行指令：

```powershell
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s weeks/week-13/solutions/1111405040/tests -p "test_*.py" -v
```

結果摘要：
- 15 個測試案例全部通過。

```text
Ran 15 tests in 0.002s

OK
```

## 結論
- 5 題正式版程式完成。
- 5 題簡單版程式完成。
- 5 題 hand 版程式完成。
- 15 個測試案例全部通過。
- 本次變更範圍僅在 `weeks/week-13/solutions/1111405040/`。
