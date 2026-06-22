# Test Cases - Q2: Caesar Cipher (SHIFT=3)

### Case 1: 題目範例
- **輸入**: `Hello, NPU!`
- **預期輸出**: `Khoor, QSX!`
- **狀態**: PASS
- **對應測試**: `tests/test_caesar_shift.py::TestCaesarShift::test_example_hello_npu`

### Case 2: Wraparound 範例
- **輸入**: `abc XYZ`
- **預期輸出**: `def ABC`
- **狀態**: PASS
- **對應測試**: `tests/test_caesar_shift.py::TestCaesarShift::test_example_abc_xyz`

### Case 3: 邊界 wraparound 小寫
- **輸入**: `xyz` → `abc`
- **狀態**: PASS
- **對應測試**: `tests/test_caesar_shift.py::TestCaesarShift::test_wraparound_lowercase`

### Case 4: 邊界 wraparound 大寫
- **輸入**: `XYZ` → `ABC`
- **狀態**: PASS
- **對應測試**: `tests/test_caesar_shift.py::TestCaesarShift::test_wraparound_uppercase`

### Case 5: 邊界非字母不變
- **輸入**: `123 !@#` → `123 !@#`
- **狀態**: PASS
- **對應測試**: `tests/test_caesar_shift.py::TestCaesarShift::test_non_alpha_unchanged`
