# Test Log - 平方數計數 (count_squares)

## 測試執行結果

### 初始（紅燈）
```
$ python -m pytest test_square_counter.py -v

test_square_counter.py::TestCountSquares::test_basic_range FAILED        [ 20%]
test_square_counter.py::TestCountSquares::test_invalid_input_raises_value_error PASSED [ 40%]
test_square_counter.py::TestCountSquares::test_no_squares_in_range PASSED [ 60%]
test_square_counter.py::TestCountSquares::test_single_large_perfect_square FAILED [ 80%]
test_square_counter.py::TestCountSquares::test_single_point_is_square FAILED [100%]

================================== FAILURES ===================================
________________________ TestCountSquares.test_basic_range ________________________

    def test_basic_range(self):
        """基本案例：count_squares(1, 10) 應為 3 (1, 4, 9)"""
>       self.assertEqual(count_squares(1, 10), 3)
E       AssertionError: 0 != 3

test_square_counter.py:20: AssertionError
________________________ TestCountSquares.test_single_large_perfect_square ________________________

    def test_single_large_perfect_square(self):
        """Edge case：大數字的完全平方數"""
>       self.assertEqual(count_squares(100, 100), 1)
E       AssertionError: 0 != 1

test_square_counter.py:32: AssertionError
________________________ TestCountSquares.test_single_point_is_square ________________________

    def test_single_point_is_square(self):
        """Edge case：單點區間，1 本身就是完全平方數"""
>       self.assertEqual(count_squares(1, 1), 1)
E       AssertionError: 0 != 1

test_square_counter.py:24: AssertionError
=========================== 3 failed, 2 passed in 0.08s =========================
```

**結果：3 個失敗，2 個通過 ✓ 紅燈確認**

---

### 最終（綠燈）
```
$ python -m pytest test_square_counter.py -v

test_square_counter.py::TestCountSquares::test_basic_range PASSED        [ 20%]
test_square_counter.py::TestCountSquares::test_invalid_input_raises_value_error PASSED [ 40%]
test_square_counter.py::TestCountSquares::test_no_squares_in_range PASSED [ 60%]
test_square_counter.py::TestCountSquares::test_single_large_perfect_square PASSED [ 80%]
test_square_counter.py::TestCountSquares::test_single_point_is_square PASSED [100%]

============================== 5 passed in 0.02s ==============================
```

**結果：5 個通過 ✓ 綠燈確認**

---

## 結論

✓ 紅 → 綠 TDD 流程完整  
✓ 所有邊界案例都涵蓋  
✓ 例外處理（ValueError）正確  
✓ `count_squares()` 實作正確，效率 O(1)
