
# AI_LOG — 0617 timeit + 搜尋評估
 
## 我用的提示詞(逐字)
1.「依 0617-search-eval.md 的規格,用 TDD 幫我把 timeit 裝飾器做出來:先補齊
   test_timing.py 跑紅燈、commit test:,再寫 timing.py 跑綠燈、commit feat:。」
2.「再寫 search.py 的 linear_search / binary_search(不可改傳入 data),配上測試。」
3.「用 timeit 量 linear vs binary,把數據和我的直覺判斷寫進 README。」
 
## 我改了什麼
- 補齊 `test_timing.py` 六個測試(規格 1~5 全覆蓋 + repeat=1 / 預設跑 3 次兩個 edge case)。
- 新寫 `timing.py`:`timeit` 支援 `@timeit` 與 `@timeit(repeat=n)` 兩種寫法;
  `records` / `last_elapsed` 掛在 wrapper 上;`repeat < 1` 用 `raise ValueError`(非 assert);
  裝飾器內無 `print`;`functools.wraps` 保留 metadata。
- 新寫 `search.py` + `test_search.py`(linear/binary 各 5 筆,含「不修改 data」測試)。
- 新寫 `benchmark.py` 量測,結果寫進 `README.md` 評估段。
 
## AI 反問我什麼 / 我怎麼回答
> 逐項記下 AI 問的規格問題與我的決定。
 
- Q:`repeat` 取**平均**還是取**最小**?
  A:取平均,要反映一般情況(最小值會偏樂觀,藏住雜訊)。
- Q:`records` 是每次呼叫**清空重來**,還是**跨呼叫累積**?
  A:累積。`records` 留所有歷史;`last_elapsed` 只反映「本次 repeat」的平均
  (用 `records[-repeat:]` 取本次那幾筆)。
- Q:`timeit` 要支援裸用 `@timeit` 嗎,還是一律 `@timeit(repeat=n)`?
  A:兩種都要支援,所以 `func=None` 時回傳 decorator。
- Q:`binary_search` 收到**未排序** data 怎麼辦?要排序、報錯還是回未定義?
  A:不偷偷排序、不報錯;在 docstring 寫明「前提是已排序,未排序回傳未定義」,
  呼叫端負責。理由:偷偷排序會改/複製資料,還把 O(log n) 變成 O(n log n)。
- Q:輸入驗證為什麼不能用 `assert`?
  A:`assert` 在 `python -O` 最佳化模式會被移除,驗證會失效;安全檢查要用 `raise`。
- Q:評估的 `n` 要多大、`target` 放哪?
  A:`n = 2,000,000`、`target` 放最尾端(linear 最壞情況),差距才看得出來。
 
## 我怎麼驗收 AI 給的東西(驗收標準)
- 測試齊不齊:規格 1~5 每條都至少一個測試,另加 repeat=1 / 預設跑 3 次 edge case。
- TDD 順序:先確認 `test:` commit 當下是紅(ImportError),寫完才綠。
- 搜尋對不對:linear/binary 回傳同一個 index;兩者跑完 data 內容不變(快照比對)。
- 評估有沒有數據:README 的判斷必須對得上 benchmark.py 實測數字。
 
## 自我檢測(不翻文件)
1. `last_elapsed` / `records` 掛 wrapper 上 → 每個被裝飾函式各自獨立紀錄,免全域狀態污染。
2. 驗證用 `raise` 不用 `assert` → `assert` 在 -O 模式被拿掉,檢查會消失。
3. binary 比 linear 快是因為每步砍半 O(log n),前提是 data 已排序。
4. 只搜尋少數幾次時「排序 + binary」反而比 linear 慢,因為排序的 O(n log n) 攤不回來。