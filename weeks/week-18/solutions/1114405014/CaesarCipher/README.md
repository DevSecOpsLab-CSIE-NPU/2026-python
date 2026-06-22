# Caesar Cipher

## 題目說明

本專案為期末上機考第二題：凱撒密碼（Caesar Cipher）。程式會讀取多行文字直到 EOF，將每一行中的英文字母依照指定的 `SHIFT` 位移加密，並輸出加密後的結果。

## 位移參數

題目規定 `SHIFT` 依照學號最後一碼 `u` 決定：

```text
SHIFT = u % 25 + 1
```

本次學號末碼為 `4`，所以：

```text
SHIFT = 4 % 25 + 1 = 5
```

## 加密規則

1. 大寫英文字母 `A-Z` 在大寫範圍內循環位移。
2. 小寫英文字母 `a-z` 在小寫範圍內循環位移。
3. 非英文字母，例如空白、數字、標點符號，全部原樣保留。
4. 支援多行輸入，直到 EOF 結束。

## 檔案結構

```text
caesar_cipher.py       # 主程式
test_caesar_cipher.py  # unittest 測試檔
README.md              # 專案說明
PR.md                  # PR 說明
AI_LOG.md              # AI 協作紀錄
TEST_LOG.md            # 測試紀錄
```

## 核心函式

### `caesar_cipher(text: str, shift: int) -> str`

處理單一字串，將其中的英文字母依照 `shift` 位移。

### `process_text(input_text: str, shift: int) -> str`

處理多行輸入，保留換行與空行，逐行套用凱撒密碼。

### `main() -> None`

從標準輸入讀取全部內容直到 EOF，使用本題設定的 `SHIFT` 輸出加密結果。

## 使用方式

執行主程式：

```bash
python caesar_cipher.py
```

輸入範例：

```text
Hello, NPU!
abc XYZ
```

若本題 `SHIFT = 5`，輸出為：

```text
Mjqqt, SUZ!
fgh CDE
```

### EOF 輸入方式

Windows PowerShell：

```text
Ctrl + Z
Enter
```

Linux / macOS / Git Bash：

```text
Ctrl + D
```

## 測試方式

使用 pytest：

```bash
pytest
```

或指定測試檔：

```bash
pytest -q test_caesar_cipher.py
```

目前測試結果：

```text
10 passed
```

## 測試涵蓋內容

- 大寫英文字母位移
- 小寫英文字母位移
- 大寫循環，例如 `XYZ -> ABC`
- 小寫循環，例如 `xyz -> abc`
- 非英文字元保留
- 空字串處理
- shift = 1
- shift = 10
- 多行輸入直到 EOF
- 空行保留
