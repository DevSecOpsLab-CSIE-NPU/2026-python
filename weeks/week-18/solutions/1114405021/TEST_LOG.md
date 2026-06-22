# TEST LOG

## 任務 1：數列去重過濾排序（Week 18 期末作業）

### Red Phase（尚未實作 main.py）

執行指令：
```
python -m unittest test_main -v
```

結果：
```
ModuleNotFoundError: No module named 'main'
```
測試總數：5  通過：0  失敗：5

修正方式：撰寫 `main.py` 實作 `process_sequence()` 與 `main()`。

### Green Phase（全部通過）

執行指令：
```
python -m unittest test_main -v
```

測試總數：5  通過：5  失敗：0

---

## 任務 2：Caesar Cipher 字元移位加密（SHIFT=2）

### Red Phase（尚未實作 caesar.py）

執行指令：
```
python -m unittest test_caesar -v
```

結果：
```
ModuleNotFoundError: No module named 'caesar'
```
測試總數：8  通過：0  失敗：8

修正方式：撰寫 `caesar.py` 實作 `shift_char()`、`encrypt_line()`、`main()`。

### Green Phase（全部通過）

執行指令：
```
python -m unittest test_caesar -v
```

結果：
```
test_basic_lowercase ... ok
test_basic_uppercase ... ok
test_empty_line ... ok
test_full_sample ... ok
test_mixed_case ... ok
test_multiple_lines ... ok
test_non_letters_unchanged ... ok
test_wrap_around ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

測試總數：8  通過：8  失敗：0
