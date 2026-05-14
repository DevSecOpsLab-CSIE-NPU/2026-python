# Week 13 Solutions - 1111405012

## 完成項目

- `R01-csv-basic.py` / `R01-csv-basic-su.py` / `R01-csv-basic-easy.py`
- `R02-json-basic.py` / `R02-json-basic-su.py` / `R02-json-basic-easy.py`
- `R03-xml-parse.py` / `R03-xml-parse-su.py` / `R03-xml-parse-easy.py`
- `R04-encoding-hex-base64.py` / `R04-encoding-hex-base64-su.py` / `R04-encoding-hex-base64-easy.py`
- `R05-stats-counter.py` / `R05-stats-counter-su.py` / `R05-stats-counter-easy.py`
- `U01-timeit-decorator.py` / `U01-timeit-decorator-su.py` / `U01-timeit-decorator-easy.py`
- 測試資料夾：`tests/`
- 文件：`TEST_CASES.md`、`TEST_LOG.txt`、`AI_USAGE.md`

## 執行方式

- Python 版本：`Python 3.12.2`
- 執行單支程式：
  - `python weeks/week-13/solutions/1111405012/R01-csv-basic.py`
  - `python weeks/week-13/solutions/1111405012/R02-json-basic.py`
  - `python weeks/week-13/solutions/1111405012/R03-xml-parse.py`
  - `python weeks/week-13/solutions/1111405012/R04-encoding-hex-base64.py`
  - `python weeks/week-13/solutions/1111405012/R05-stats-counter.py`
  - `python weeks/week-13/solutions/1111405012/U01-timeit-decorator.py`
- 執行測試：
  - `python -m unittest discover -s "weeks/week-13/solutions/1111405012/tests" -p "test_*.py" -v`
- 語法檢查：
  - `python -m compileall "weeks/week-13/solutions/1111405012"`

## 資料結構與作法選擇

- `R01 CSV`：用 `list[list[str]]` 保留 `csv.reader` 的原始列資料，再用 `list[dict]` 對照 `DictReader` 的欄位名稱，方便同時示範兩種讀法。
- `R02 JSON`：直接用 `dict` / `list` 做序列化與反序列化，因為這是 `json` 模組最自然的對應型別。
- `R03 XML`：使用 `ElementTree.Element` 當核心節點結構，再把常用結果整理成 `list[dict[str, str]]`，測試比較直接。
- `R04 Encoding`：以 `bytes` 當原始資料型別，Hex 與 Base64 都只負責表達轉換，不混用字串與位元組語意。
- `R05 Stats`：`Counter` 負責計數，`defaultdict` 負責分組與累加，`namedtuple` 負責可讀欄位，三者分工清楚。
- `U01 Decorator`：把讀取器與計時器拆成獨立函式，讓裝飾器測試與格式效能比較彼此不耦合。

## 遇到的錯誤與修正

- `R02-json-basic.py` 原本在匯入時直接寫 `/tmp/data.json`，在 Windows 環境會觸發 `FileNotFoundError`。後來改成可注入路徑的 `write_json_file()` / `read_json_file()`，示範執行時改用 `TemporaryDirectory()`。
- 第一版測試用 `from tests.support import load_module`，但 `unittest discover` 以 `-s tests` 啟動時不會把 `tests` 當成套件根。後來改成 `from support import load_module`，載入就正常。

## Red → Green → Refactor 摘要

- `R01 CSV`
  - Red：測試先要求 `read_csv_rows()`、`read_csv_dict_rows()`、`write_csv_text()`、`write_dict_csv_text()`，但原始腳本只有頂層 `print`，因此全部缺函式。
  - Green：把頂層示範改寫成四個函式，並用 `main()` 保留原本輸出行為。
  - Refactor：抽出 `OUTPUT_FIELDS` 常數，讓 `writer` 與 `DictWriter` 共用欄位定義。

- `R02 JSON`
  - Red：測試要求字串 round-trip 與檔案 I/O，但原始腳本在匯入階段就直接操作 `/tmp/data.json`，導致載入失敗。
  - Green：補上 `to_json_text()`、`from_json_text()`、`write_json_file()`、`read_json_file()`，並把檔案副作用移入 `main()`。
  - Refactor：把 `ensure_ascii`、`indent`、`sort_keys` 做成參數，讓同一組函式可同時支援簡單輸出與漂亮格式化。

- `R03 XML`
  - Red：測試先要求 `parse_xml()`、`get_channel_title()`、`list_items()`、`list_titles()`，原始檔沒有可重用函式。
  - Green：建立安全取文字的 `get_child_text()`，把 `find` / `findall` / `iter` 行為分成明確函式。
  - Refactor：加入 `get_attribute()`，把屬性預設值處理集中在同一個地方。

- `R04 Encoding`
  - Red：測試要求 Hex 與 Base64 的往返函式，但原始檔只有一次性示範碼。
  - Green：補出 `bytes_to_hex()`、`hex_to_bytes()`、`encode_base64()`、`decode_base64()`、`encode_urlsafe_base64()`。
  - Refactor：統一讓編碼函式回傳字串、解碼函式回傳 `bytes`，避免介面不一致。

- `R05 Stats`
  - Red：測試直接要求 Counter、分組、累加、平均的函式，但原始程式只是在頂層組資料後列印。
  - Green：拆成 `count_words()`、`merge_word_counts()`、`group_members_by_dept()`、`sum_scores_by_name()`、`calculate_dept_averages()`。
  - Refactor：將示範資料拉成模組常數，讓測試與示範輸出共用同一份資料。

- `U01 Decorator`
  - Red：測試要求 `build_sample_datasets()` 與 `benchmark_readers()`，原始腳本沒有獨立介面，且一匯入就直接跑完整 benchmark。
  - Green：把資料建立、裝飾器、計時包裝、benchmark 全部拆成函式，並把示範流程搬到 `main()`。
  - Refactor：保留 `naive_timeit()` 做教學對照，正式版本則固定使用 `functools.wraps` 的 `timeit()`。
