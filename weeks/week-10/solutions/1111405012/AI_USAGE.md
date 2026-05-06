# Week 10 AI 使用紀錄

## 詢問 AI 的問題

- 如何依 Week 10 HOMEWORK 的提交結構安排 Task 1、Task 2、Task 3。
- CSV 使用 `utf-8-sig` 讀取時，如何保留中文欄位名稱並轉成 JSON。
- JSON 轉 XML 時，學生資料應該放成子節點文字還是 XML attributes。
- `@timeit` 裝飾器如何保留原函式名稱，避免測試與除錯時看到 `wrapper`。
- 當本機沒有 `matplotlib` 時，Task 3 是否需要 fallback 方案產生圖檔。
- 更新 CSV 資料路徑 `assets/stu-data/113年新生資料庫.csv`，避免沿用 HOMEWORK 舊路徑。
- 加分版圖表如何使用 `seaborn` 並確保中文字不亂碼。

## 採用的建議

- 採用 `csv.DictReader`，讓每一列直接變成 dict，方便用中文欄位過濾與投影。
- 採用 `Counter` 統計各系所人數，避免手動維護巢狀判斷。
- 採用 `xml.etree.ElementTree` 建立 XML，避免用字串拼接 XML 造成跳脫字元問題。
- 使用 `functools.wraps` 實作 `@timeit`，讓裝飾後函式保留原本名稱。
- 測試先聚焦核心函式，不直接依賴完整真實 CSV，讓測試資料小而穩定。

## 未採用的建議

- 未採用「直接用 set 或 dict comprehension 去重建所有資料欄位」的做法，因為本題只要求輸出指定欄位，保留全部欄位會讓 JSON 輸出不符合格式。
- 未採用「把 XML 每個欄位做成巢狀元素」的做法，因為 HOMEWORK 指定格式是 `<student id="..." dept="..." school="..." zip="..."/>`。
- 未採用「只支援 matplotlib，缺套件就停止」的做法，因為目前環境未安裝 `matplotlib`，仍需要產生 `timing_comparison.png`。
- 未採用下載 `fonts-noto-cjk` 的做法，因為該字型套件涉及授權條款確認；改成只使用系統已安裝字型。

## AI 建議不完整與修正

一開始 HOMEWORK 內的 CSV 路徑是舊資料；實際資料位於：

```text
assets/stu-data/113年新生資料庫.csv
```

修正方式是在 `task1_csv_to_json.py` 中直接設定 `CSV_PATH = REPO_ROOT / "assets/stu-data/113年新生資料庫.csv"`，讓程式固定使用新版資料來源。

另外，Task 3 fallback PNG 產生器第一次執行時把 PNG chunk type 傳成字串，造成：

```text
TypeError: can't concat str to bytes
```

修正方式是將 `IHDR`、`IDAT`、`IEND` 改為 bytes，例如 `b"IHDR"`。

## 加分版處理

依需求新增三個 `_bonus` 版程式：

- `task1_csv_to_json_bonus.py`：增加加分摘要、系所排名、全部入學方式統計。
- `task2_json_to_xml_bonus.py`：增加摘要 XML 節點與系所排名 XML 節點。
- `task3_plot_comparison_bonus.py`：使用 `seaborn`、中文標題與座標軸、漸層效果、X 軸右旋轉 90 度、圖上笑臉、摘要註解與結論。

中文字型策略：

- Windows：優先使用系統字型 `Microsoft JhengHei`。
- Linux：自動尋找系統已安裝的 WenQuanYi、AR PL、Source Han、LXGW 等 CJK 字型，也會檢查其他支援中文字的系統字型。
- 若找不到可顯示中文的系統字型，程式會停止輸出，避免產生中文方塊或亂碼圖。
