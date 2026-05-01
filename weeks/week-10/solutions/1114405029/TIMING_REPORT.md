# TIMING_REPORT

## 執行結果

```text
[timeit] read_csv 耗時 0.039912s
[timeit] write_json 耗時 0.001980s
[timeit] read_json 耗時 0.009801s
[timeit] write_xml 耗時 0.001806s
```

---

# 問題回答

## 1. 哪個操作最耗時？你認為原因是什麼？

本次實驗中，`read_csv` 是四個函式中耗時最高的操作，執行時間約為 `0.039912s`。

我認為主要原因是 CSV 屬於較原始的純文字資料格式，Python 在讀取時需要逐列解析資料內容，再依照欄位名稱建立 dictionary 結構。此外，本次 CSV 檔案包含多筆學生資料與多個欄位，因此在解析與轉換過程中需要額外的處理時間。

另外，本次 CSV 使用 `utf-8-sig` 編碼讀取，程式也需要處理 BOM（Byte Order Mark），因此讀取成本會比已經結構化的 JSON 格式更高。

相較之下，JSON 本身已經具有明確的階層化資料結構，因此在 Python 中可以較快速地轉換成 dict 與 list 物件。

---

## 2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？

本次結果如下：

- `read_csv`：0.039912s
- `read_json`：0.009801s

可以觀察到 `read_csv` 明顯比 `read_json` 慢。

這與課堂 U01 的資料格式效能比較實驗結果大致一致。

原因在於：

CSV 屬於較低階的文字格式，Python 必須：

1. 逐列讀取資料
2. 解析逗號分隔欄位
3. 建立 dictionary
4. 處理欄位名稱與資料格式

而 JSON 本身已經具有階層化結構，因此 Python 在解析時可以直接轉換成 dict 與 list。

此外，本次作業中的 JSON 是經過 Task 1 篩選後的結果，因此資料量比原始 CSV 小，這也是 `read_json` 耗時較低的原因之一。

---

## 3. write_xml 比 write_json 快還是慢？原因為何？

本次結果如下：

- `write_json`：0.001980s
- `write_xml`：0.001806s

可以看出本次實驗中 `write_xml` 稍微比 `write_json` 快。

我認為原因有以下幾點：

### （1）本次 XML 結構較簡單

本次 XML 採用：

```xml
<student id="" dept="" school="" zip="" />
```

這種屬性型式，因此 XML 標籤結構相對單純。

---

### （2）JSON 有進行格式化輸出

在 `json.dump()` 中使用了：

```python
indent=2
```

Python 需要額外處理換行與縮排，因此輸出時會增加一些時間成本。

---

### （3）資料量不算非常大

本次資料量有限，因此 XML 與 JSON 的差距並不明顯。

如果資料量持續增加，XML 標籤與樹狀結構的成本可能會逐漸提高。

---

## 4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？

如果資料筆數從 100 筆增加到 10000 筆，我預期四個函式的執行時間都會明顯增加。

---

### read_csv

`read_csv` 的增加幅度可能最明顯。

因為：

- CSV 需要逐列解析
- 每列都要建立 dictionary
- 欄位數越多，處理成本越高

因此資料量增加後，CSV 的解析時間通常會快速上升。

---

### write_json

`write_json` 的耗時也會增加。

因為：

- Python 需要將大量 dict 序列化
- `indent=2` 會增加格式化成本
- 輸出檔案大小也會增加

因此輸出時間會隨資料量成長。

---

### read_json

`read_json` 也會變慢，但我認為增加幅度可能仍低於 CSV。

因為 JSON 本身已經是結構化格式，因此 Python 不需要像 CSV 一樣重新解析欄位。

---

### write_xml

`write_xml` 在大量資料下也會逐漸增加耗時。

原因包括：

- 需要建立大量 `<student>` 標籤
- ElementTree 需要管理完整 XML 樹狀結構
- 屬性與節點數量增加後，記憶體與輸出成本都會提高

因此在大規模資料下，XML 的成本也會變得更加明顯。

---

# 總結

透過本次作業，我實際比較了 CSV、JSON 與 XML 三種資料格式在 Python 中的處理方式與效能差異。

本次結果顯示：

- `read_csv` 的解析成本最高
- JSON 在 Python 中具有良好的可讀性與處理效率
- XML 雖然結構明確，但資料量增加後標籤成本也會提高

此外，我也學習到：

- 如何使用 `@timeit` decorator 量測函式執行時間
- 如何利用 `csv`、`json`、`ElementTree` 處理不同資料格式
- 如何使用 `matplotlib` 與 `seaborn` 製作效能比較圖

透過這次作業，我對 Python 的資料格式處理與效能分析有更深入的理解。