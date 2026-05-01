# AI_USAGE

## 我詢問 AI 的問題

1. 如何使用 `csv.DictReader()` 讀取 UTF-8-BOM 編碼的 CSV 檔案？
2. 如何使用 `json.dump()` 將 Python dict 輸出成格式化 JSON？
3. 如何使用 `xml.etree.ElementTree` 建立 XML 樹狀結構？
4. 如何將學生資料轉換成 `<student />` 屬性格式的 XML？
5. 如何使用 `@timeit` decorator 量測函式執行時間？
6. 如何使用 `matplotlib` 與 `seaborn` 繪製函式耗時比較圖？
7. 如何讓 matplotlib 與 seaborn 正常顯示中文字型？
8. 如何使用 `unittest` 撰寫 Task 1 與 Task 2 的測試案例？
9. 如何依照 TDD 的 Red → Green → Refactor 流程完成作業？

---

## AI 建議後有採用的部分

本次作業中，我有採用以下 AI 建議：

- 使用 `csv.DictReader()` 讀取 CSV 資料
- 使用 `utf-8-sig` 解決 BOM 編碼問題
- 使用 `json.dump()` 搭配 `indent=2` 輸出 JSON
- 使用 `xml.etree.ElementTree` 建立 XML
- 使用 `@timeit` decorator 量測函式耗時
- 使用 `Path` 建立與管理輸出資料夾
- 使用 `unittest` 建立正常輸入、空輸入與 XML 合法性測試
- 使用 `matplotlib` 與 `seaborn` 製作長條圖
- 使用 `Microsoft JhengHei` 解決圖表中文字顯示問題

---

## AI 建議但未採用的部分

AI 曾建議：

### （1）使用更複雜的 XML 巢狀結構

例如：

```xml
<student>
    <id>1131234001</id>
    <dept>資訊工程系</dept>
</student>
```

但最後沒有採用。

因為題目要求使用：

```xml
<student id="" dept="" school="" zip="" />
```

這種屬性格式，因此仍依照作業規格實作。

---

### （2）將所有功能寫成單一大型函式

AI 一開始曾提供較長的大型函式版本。

但最後沒有採用，因為：

- 可讀性較差
- 不利於 unittest 測試
- 不符合 Refactor 的拆函式要求

因此最後改為：

- `read_csv()`
- `write_json()`
- `filter_by_admission()`
- `count_by_dept()`
- `build_xml_tree()`

等獨立函式。

---

## AI 輸出有誤的案例與修正

本次作業中，AI 曾提供錯誤的 CSV 路徑：

```text
weeks/week-08/in-class/stu-data/113年新生資料庫.csv
```

但實際專案中的 CSV 檔案位置為：

```text
assets/stu-data/113年新生資料庫.csv
```

因此執行 Task 1 時發生：

```text
FileNotFoundError
```

後來重新檢查專案資料夾結構後，修改 `get_csv_path()`，才成功完成 CSV 讀取與 JSON 輸出。

---

## 使用 AI 的心得

透過本次作業，我發現 AI 很適合：

- 查詢 API 用法
- 協助理解資料格式轉換
- 提供 unittest 測試案例
- 協助除錯與分析錯誤原因

但 AI 提供的程式與路徑設定仍需要自行驗證。

如果沒有實際執行與測試，仍然可能出現：

- 路徑錯誤
- 資料格式不符合題目要求
- 圖表中文字顯示問題

因此在使用 AI 協助開發時，仍需要自己理解程式邏輯並進行測試與修正。