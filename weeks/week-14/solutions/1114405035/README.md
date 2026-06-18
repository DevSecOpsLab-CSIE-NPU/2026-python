# Week 14 作業提交 - 1114405035

本週作業為綜合練習，包含 4 題 CPE 演算法解題。所有程式碼與測試檔案均已建立並通過驗證。

---

## 檔案結構

```text
weeks/week-14/solutions/1114405035/
├── 11349.py                   # CPE 11349 標準版 (Symmetric Matrix)
├── 11349-easy.py              # CPE 11349 易記版
├── 11417.py                   # CPE 11417 標準版 (GCD)
├── 11417-easy.py              # CPE 11417 易記版
├── 11461.py                   # CPE 11461 標準版 (Square Numbers)
├── 11461-easy.py              # CPE 11461 易記版
├── 12019.py                   # CPE 12019 標準版 (Doom's Day Algorithm)
├── 12019-easy.py              # CPE 12019 易記版
├── tests/                     # 單元測試目錄
│   ├── test_11349.py          # 11349 單元測試
│   ├── test_11349.log         # 11349 測試日誌
│   ├── test_11417.py          # 11417 單元測試
│   ├── test_11417.log         # 11417 測試日誌
│   ├── test_11461.py          # 11461 單元測試
│   ├── test_11461.log         # 11461 測試日誌
│   ├── test_12019.py          # 12019 單元測試
│   └── test_12019.log         # 12019 測試日誌
├── TEST_LOG.md                # 測試執行歷程日誌 (Red -> Green 紀錄)
├── AI_USAGE.md                # AI 協助開發聲明與紀錄
├── PR_DESCRIPTION.md          # PR 說明文件
└── README.md                  # 本說明文件
```

---

## 執行與測試方式

### 1. 執行單一測試

在 `solutions/1114405035/` 目錄下執行：

```bash
python -m unittest tests/test_11349.py
python -m unittest tests/test_11417.py
```

### 2. 一鍵執行所有單元測試

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
所有 4 個單元測試均可全數通過。
