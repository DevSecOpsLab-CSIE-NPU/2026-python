# TEST_LOG

日期：2026-05-27
環境：`.venv` Python 3.14.2

## 全量測試

執行方式（逐檔）：

```powershell
$tests = Get-ChildItem -Path "weeks/week-14/solutions/1114405011-0527" -Recurse -Filter "test_*.py" | Sort-Object FullName
foreach ($t in $tests) {
	d:/2026-python/.venv/Scripts/python.exe $t.FullName -v
}
```

結果：所有測試皆 `OK`。

## 手打程式測試紀錄（集中）

### 11349 / test_q11349_hand_typed.py

```text
test_hand_typed (__main__.Test11349HandTyped.test_hand_typed) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.254s

OK
```

### 11417 / test_q11417_hand_typed.py

```text
test_hand (__main__.Test11417HandTyped.test_hand) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.225s

OK
```

### 11461 / test_q11461_hand_typed.py

```text
test_hand (__main__.Test11461HandTyped.test_hand) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.244s

OK
```

### 12019 / test_q12019_hand_typed.py

```text
test_hand (__main__.Test12019HandTyped.test_hand) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.214s

OK
```
