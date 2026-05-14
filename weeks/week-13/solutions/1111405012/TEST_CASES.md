# TEST CASES

## Case 1：R01 CSV 正常讀取

- 輸入：`RAW_CSV` 範例字串，共 1 行標頭 + 3 行資料
- 預期輸出：標頭為 `["Symbol", "Price", "Date", "Time", "Change", "Volume"]`，第一列資料為 `["AA", "39.48", "6/11/2007", "9:36am", "-0.18", "181800"]`
- 實際輸出：與預期一致
- 是否通過：`PASS`
- 對應測試：`tests/test_r01_csv_basic.py::test_reader_can_split_header_and_rows`
- 關鍵修改點：把頂層 `csv.reader` 示範抽成 `read_csv_rows()`

## Case 2：R02 中文 JSON 與跳脫字元

- 輸入：`{"城市": "澎湖"}`
- 預期輸出：`ensure_ascii=True` 時包含 `\u57ce\u5e02`，`ensure_ascii=False` 時保留 `澎湖`
- 實際輸出：`escaped` 內含 Unicode escape，`utf8_text` 直接顯示中文
- 是否通過：`PASS`
- 對應測試：`tests/test_r02_json_basic.py::test_ensure_ascii_switches_chinese_output`
- 關鍵修改點：把 `json.dumps()` 的 `ensure_ascii` 變成可控制參數

## Case 3：R03 XML 缺少屬性時的預設值

- 輸入：`<rss version="2.0">...</rss>`，查詢不存在的 `missing` 屬性並給預設值 `預設值`
- 預期輸出：回傳 `預設值`
- 實際輸出：`預設值`
- 是否通過：`PASS`
- 對應測試：`tests/test_r03_xml_parse.py::test_iter_titles_and_missing_default`
- 關鍵修改點：加入 `get_attribute(element, name, default)` 統一處理預設值

## Case 4：R04 URL-safe Base64 反例

- 輸入：位元組資料 `b"\xfb\xef\xff"`
- 預期輸出：編碼後結果不包含 `+` 與 `/`，且解碼可回到原始資料
- 實際輸出：不含 `+`、`/`，解碼後等於原輸入
- 是否通過：`PASS`
- 對應測試：`tests/test_r04_encoding_hex_base64.py::test_urlsafe_base64_avoids_plus_and_slash`
- 關鍵修改點：把解碼統一交給可處理 URL-safe 字元的 `decode_base64()`

## Case 5：R05 分數累加與平均

- 輸入：`SCORES = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]` 與 `DEPT_SCORE_ROWS`
- 預期輸出：個人總分為 `{"Alice": 175, "Bob": 150}`，各系平均為 `{"系資": 88.5, "電子": 83.0}`
- 實際輸出：與預期一致
- 是否通過：`PASS`
- 對應測試：
  - `tests/test_r05_stats_counter.py::test_sum_scores_by_name`
  - `tests/test_r05_stats_counter.py::test_calculate_department_averages`
- 關鍵修改點：把 `defaultdict(int)` 與 `defaultdict(list)` 各自封裝成獨立函式

## Case 6：U01 三種格式讀取一致性

- 輸入：`build_sample_datasets(3)`
- 預期輸出：`read_csv_raw()`、`read_json_raw()`、`read_xml_raw()` 都應回傳 3 筆資料
- 實際輸出：三者長度皆為 3
- 是否通過：`PASS`
- 對應測試：`tests/test_u01_timeit_decorator.py::test_readers_parse_same_number_of_rows`
- 關鍵修改點：把資料生成流程抽成 `build_sample_datasets()`，避免 benchmark 與測試各寫一套

## Case 7：R01 Class 距離與類別變數

- 輸入：`Point(0, 0)`、`Point(3, 4)`，以及兩個 `Student` 實例
- 預期輸出：兩點距離為 `5.0`；把 `Student.school` 改成 `NPU` 後，兩個實例都看到新值
- 實際輸出：距離為 `5.0`，兩個實例的 `school` 都更新為 `NPU`
- 是否通過：`PASS`
- 對應測試：
  - `tests/test_r01_class_basic.py::test_point_repr_str_and_distance`
  - `tests/test_r01_class_basic.py::test_updating_school_affects_all_instances`
- 關鍵修改點：把頂層示範移入 `main()`，讓類別可直接被測試建立與驗證

## Case 8：R02 Property 負半徑反例

- 輸入：`Circle(-1)` 與 `circle.radius = -2`
- 預期輸出：兩者都應拋出 `ValueError("半徑不能為負數")`
- 實際輸出：初始化與 setter 都正確拋出 `ValueError`
- 是否通過：`PASS`
- 對應測試：`tests/test_r02_property.py::test_circle_rejects_negative_radius_in_init_and_setter`
- 關鍵修改點：把 `Circle.__init__` 從直接指定 `_radius` 改成走 `self.radius = radius`

## Case 9：R03 Inheritance 多型回傳結果

- 輸入：`[Dog("小黑"), Cat("咪咪"), GuideDog("阿金", "王伯伯")]`
- 預期輸出：`make_sounds()` 回傳三筆叫聲字串列表
- 實際輸出：`["小黑 說：汪汪！", "咪咪 說：喵～", "阿金 說：汪汪！（導盲犬，主人：王伯伯）"]`
- 是否通過：`PASS`
- 對應測試：`tests/test_r03_inheritance.py::test_make_sounds_collects_polymorphic_results`
- 關鍵修改點：把 `make_sounds()` 從純 `print()` 改成回傳列表，再由 `main()` 做輸出

## Case 10：R04 Special Methods 匯入不可有副作用

- 輸入：載入 `R04-special-methods.py`
- 預期輸出：匯入時標準輸出應為空字串，類別定義可正常建立測試物件
- 實際輸出：重構後匯入時無輸出，`Score` 與 `Classroom` 可直接使用
- 是否通過：`PASS`
- 對應測試：`tests/test_r04_special_methods.py::test_import_has_no_side_effect_output`
- 關鍵修改點：把頂層示範碼全部移入 `main()`

## Case 11：R04 Special Methods 比較與容器行為

- 輸入：`Score("Alice", 90)`、`Score("Bob", 75)`、`Score("Carol", 90)`，以及加入 `Alice`、`Bob`、`Carol` 的 `Classroom("資工一甲")`
- 預期輸出：`sorted(scores)` 依分數升冪排列；`len(classroom)` 為 `3`；`"Alice" in classroom` 為 `True`；可迭代出 `["Alice", "Bob", "Carol"]`
- 實際輸出：與預期一致
- 是否通過：`PASS`
- 對應測試：
  - `tests/test_r04_special_methods.py::test_score_supports_ordering_and_repr`
  - `tests/test_r04_special_methods.py::test_classroom_supports_len_contains_iter_and_repr`
- 關鍵修改點：保留 `Score` 的比較特殊方法與 `Classroom` 的容器特殊方法，並避免匯入時執行示範碼
