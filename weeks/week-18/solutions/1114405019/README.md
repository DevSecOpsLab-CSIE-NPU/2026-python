# 第三題：任意進位的數字根（base=6）

依學號末兩碼 19，個位 9 查對照表得 `base=6`。

## 檔案說明

| 檔案 | 說明 |
| --- | --- |
| `digital_root-easy.py` | AI 教的簡單版本：單一函式 `digital_root_easy`，不拆 helper function，邏輯較好記，附詳細繁體中文註解 |
| `digital_root.py` | 手打版本：拆成 `digit_sum_in_base`（單輪轉進位＋相加）與 `digital_root`（收斂迴圈）兩個函式 |
| `test_digital_root.py` | 針對手打版本的 unittest 測試，涵蓋 0、單輪收斂、雙輪收斂、大數、base=16 等邊界 |
| `test_red.txt` | 實作前跑測試的紀錄（紅燈，`ModuleNotFoundError`） |
| `test_green.txt` | 實作後跑測試的紀錄（綠燈，10 個測試全過） |
| `sample_io.txt` | 手打版本對題目 Sample I/O（輸入 0/8/63）的實際輸出 |
| `sample_io_easy.txt` | 簡單版本對同一組 Sample I/O 的實際輸出（用來確認兩版本結果一致） |
| `AI_LOG.md` | AI 使用紀錄，依 week-18 README 的五步驟記錄實際操作過程與人工確認點 |

## 執行方式

```
echo -e "0\n8\n63" | python digital_root.py
echo -e "0\n8\n63" | python digital_root-easy.py
python -m unittest test_digital_root.py -v
```
