# 11417 測試紀錄

## 測試指令

```powershell
"C:/Users/user/AppData/Local/Python/pythoncore-3.14-64/python.exe" -m unittest test_11417 -v
```

## 測試結果

```text
test_medium_limit (test_11417.Test11417.test_medium_limit)
再確認一個較小的中間值，避免索引錯誤。 ... ok
test_sample_input (test_11417.Test11417.test_sample_input)
題目範例輸入要回傳對應的三筆答案。 ... ok
test_small_limit (test_11417.Test11417.test_small_limit)
N = 2 時只有一組 (1, 2)，gcd 會是 1。 ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.017s

OK
```
