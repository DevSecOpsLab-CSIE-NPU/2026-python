# Week 04 作業：1114405035

本目錄包含 Week 04 的五題 UVA 解題程式與測試。

## 目錄結構

- `uva948.py` - UVA 948：假幣判斷
- `uva10008.py` - UVA 10008：密碼翻譯字頻統計
- `uva10019.py` - UVA 10019：Hashmat 戰士差距
- `uva10035.py` - UVA 10035：進位計算
- `uva10038.py` - UVA 10038：Jolly Jumper 判斷
- `tests/test_week04.py` - 週次測試檔
- `TEST_CASES.md` - 測試案例說明
- `TEST_LOG.md` - 測試執行日誌
- `AI_USAGE.md` - AI 使用紀錄
- `assets/` - 遊戲截圖或相關補充檔案（本週可空）

## 執行方式

### UVA 程式
```bash
python uva948.py < input.txt
python uva10008.py < input.txt
python uva10019.py < input.txt
python uva10035.py < input.txt
python uva10038.py < input.txt
```

### 單元測試
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 注意事項

- 目前各題程式皆已實作並包含中文註解
- 若要上傳，請放在 `weeks/week-04/solutions/1114405035/`
- 需建立 `submit/week-04` 分支並推送到 fork
