# Week 13 作業提交 - 1114405035

本週作業包含 5 題 CPE 演算法解題以及 2 項招生數據視覺化分析任務。所有程式碼與測試檔案均已建立並通過驗證。

---

## 檔案結構

```text
weeks/week-13/solutions/1114405035/
├── 11005.py                   # CPE 11005 標準版 (Cheapest Base)
├── 11005-easy.py              # CPE 11005 易記版
├── 11063.py                   # CPE 11063 標準版 (RGB -> XYZ)
├── 11063-easy.py              # CPE 11063 易記版
├── 11150.py                   # CPE 11150 標準版 (Frog Single Log Bridge)
├── 11150-easy.py              # CPE 11150 易記版
├── 11321.py                   # CPE 11321 標準版 (Inke's Trap Path)
├── 11321-easy.py              # CPE 11321 易記版
├── 11332.py                   # CPE 11332 標準版 (Mirror Visibility)
├── 11332-easy.py              # CPE 11332 易記版
├── task1_grouped_bar.py       # Task 1：三年並排長條圖繪製
├── task2_zipcode_heatmap.py   # Task 2：來源縣市熱力圖繪製
├── output/                    # 圖表輸出目錄
│   ├── task1.png              # Task 1 輸出圖
│   └── task2.png              # Task 2 輸出圖
├── tests/                     # 單元測試目錄
│   ├── test_11005.py          # 11005 單元測試
│   ├── test_11005.log         # 11005 測試日誌
│   ├── test_11063.py          # 11063 單元測試
│   ├── test_11063.log         # 11063 測試日誌
│   ├── test_11150.py          # 11150 單元測試
│   ├── test_11150.log         # 11150 測試日誌
│   ├── test_11321.py          # 11321 單元測試
│   ├── test_11321.log         # 11321 測試日誌
│   ├── test_11332.py          # 11332 單元測試
│   ├── test_11332.log         # 11332 測試日誌
│   ├── test_task1.py          # Task 1 單元測試
│   └── test_task2.py          # Task 2 單元測試
├── TEST_LOG.md                # 測試執行歷程日誌 (Red -> Green 紀錄)
├── REPORT.md                  # 視覺化圖表數據分析心得報告
├── AI_USAGE.md                # AI 協助開發聲明與紀錄
└── README.md                  # 本說明文件
```

---

## 依賴套件

本週視覺化任務需要安裝以下第三方套件：
*   `matplotlib` (用於繪圖)
*   `numpy` (用於數據矩陣運算)

---

## 執行與測試方式

### 1. 執行招生資料視覺化繪圖

在 `solutions/1114405035/` 目錄下執行：

```bash
# 產生 Task 1 三年並排長條圖
python task1_grouped_bar.py

# 產生 Task 2 來源縣市熱力圖
python task2_zipcode_heatmap.py
```
繪圖完成後，PNG 圖表將自動儲存於 `output/` 資料夾中。

### 2. 執行單一測試

```bash
python -m unittest tests/test_task1.py
python -m unittest tests/test_task2.py
python -m unittest tests/test_11005.py
```

### 3. 一鍵執行所有單元測試

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
所有 17 個單元測試均可在一秒內全數通過。
