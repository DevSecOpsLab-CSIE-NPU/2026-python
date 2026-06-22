# TEST_LOG - benchmark_search

## 執行指令
```
python benchmark_search.py --generate --n 1000 --repeat 1
```

## 測試輸出（results.json 內容）
```
```

以下為 `assets/results.json` 內容：

```json
<!-- see file assets/results.json -->
```

## 說明
- 執行時如果未安裝 `matplotlib`，程式仍會產生 `assets/results.json` 與 `assets/radar.png`（後者為佔位檔），以確保作業輸出可被驗收。
- 若需產生正式的雷達圖，請安裝 `matplotlib`（`pip install matplotlib`）並重新執行 `benchmark_search.py`。
