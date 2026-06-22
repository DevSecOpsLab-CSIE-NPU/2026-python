# TEST_LOG.md — Data Cleaning（D=3）

## Red（尚未通過）

執行指令：
```
python -m pytest tests/ -v
```

結果摘要：
- 總數：10（collection 階段即失敗，0 個能執行）
- 通過：0
- 失敗：2 個 collection error
- 原因：`data_cleaning.py` 尚不存在，`from data_cleaning import clean_sequence, format_result` / `from data_cleaning import main` 皆 `ModuleNotFoundError`。

## Green（全部通過）

執行指令：
```
python -m pytest tests/ -v
```

結果摘要：
- 總數：10
- 通過：10
- 失敗：0
- 從紅燈到綠燈的修改：新增 `data_cleaning.py`，實作 `clean_sequence`（去重保序 → 篩選整除 → 排序）、`format_result`（空 list 轉 `"NONE"`）、`main`（用 `while True` 配合 `sys.stdin.readline()` 讀到 `n=0` 才結束，每組讀完立即輸出，不等 EOF）。

## 手動 stdin 驗證（補充，非 pytest）

執行指令與輸出：
```
$ printf '8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n' | python data_cleaning.py
6 9
3

$ printf '0\n' | python data_cleaning.py
(無輸出)

$ printf '4\n1 2 4 5\n0\n' | python data_cleaning.py
NONE

$ printf '3\n-9 -3 2\n0\n' | python data_cleaning.py
-9 -3
```

全部符合預期，包含用 `cat -A` 檢查過輸出沒有多餘空行（Windows 環境下行尾為 `\r\n` 屬於文字模式正常行為，不是程式錯誤）。
