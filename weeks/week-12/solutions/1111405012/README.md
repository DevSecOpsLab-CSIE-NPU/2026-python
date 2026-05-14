# Week 12 Solutions - 1111405012

## 完成項目

- `R01-csv-basic.py` / `R01-csv-basic-su.py` / `R01-csv-basic-easy.py`
- `R01-class-basic.py` / `R01-class-basic-su.py` / `R01-class-basic-easy.py`
- `R02-json-basic.py` / `R02-json-basic-su.py` / `R02-json-basic-easy.py`
- `R02-property.py` / `R02-property-su.py` / `R02-property-easy.py`
- `R03-xml-parse.py` / `R03-xml-parse-su.py` / `R03-xml-parse-easy.py`
- `R03-inheritance.py` / `R03-inheritance-su.py` / `R03-inheritance-easy.py`
- `R04-encoding-hex-base64.py` / `R04-encoding-hex-base64-su.py` / `R04-encoding-hex-base64-easy.py`
- `R04-special-methods.py` / `R04-special-methods-su.py` / `R04-special-methods-easy.py`
- `R05-stats-counter.py` / `R05-stats-counter-su.py` / `R05-stats-counter-easy.py`
- `U01-timeit-decorator.py` / `U01-timeit-decorator-su.py` / `U01-timeit-decorator-easy.py`
- 測試資料夾：`tests/`
- 文件：`TEST_CASES.md`、`TEST_LOG.txt`、`AI_USAGE.md`

## 執行方式

- Python 版本：`Python 3.12.2`
- 執行單支程式：
  - `python weeks/week-12/solutions/1111405012/R01-csv-basic.py`
  - `python weeks/week-12/solutions/1111405012/R01-class-basic.py`
  - `python weeks/week-12/solutions/1111405012/R02-json-basic.py`
  - `python weeks/week-12/solutions/1111405012/R02-property.py`
  - `python weeks/week-12/solutions/1111405012/R03-xml-parse.py`
  - `python weeks/week-12/solutions/1111405012/R03-inheritance.py`
  - `python weeks/week-12/solutions/1111405012/R04-encoding-hex-base64.py`
  - `python weeks/week-12/solutions/1111405012/R04-special-methods.py`
  - `python weeks/week-12/solutions/1111405012/R05-stats-counter.py`
  - `python weeks/week-12/solutions/1111405012/U01-timeit-decorator.py`
- 執行測試：
  - `python -m unittest discover -s "weeks/week-12/solutions/1111405012/tests" -p "test_*.py" -v`
- 語法檢查：
  - `python -m compileall "weeks/week-12/solutions/1111405012"`

## 資料結構與作法選擇

- `R01 CSV`：用 `list[list[str]]` 保留 `csv.reader` 的原始列資料，再用 `list[dict]` 對照 `DictReader` 的欄位名稱，方便同時示範兩種讀法。
- `R01 Class`：`Point` 與 `Student` 都直接保留成類別，因為這題重點是實例變數、類別變數與魔術方法，不需要額外包裝成資料表結構。
- `R02 JSON`：直接用 `dict` / `list` 做序列化與反序列化，因為這是 `json` 模組最自然的對應型別。
- `R02 Property`：以 `Circle`、`Rectangle` 類別直接示範封裝規則，讓 getter / setter / 唯讀屬性的責任維持在物件內部。
- `R03 XML`：使用 `ElementTree.Element` 當核心節點結構，再把常用結果整理成 `list[dict[str, str]]`，測試比較直接。
- `R03 Inheritance`：用 `Animal -> Dog/Cat/GuideDog` 的繼承鏈直接呈現覆寫與 `super()`，再用 `list[Animal]` 驗證多型。
- `R04 Encoding`：以 `bytes` 當原始資料型別，Hex 與 Base64 都只負責表達轉換，不混用字串與位元組語意。
- `R04 Special Methods`：`Score` 保留成可比較物件，`Classroom` 保留成可迭代容器，這樣最能直接示範 `__eq__`、`__lt__`、`__len__`、`__contains__`、`__iter__`。
- `R05 Stats`：`Counter` 負責計數，`defaultdict` 負責分組與累加，`namedtuple` 負責可讀欄位，三者分工清楚。
- `U01 Decorator`：把讀取器與計時器拆成獨立函式，讓裝飾器測試與格式效能比較彼此不耦合。

## 遇到的錯誤與修正

- `R02-json-basic.py` 原本在匯入時直接寫 `/tmp/data.json`，在 Windows 環境會觸發 `FileNotFoundError`。後來改成可注入路徑的 `write_json_file()` / `read_json_file()`，示範執行時改用 `TemporaryDirectory()`。
- 第一版測試用 `from tests.support import load_module`，但 `unittest discover` 以 `-s tests` 啟動時不會把 `tests` 當成套件根。後來改成 `from support import load_module`，載入就正常。
- `R02-property.py` 一開始只在 setter 檢查負半徑，但 `__init__` 直接指定 `_radius`，導致 `Circle(-1)` 不會報錯。後來改成初始化直接走 `self.radius = radius`。
- `R03-inheritance.py` 原本 `make_sounds()` 只有 `print()` 沒有回傳值，測試無法驗證多型結果。後來改成回傳字串列表，再由 `main()` 負責印出。
- `R04-special-methods.py` 原本在匯入時就直接建立物件並 `print()`，導致模組不能安靜地被測試載入。後來把所有示範輸出集中到 `main()`。

## Red → Green → Refactor 摘要

- `R01 CSV`
  - Red：測試先要求 `read_csv_rows()`、`read_csv_dict_rows()`、`write_csv_text()`、`write_dict_csv_text()`，但原始腳本只有頂層 `print`，因此全部缺函式。
  - Green：把頂層示範改寫成四個函式，並用 `main()` 保留原本輸出行為。
  - Refactor：抽出 `OUTPUT_FIELDS` 常數，讓 `writer` 與 `DictWriter` 共用欄位定義。

- `R01 Class`
  - Red：先驗證 `Point` 的 `repr` / `str` / 距離計算，以及 `Student.school` 變更後是否影響全部實例。
  - Green：把頂層示範碼收進 `main()`，保留 `Point` 與 `Student` 的核心行為供測試直接建立物件。
  - Refactor：補上型別註記與類別說明，讓示範碼與可測介面分離。

- `R02 JSON`
  - Red：測試要求字串 round-trip 與檔案 I/O，但原始腳本在匯入階段就直接操作 `/tmp/data.json`，導致載入失敗。
  - Green：補上 `to_json_text()`、`from_json_text()`、`write_json_file()`、`read_json_file()`，並把檔案副作用移入 `main()`。
  - Refactor：把 `ensure_ascii`、`indent`、`sort_keys` 做成參數，讓同一組函式可同時支援簡單輸出與漂亮格式化。

- `R02 Property`
  - Red：測試先要求 `Circle(-1)` 在初始化時就丟出 `ValueError`，但原始版本只在 setter 驗證，導致初始負值漏檢。
  - Green：把 `__init__` 改成直接指定 `self.radius = radius`，讓初始化與後續賦值共用同一套規則。
  - Refactor：將 `math` 移到模組層，並加上類別註解，使 `Circle` 與 `Rectangle` 的責任更清楚。

- `R03 XML`
  - Red：測試先要求 `parse_xml()`、`get_channel_title()`、`list_items()`、`list_titles()`，原始檔沒有可重用函式。
  - Green：建立安全取文字的 `get_child_text()`，把 `find` / `findall` / `iter` 行為分成明確函式。
  - Refactor：加入 `get_attribute()`，把屬性預設值處理集中在同一個地方。

- `R03 Inheritance`
  - Red：測試要求 `make_sounds()` 回傳多型結果列表，但原始版本只有列印，回傳值是 `None`。
  - Green：把 `make_sounds()` 改成回傳 `list[str]`，再由 `main()` 負責輸出。
  - Refactor：為 `Animal`、`Dog`、`Cat`、`GuideDog` 與 `make_sounds()` 補上型別註記與簡短說明。

- `R04 Encoding`
  - Red：測試要求 Hex 與 Base64 的往返函式，但原始檔只有一次性示範碼。
  - Green：補出 `bytes_to_hex()`、`hex_to_bytes()`、`encode_base64()`、`decode_base64()`、`encode_urlsafe_base64()`。
  - Refactor：統一讓編碼函式回傳字串、解碼函式回傳 `bytes`，避免介面不一致。

- `R04 Special Methods`
  - Red：測試先要求匯入模組時不得直接輸出，但原始版本一載入就執行示範列印，因此失敗。
  - Green：把建立 `Score` / `Classroom` 與所有 `print()` 全部移入 `main()`，讓模組匯入時只保留類別定義。
  - Refactor：為 `Score`、`Classroom` 與特殊方法補上型別註記與簡短說明，讓行為與教學意圖更清楚。

- `R05 Stats`
  - Red：測試直接要求 Counter、分組、累加、平均的函式，但原始程式只是在頂層組資料後列印。
  - Green：拆成 `count_words()`、`merge_word_counts()`、`group_members_by_dept()`、`sum_scores_by_name()`、`calculate_dept_averages()`。
  - Refactor：將示範資料拉成模組常數，讓測試與示範輸出共用同一份資料。

- `U01 Decorator`
  - Red：測試要求 `build_sample_datasets()` 與 `benchmark_readers()`，原始腳本沒有獨立介面，且一匯入就直接跑完整 benchmark。
  - Green：把資料建立、裝飾器、計時包裝、benchmark 全部拆成函式，並把示範流程搬到 `main()`。
  - Refactor：保留 `naive_timeit()` 做教學對照，正式版本則固定使用 `functools.wraps` 的 `timeit()`。
