# Test Log - UVA 11417 GCD

## 測試執行結果

### 初始（紅燈）
```
$ python -m pytest test_gcd.py -v

test_gcd.py::TestSumOfGcd::test_n_equals_1 PASSED                        [ 25%]
test_gcd.py::TestSumOfGcd::test_n_equals_10 FAILED                       [ 50%]
test_gcd.py::TestSumOfGcd::test_n_equals_2 FAILED                        [ 75%]
test_gcd.py::TestSumOfGcd::test_n_equals_3 FAILED                        [100%]

================================== FAILURES ===================================
________________________ TestSumOfGcd.test_n_equals_10 ________________________

self = <test_gcd.TestSumOfGcd testMethod=test_n_equals_10>

    def test_n_equals_10(self):
        """題目範例: 結果應為 67"""
>       self.assertEqual(sum_of_gcd(10), 67)
E       AssertionError: 0 != 67

test_gcd.py:32: AssertionError
________________________ TestSumOfGcd.test_n_equals_2 _________________________

self = <test_gcd.TestSumOfGcd testMethod=test_n_equals_2>

    def test_n_equals_2(self):
        """基本案例: gcd(1,2)=1，總和應為 1"""
>       self.assertEqual(sum_of_gcd(2), 1)
E       AssertionError: 0 != 1

test_gcd.py:24: AssertionError
________________________ TestSumOfGcd.test_n_equals_3 _________________________

self = <test_gcd.TestSumOfGcd testMethod=test_n_equals_3>

    def test_n_equals_3(self):
        """中等案例: gcd(1,2)=1, gcd(1,3)=1, gcd(2,3)=1，總和應為 3"""
>       self.assertEqual(sum_of_gcd(3), 3)
E       AssertionError: 0 != 3

test_gcd.py:28: AssertionError
=========================== short test summary info ===========================
FAILED test_gcd.py::TestSumOfGcd::test_n_equals_10 - AssertionError: 0 != 67
FAILED test_gcd.py::TestSumOfGcd::test_n_equals_2 - AssertionError: 0 != 1
FAILED test_gcd.py::TestSumOfGcd::test_n_equals_3 - AssertionError: 0 != 3
========================= 3 failed, 1 passed in 0.08s =========================
```

**結果：3 個失敗，1 個通過 ✓ 紅燈確認**

---

### 最終（綠燈）
```
$ python -m pytest test_gcd.py -v

test_gcd.py::TestSumOfGcd::test_n_equals_1 PASSED                        [ 25%]
test_gcd.py::TestSumOfGcd::test_n_equals_10 PASSED                       [ 50%]
test_gcd.py::TestSumOfGcd::test_n_equals_2 PASSED                        [ 75%]
test_gcd.py::TestSumOfGcd::test_n_equals_3 PASSED                        [100%]

============================== 4 passed in 0.02s ==============================
```

**結果：4 個通過 ✓ 綠燈確認**

---

## 結論

✓ 紅 → 綠 TDD 流程完整  
✓ 所有測試用例都通過  
✓ `sum_of_gcd()` 實作正確
