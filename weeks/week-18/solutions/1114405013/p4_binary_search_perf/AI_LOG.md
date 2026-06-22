# AI_LOG

## 開工前資訊檢查表

### ① 函式簽名

本題不是只寫函式，而是整支程式讀 stdin、印 stdout。  
主要程式檔為 `main.py`。  
程式從標準輸入讀入一組已升冪排序的整數陣列，搜尋固定目標 K = 113，並輸出搜尋結果、比較次數與效能比較結果。

### ② 輸入邊界

第 1 行輸入整數 n。  
第 2 行輸入 n 個已升冪排序的整數。  
陣列可能包含 K，也可能不包含 K。  
陣列大小會影響 linear search 與 binary search 的效能差距。  
我的學號末兩碼是 13，所以 K = 100 + 13 = 113。

### ③ 例外處理

題目主要處理合法輸入。  
若 K 不在陣列中，輸出 `NOT FOUND cmp=次數`。  
若 K 在陣列中，輸出 `FOUND idx cmp=次數`。  
若輸入為空或格式不足，程式不額外擴充題目沒有要求的非法格式處理。

### ④ edge case

我設計 K 不存在於陣列中的情況作為 edge case。  
例如輸入陣列 `1 20 37 80 150`，其中沒有 113，所以預期輸出第一行包含 `NOT FOUND cmp=`。

我也測試 K 存在於陣列中的情況。  
例如輸入陣列 `1 20 37 80 113 150 200 300`，其中 113 存在，所以預期輸出第一行包含 `FOUND idx cmp=`。

### ⑤ 驗收標準

程式必須用 binary search 搜尋 K = 113。  
第一行要輸出 `FOUND idx cmp=次數` 或 `NOT FOUND cmp=次數`。  
程式必須用 timeit 輸出 linear search 與 binary search 的時間。  
程式必須輸出哪個方法比較快。  
程式必須產生 `assets/radar.png`。  
程式必須產生 `README.md`，說明雷達圖維度、正規化方式與比較結果。  
我會用 `python -m unittest -v test_search_perf.py` 驗證。  
測試必須先紅燈，再完成 `main.py` 實作後變綠燈。

---


## 我問了 AI 什麼

1. 我請 AI 根據第四題「二分搜尋效能」題目，先建立 unittest 測試檔 `test_search_perf.py`。
2. 我告訴 AI 這題是整支程式讀 stdin、印 stdout，並且要另外產生 `assets/radar.png` 和 `README.md`。
3. 我提供我的學號末兩碼是 13，所以搜尋目標 `K = 100 + 13 = 113`。
4. 我要求測試至少包含 3 個 test case：
   - FOUND 案例：陣列包含 113。
   - NOT FOUND edge case：陣列不包含 113。
   - 檔案產生案例：確認會產生 `assets/radar.png` 和 `README.md`。
5. 我要求先不要建立 `main.py`，先確認 red test。
6. 我確認 red test 失敗，原因是尚未建立 `main.py`。
7. 我完成 `test:` commit 後，請 AI 建立 `main.py`、`README.md`，並讓程式執行時產生 `assets/radar.png`。
8. 我要求 AI 使用 `matplotlib.use("Agg")`，避免無視窗環境出錯。
9. 我執行測試後發現錯誤：`ModuleNotFoundError: No module named 'matplotlib'`，再請 AI 協助修正。

## AI 給了我什麼

1. AI 幫我建立 unittest 測試檔：

   `test_search_perf.py`

2. AI 設計了 3 個測試案例：
   - FOUND：確認第一行包含 `FOUND`、`idx`、`cmp=`
   - NOT FOUND edge case：確認第一行包含 `NOT FOUND` 和 `cmp=`
   - 檔案產生：確認執行後會產生 `assets/radar.png` 和 `README.md`

3. AI 說明如何執行測試：

   `python -m unittest -v test_search_perf.py`

4. AI 確認尚未建立 `main.py` 時，測試會紅燈失敗。
5. 在我完成 red test commit 後，AI 幫我建立：
   - `main.py`
   - `README.md`
   - `assets/radar.png`

6. AI 在 `main.py` 中實作：
   - linear search
   - binary search
   - binary search 的 `FOUND / NOT FOUND` 與 `cmp` 輸出
   - `timeit` 比較 linear 與 binary 的執行時間
   - 雷達圖產生
   - README 產生

7. AI 幫我補上 `matplotlib` 不存在時的 fallback，避免測試環境沒有安裝 matplotlib 時程式直接失敗。

## 我改了什麼

1. 我建立第四題資料夾：

   `weeks/week-18/solutions/1114405013/p4_binary_search_perf/`

2. 我使用 AI 產生的測試檔：

   `test_search_perf.py`

3. 我先執行 unittest，確認因為沒有 `main.py`，所以測試是 red test。
4. 我完成 commit：

   `test: add failing tests for binary search performance`

5. 我請 AI 建立正式實作檔案：

   `main.py`

6. 我請 AI 建立說明文件：

   `README.md`

7. 我讓程式執行時產生：

   `assets/radar.png`

8. 我執行測試時發現本機環境缺少 `matplotlib`，並把錯誤截圖提供給 AI。
9. AI 修正後，我再次執行 unittest，確認測試通過。
10. 我保留 `test_search_perf.py` 不修改，只修改/新增正式實作與輸出檔案。
