# AI 使用說明

## 使用目的
1. 協助整理 HOMEWORK.md 中的功能需求
2. 先設計單元測試，再完成戰役引擎
3. 補上繁體中文註解與作業文件

## AI 協助內容
- 拆解 Stage 1、Stage 2、Stage 3 的需求
- 建立 `tests/test_chibi.py`
- 撰寫 `chibi_battle.py`
- 撰寫 `chibi_battle_easy.py`
- 整理 `README.md`、`TEST_CASES.md`、`TEST_LOG.md`

## 人工確認內容
- 檢查測試是否真的覆蓋資料讀取、戰鬥統計與報告輸出
- 檢查輸入資料格式是否符合作業範例
- 確認所有變更都只放在 `weeks/week-07/solutions/1111405040/`
- 執行全部測試與主程式，確認結果正常

## 驗證方式
```powershell
cd weeks/week-07/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

## 驗證結果
- 17 個測試案例全部通過

## 備註
- AI 協助以需求整理、測試設計、程式撰寫與文件整理為主
- 最終提交前已再次檢查程式可執行性與變更範圍
