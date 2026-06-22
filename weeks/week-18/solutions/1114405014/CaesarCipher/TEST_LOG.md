# TEST_LOG.md

## 測試環境

```text
OS: Windows
Python: 3.14.3
pytest: 9.0.3
測試目錄: weeks/week-18/solutions/1114405014/CaesarCipher
```

## 第一次測試紀錄

### 執行指令

```bash
pytest
```

### 結果

```text
collected 0 items / 1 error

ImportError while importing test module 'test_caesar_cipher.py'
ModuleNotFoundError: No module named 'caesar_cipher'
```

### 問題原因

測試檔 `test_caesar_cipher.py` 使用：

```python
from caesar_cipher import caesar_cipher, process_text
```

但當時測試環境無法找到 `caesar_cipher.py`，因此發生匯入錯誤。

### 修正方式

確認主程式檔案名稱為 `caesar_cipher.py`，並將主程式與測試檔放在同一個資料夾，讓 pytest 可以正確匯入。

## 第二次測試紀錄

### 執行指令

```bash
pytest
```

### 結果

```text
collected 10 items

test_caesar_cipher.py .......... [100%]

10 passed in 0.05s
```

## 本次重新驗證

### 執行指令

```bash
pytest -q test_caesar_cipher.py
```

### 結果

```text
..........                                                               [100%]
10 passed in 0.11s
```

## 測試案例整理

| 測試名稱 | 測試目的 | 預期結果 |
|---|---|---|
| `test_uppercase_letters_shift` | 測試大寫字母位移 | `ABC -> DEF` |
| `test_lowercase_letters_shift` | 測試小寫字母位移 | `abc -> def` |
| `test_preserve_non_letters` | 測試非英文字元保留 | 數字與標點不變 |
| `test_uppercase_wrap_around` | 測試大寫循環 | `XYZ -> ABC` |
| `test_lowercase_wrap_around` | 測試小寫循環 | `xyz -> abc` |
| `test_empty_string` | 測試空字串 | 回傳空字串 |
| `test_shift_one` | 測試 shift = 1 | `Az az -> Ba ba` |
| `test_shift_ten` | 測試 shift = 10 | `ABC xyz -> KLM hij` |
| `test_process_multiple_lines_until_eof` | 測試多行輸入 | 每行正確加密並保留換行 |
| `test_process_keeps_blank_lines` | 測試空行保留 | 空行不被刪除 |

## 結論

第二題 Caesar Cipher 的主程式與測試檔已通過測試。測試涵蓋大小寫位移、循環、非英文字元保留、空字串、多行 EOF 與空行保留等題目要求。
