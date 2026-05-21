# Week 13 招生資料視覺化分析 - 解題報告

## 專案概述

本專案面對 Week 13 作業要求，使用 Python 對澎湖科技大學 109～114 年新生招生資料進行視覺化分析，包括：
1. **Task 1**：繪製三年並排長條圖，分析各系招生人數變化
2. **Task 2**：繪製縣市熱力圖，分析地域生源分佈

---

## 目錄結構

```
weeks/week-13/solutions/1114405017/
├── task1_grouped_bar.py        # Task 1：三年並排長條圖程式
├── task2_zipcode_heatmap.py    # Task 2：縣市熱力圖程式
├── output/                     # 程式自動產生的輸出目錄
│   ├── task1.png              # 三年並排長條圖
│   └── task2.png              # 縣市熱力圖
├── tests/                      # 單元測試目錄
│   ├── __init__.py
│   ├── test_task1.py          # Task 1 測試檔案（5 個測試）
│   └── test_task2.py          # Task 2 測試檔案（7 個測試）
├── TEST_LOG.md                # Red → Green 測試執行紀錄
├── REPORT.md                  # 資料分析心得報告
├── AI_USAGE.md                # AI 使用聲明
└── README.md                  # 本檔案
```

---

## 快速開始

### 前置需求

```bash
pip install pandas matplotlib seaborn numpy
```

### 執行程式

#### 1. 執行 Task 1 - 三年並排長條圖

```bash
python task1_grouped_bar.py
```

**預期輸出**：
- 控制台輸出各年招生統計
- 生成 `output/task1.png` 圖表

#### 2. 執行 Task 2 - 縣市熱力圖

```bash
python task2_zipcode_heatmap.py
```

**預期輸出**：
- 控制台輸出各縣市招生統計
- 生成 `output/task2.png` 圖表

### 執行測試

```bash
# 執行所有測試
python -m unittest discover -s tests -p "test_*.py" -v

# 執行特定測試
python -m pytest tests/test_task1.py -v
python -m pytest tests/test_task2.py -v
```

**預期結果**：所有 12 個測試通過 ✓

---

## 核心函式說明

### Task 1 - 三年並排長條圖

#### `load_year(year: int, data_dir: Path) -> dict[str, int]`
- **功能**：讀取單一年份 CSV，回傳 {系所名稱: 人數}
- **參數**：年份（112/113/114）、資料目錄路徑
- **回傳**：系所名稱與招生人數的字典

#### `get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]`
- **功能**：從多年資料中找出任一年曾進前 top_n 的系所清單
- **參數**：{年份: {系所: 人數}} 嵌套字典、前幾名
- **回傳**：符合條件的系所清單

#### `plot_grouped_bar_chart(year_data, output_path)`
- **功能**：繪製三年並排長條圖
- **視覺效果**：
  - 橫軸：系所名稱（旋轉 45°）
  - 縱軸：人數
  - 三色柱子代表三個年份（紅/綠/藍）
  - 包含圖例與網格線

### Task 2 - 縣市熱力圖

#### `zip_to_county(zipcode: str) -> str`
- **功能**：郵遞區號前 3 碼轉換為縣市名稱
- **回傳**：縣市名稱或「其他」（未知區號）

#### `load_county_counts(year: int, data_dir: Path) -> dict[str, int]`
- **功能**：讀取單一年份，回傳 {縣市: 人數}
- **處理**：自動轉換郵遞區號為縣市
- **回傳**：縣市與招生人數的字典

#### `get_top_counties(all_years: dict[int, dict], top_n: int = 10) -> list[str]`
- **功能**：6 年合計，回傳人數前 top_n 的縣市清單
- **排序**：按總人數由高到低

#### `plot_heatmap(all_years, output_path)`
- **功能**：繪製縣市 × 年份熱力圖
- **視覺效果**：
  - 橫軸：年份（109～114）
  - 縱軸：縣市名稱
  - 顏色深度代表招生人數
  - 每個格子標註具體數字

---

## 主要分析結果

### Task 1 - 系所招生變化

**關鍵發現**：
- **資訊管理系**人數變化最大（-48%，從 42 → 24）
- **觀光休閒系**招生最穩定（61 → 60 → 58）
- 整體來看，103 年至 114 年間各系人數波動明顯

### Task 2 - 地域分佈

**區域排名**（6 年合計）：
1. 台中市：502 人
2. 高雄市：337 人
3. 新北市：264 人
4. 台南市：255 人
5. **澎湖縣：211 人 (6.6%)**
6. 彰化縣：128 人
7. 新竹縣：101 人
8. 台北市：71 人
9. 苗栗縣：65 人

**重要觀察**：招生人數逐年下降（109年 682 → 114年 412，-39.6%）

---

## 測試覆蓋

### Task 1 測試（test_task1.py）

| 測試名稱 | 說明 |
|---------|------|
| `test_load_year_returns_dict` | 驗證回傳型別為 dict |
| `test_load_year_counts_correct` | 驗證計數正確性 |
| `test_load_year_total_positive` | 驗證總人數 > 0 |
| `test_get_top_depts_length` | 驗證結果不超過 top_n |
| `test_get_top_depts_includes_popular` | 驗證包含已知熱門系所 |

### Task 2 測試（test_task2.py）

| 測試名稱 | 說明 |
|---------|------|
| `test_zip_to_county_penghu` | 測試 880 → 澎湖縣 |
| `test_zip_to_county_unknown` | 測試未知區號 → 其他 |
| `test_zip_to_county_taipei` | 測試 100 → 台北市 |
| `test_load_county_counts_type` | 驗證回傳型別為 dict |
| `test_load_county_counts_penghu_positive` | 驗證澎湖縣人數 > 0 |
| `test_get_top_counties_length` | 驗證結果不超過 top_n |
| `test_get_top_counties_sorted` | 驗證結果是列表 |

---

## 技術棧

- **Python 3.10+**
- **Pandas**：資料彙總與處理
- **Matplotlib**：長條圖繪製
- **Seaborn**：熱力圖繪製
- **NumPy**：數值計算
- **Unittest**：單元測試框架

---

## 文件說明

- **TEST_LOG.md**：詳細記錄 TDD 紅綠流程與測試執行結果
- **REPORT.md**：分析與洞察報告（三個問題均已深入回答）
- **AI_USAGE.md**：說明 AI 協助的程式部分與自主完成部分

---

## 進階說明

### 資料路徑配置

程式使用 `pathlib.Path` 動態計算資料路徑：

```python
current_file = Path(__file__).resolve()
# 從 week-13/solutions/1114405017/task1_grouped_bar.py 向上 5 層
data_dir = current_file.parent.parent.parent.parent.parent / "assets" / "stu-data"
```

### CSV 編碼設定

資料檔案包含 UTF-8 BOM，讀取時使用：
```python
df = pd.read_csv(filepath, encoding='utf-8-sig')
```

### 郵遞區號對應

澎湖縣郵遞區號示例：880, 881, 882, 884 等均對應澎湖縣

---

## 可能的改進方向

1. **增加互動式圖表**：使用 Plotly 創建可互動的圖表
2. **時序分析**：分析招生組成的年度變化趨勢
3. **關聯分析**：探索系所特性與地域分佈的關聯
4. **預測模型**：用機器學習預測未來招生趨勢
5. **多維分析**：加入入學方式、性別等其他維度

---

## 聯絡資訊

- **學號**：1114405017
- **作業週次**：Week 13
- **提交日期**：2026 年 5 月

---

## 參考資料

- 課程教材：Python3 Cookbook 第七章（函數）、第八章（類別與物件）
- 資料來源：`assets/stu-data/109～114年新生資料庫.csv`
- 課堂參考圖：`assets/V01-bar.png`, `assets/V02-heatmap.png`
