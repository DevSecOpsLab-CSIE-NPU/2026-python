# Week 12 作業提交 - 1114405035

## 完成題號與項目

### 1. CPE 題庫挑戰 (5 題)
- **QUESTION-10812** — Beat the Spread!
- **QUESTION-10908** — Largest Square
- **QUESTION-10922** — 2 the 9s
- **QUESTION-10929** — You can say 11
- **QUESTION-10931** — Parity

### 2. 課堂範例註釋與整理 (9 個範例)
本週合併 Week 11 停課補課，已針對以下 Week 10 與 Week 11 課堂範例補齊詳細的繁體中文註釋並拷貝至本目錄下：
- `R01-csv-basic.py`
- `R02-json-basic.py`
- `R03-xml-parse.py`
- `R04-encoding-hex-base64.py`
- `R05-stats-counter.py`
- `R01-class-basic.py`
- `R02-property.py`
- `R03-inheritance.py`
- `R04-special-methods.py`

---

## 檔案結構說明
每一題均包含四個對應檔案（例如以 10812 為例）：
1. `10812-easy.py`：AI 建議的簡單、易讀版本（含詳細中文註釋）。
2. `10812.py`：手打並優化的程式版本（含詳細中文註釋）。
3. `test_10812.py`：單元測試程式。
4. `test_10812.log`：單元測試執行結果日誌。

## 執行與測試方式

### 執行特定解題程式：
```bash
python 10812.py
python 10908.py
python 10922.py
python 10929.py
python 10931.py
```

### 執行單元測試：
```bash
python -m unittest test_10812.py
python -m unittest test_10908.py
python -m unittest test_10922.py
python -m unittest test_10929.py
python -m unittest test_10931.py
```

## 依賴套件
- 本作業僅使用 Python 3 標準內建函式庫（如 `sys`、`io`、`unittest`、`csv`、`json` 等），無需安裝額外套件。
