# AI 使用說明

## 使用目的
1. 協助整理 `week-13` 的題目需求。
2. 先設計單元測試，再完成正式版與簡單版程式。
3. 補上繁體中文註解與文件。

## 使用方式
1. 先閱讀 `week-13/README.md`，確認本週需要完成的 5 題。
2. 檢查各題 `QUESTION-*.md` 後，發現多份內容與題號不一致。
3. 依題號對應的正式 UVA 題意建立測試案例。
4. 根據測試結果完成程式，並同步提供正式版與簡單版。
5. 執行全部測試後，整理測試紀錄與作業文件。

## AI 協助內容
- 建立 5 份 `unittest` 測試檔。
- 撰寫 5 題正式版程式。
- 撰寫 5 題簡單版程式。
- 補上繁體中文註解。
- 整理 README、TEST_CASES、TEST_LOG。

## 驗證方式
執行指令：

```powershell
cd weeks/week-13/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

驗證結果：
- 15 個測試案例全部通過。

## 備註
- 本次 AI 協助以程式撰寫、測試設計與文件整理為主。
- 題意判讀以 `week-13/README.md` 的題號清單與對應 UVA 正式題意為準。
