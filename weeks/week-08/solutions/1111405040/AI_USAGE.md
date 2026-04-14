# AI 使用說明

## 使用目的
1. 協助確認 Week 08 題目清單。
2. 協助整理各題正式 UVA 題意。
3. 先建立測試，再完成解題程式。
4. 補上繁體中文註解與作業文件。

## AI 協助內容
- 撰寫 5 題解法。
- 撰寫 5 份 `unittest` 測試檔。
- 整理 README、TEST_CASES、TEST_LOG。
- 協助檢查測試失敗原因。

## 人工確認內容
- 確認 `QUESTION-10190.md`、`QUESTION-10193.md`、`QUESTION-10222.md` 與實際 UVA 題號不一致。
- 確認本次以 `week-08/README.md` 題號清單和正式 UVA 題意為準。
- 執行全部測試並確認通過。
- 檢查變更範圍只在 `weeks/week-08/solutions/1111405040/`。

## 驗證方式
```powershell
cd weeks/week-08/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

## 驗證結果
- 17 個測試案例全部通過。
