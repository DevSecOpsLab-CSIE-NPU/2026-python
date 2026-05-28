# Week 08｜檔案與 I/O 練習題

**資料來源：** `stu-data/` 資料夾，內含國立澎湖科技大學 109～114 學年度新生資料庫  
**欄位：** `序、學校名稱、系所名稱、學制名稱、班級名稱、學號、入學方式、原具身份、招生類別、郵遞區號、畢業學校、前畢業科系`

> 注意：所有 CSV 檔案編碼為 **UTF-8-BOM**，開啟時請使用 `encoding='utf-8-sig'`

---

## 題目一：讀取 CSV 並篩選輸出

**對應知識點：5.1 讀寫文字資料**

### 任務

1. 讀取 `stu-data/113年新生資料庫.csv`
2. 篩選出 **入學方式 == `繁星推甄`** 的學生
3. 在 `week-08/` 下建立 `output/` 資料夾，將結果寫入 `output/113_star.txt`
4. 輸出格式如下：

```
系所名稱 | 學號 | 畢業學校
應用外語系 | 1113402005 | 國立馬公高中
...
共 XX 筆
```

### 提示

- `open(..., encoding='utf-8-sig')` 可自動去除 BOM 字元
- `print(..., file=f)` 可將輸出導向檔案
- 用 `csv.DictReader` 讀取，每列是一個 dict

---

## 題目二：安全建立報告檔（不覆蓋既有檔案）

**對應知識點：5.5 檔案不存在時才寫入**

### 任務

寫一個函式 `safe_report(year)`：

1. 讀取對應年份的 CSV，統計各 **入學方式** 的人數
2. 嘗試將統計結果寫入 `output/{year}_report.txt`
3. 若檔案**已存在**，印出警告訊息並停止，**不覆蓋**

依序呼叫：

```python
safe_report(109)
safe_report(110)
safe_report(114)
safe_report(109)   # 第二次呼叫，應看到警告
```

### 提示

- 使用 `open(..., 'x')` 模式，檔案已存在時會自動拋出 `FileExistsError`
- 用 `try / except FileExistsError` 捕捉並印出提示

### 預期輸出範例

```
109 年報告已建立：output/109_report.txt
110 年報告已建立：output/110_report.txt
114 年報告已建立：output/114_report.txt
⚠️  output/109_report.txt 已存在，略過。
```

---

## 題目三：用 StringIO 做資料清洗測試

**對應知識點：5.6 在字串上執行 I/O 操作**

### 任務

實作函式 `parse_students(file_obj)` 接受**任何類檔案物件**，回傳 `list[dict]`。

1. 用真實檔案 `stu-data/114年新生資料庫.csv` 呼叫它，印出前 3 筆
2. 用 `io.StringIO` 包裝下方**測試字串**呼叫它，**不建立任何實體檔案**：

```
序,學校名稱,系所名稱,學號,入學方式
1,測試大學,資工系,A001,甄選入學
2,測試大學,電機系,A002,繁星推甄
```

3. 確認兩種呼叫方式都能正常解析，結構一致

### 提示

- `io.StringIO(string)` 產生可當成檔案物件的字串流
- `csv.DictReader` 可接受任何可迭代的類檔案物件，不限定真實檔案

### 思考問題

> 為什麼要讓函式接受「類檔案物件」而不是直接接受「檔案路徑」？這在測試與部署上有什麼好處？

---

## 題目四：合併六年資料並壓縮封存＋趨勢視覺化

**對應知識點：5.7 讀寫壓縮的資料檔案**

### 任務

1. 讀取 109～114 全部六個 CSV，在每筆資料加上 `年份` 欄位
2. 將合併後的資料（保留 CSV 格式）寫入 `output/all_years.csv.gz`
3. 讀取 `output/all_years.csv.gz`，統計每年的學生人數，印出招生趨勢
4. 印出壓縮檔的大小（bytes）
5. **【視覺化】** 用 seaborn 繪製「109～114 學年度招生人數趨勢」折線圖，存成 `output/trend.png`

### 視覺化規格

- X 軸：學年度（109～114）
- Y 軸：招生人數
- 在每個資料點標上人數數字
- 圖表標題：`澎科大 109～114 學年度招生人數趨勢`
- 存檔後印出 `「圖表已儲存：output/trend.png」`

```python
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Taipei Sans TC Beta'  # 中文字型

# 範例資料結構（從上方統計結果取得）
years  = [109, 110, 111, 112, 113, 114]
counts = [682, 590, 578, 517, 437, 412]   # 替換成你實際統計的結果

# TODO: 用 sns.lineplot 畫折線圖，標上每點數字，存成 output/trend.png
```

### 提示

- `gzip.open('檔名', 'wt', encoding='utf-8')` 可以像普通文字檔一樣寫入
- `csv.DictWriter` 可搭配 gzip 使用
- 用 `os.path.getsize()` 取得檔案大小
- `plt.text(x, y, str(y))` 可在折線圖上標注數字
- `plt.savefig('output/trend.png', dpi=150, bbox_inches='tight')` 儲存圖片

### 預期輸出範例

```
109 年：682 人
110 年：590 人
111 年：578 人
112 年：517 人
113 年：437 人
114 年：412 人
壓縮後大小：XX,XXX bytes
圖表已儲存：output/trend.png
```

---

## 題目五：用 pickle 建立年度招生統計快取＋入學方式分佈圖

**對應知識點：5.21 序列化 Python 物件**

### 任務

招生統計若每次都重新讀 CSV 計算會很慢，設計一個**快取機制**。

實作函式 `get_stats(year)` 回傳以下結構的 dict：

```python
{
    'total': 總人數,
    'by_admission': {入學方式: 人數, ...},
    'by_dept':      {系所名稱: 人數, ...},
    'top_school':   最多學生來自的高中名稱
}
```

快取邏輯：

- 若 `output/{year}_stats.pkl` **存在** → 直接載入並回傳，印出 `「從快取載入」`
- 若**不存在** → 從 CSV 計算，儲存成 pkl 後回傳，印出 `「重新計算並快取」`

測試方式：

```python
for year in [112, 113, 112, 113]:
    stats = get_stats(year)
    top = max(stats['by_admission'], key=stats['by_admission'].get)
    print(f"{year} 年｜總人數：{stats['total']}｜最多入學方式：{top}")
```

### 【視覺化】入學方式分佈橫條圖

取得 113 年的統計快取後，繪製各入學方式的人數橫條圖，存成 `output/113_admission.png`

- X 軸：人數
- Y 軸：入學方式（依人數由大到小排序）
- 圖表標題：`113 學年度入學方式分佈`
- 存檔後印出 `「圖表已儲存：output/113_admission.png」`

```python
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Taipei Sans TC Beta'  # 中文字型

stats_113 = get_stats(113)
by_adm = stats_113['by_admission']   # {入學方式: 人數}

# TODO: 整理成排序後的列表，用 sns.barplot 畫橫條圖，存成 output/113_admission.png
```

### 提示

- `pickle.dump(obj, f)` 需以 `'wb'` 模式開檔
- `pickle.load(f)` 需以 `'rb'` 模式開檔
- `collections.Counter` 可快速統計，並支援 `.most_common()`
- `sns.barplot(x=counts, y=labels, orient='h')` 畫橫條圖
- `plt.tight_layout()` 防止中文標籤被裁切

### 預期輸出範例

```
重新計算並快取：112
重新計算並快取：113
從快取載入：112
從快取載入：113
112 年｜總人數：517｜最多入學方式：甄選入學
113 年｜總人數：437｜最多入學方式：甄選入學
112 年｜總人數：517｜最多入學方式：甄選入學
113 年｜總人數：437｜最多入學方式：甄選入學
圖表已儲存：output/113_admission.png
```

---

## 課堂總覽

| 題目 | 知識點 | 資料應用 | 難度 |
|------|-------|---------|------|
| 1 | `open()` + encoding + 篩選寫入 | 篩選繁星推甄學生 | ⭐ |
| 2 | `'x'` 模式 + `FileExistsError` | 年度報告防覆蓋 | ⭐ |
| 3 | `io.StringIO` 介面一致性 | 讓解析函式可單元測試 | ⭐⭐ |
| 4 | `gzip.open()` + `seaborn.lineplot` | 六年資料合併封存 + 趨勢折線圖 | ⭐⭐ |
| 5 | `pickle` 序列化 + `seaborn.barplot` | 招生統計快取 + 入學方式分佈圖 | ⭐⭐⭐ |
