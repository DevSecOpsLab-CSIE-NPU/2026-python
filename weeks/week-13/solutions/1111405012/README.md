# Week 13 解題紀錄

student-id：`1111405012`

## 完成題號

- [QUESTION-11005](../../QUESTION-11005.md)
- [QUESTION-11063](../../QUESTION-11063.md)
- [QUESTION-11150](../../QUESTION-11150.md)
- [QUESTION-11321](../../QUESTION-11321.md)
- [QUESTION-11332](../../QUESTION-11332.md)

## 目錄結構

```markdown
weeks\week-13\solutions\1111405012
├── README.md                  # 作業說明
├── AI_USAGE.md                # AI 使用紀錄
├── TEST_CASES.md              # 測試案例整理
├── TEST_LOG.md                # 測試執行紀錄
│
├── QUESTION_*.py              # AI 撰寫初始版本（含中文註解）
├── QUESTION_*-easy.py         # AI 撰寫簡單版本（含中文註解）
├── QUESTION_*-hand.py         # 手打版本（原則上不含中文註解）
│
├── test_support.py            # 動態模組加載工具：加載題目解法
│
└── tests/
    ├── test_question_11005.py # 單元測試
    ├── test_question_11063.py
    ├── test_question_11150.py
    ├── test_question_11321.py
    └── test_question_11332.py
```

## 目錄用途

- 題目正式程式：放在此資料夾下
- 測試程式：放在 `tests/`
- 測試紀錄：寫入 `TEST_LOG.md`
- 測試案例整理：寫入 `TEST_CASES.md`
- AI 使用紀錄：寫入 `AI_USAGE.md`

## 依賴套件
- 無

## 執行方式

### 單題程式
```bash
python <filename>.py < input.txt
```

### 單元測試
```bash
python -m unittest discover -s "weeks/week-13/solutions/1111405012/tests" -p "test_*.py" -v
```

> [!NOTE]
> 如想執行測試請另行準備測資檔案或手動輸入測資（Stdin）。

## 補充說明
- 目錄結構採用 `docs\WEEK02_EVALUATION_GUIDE.md` 所描述之 "Submission Structure"。
- 作業題目主體程式之命名採用「原檔案名稱 + `-easy`/`-hand`（版本 Tag）」的原則，Python 程式副檔名為 `.py`。
- 
