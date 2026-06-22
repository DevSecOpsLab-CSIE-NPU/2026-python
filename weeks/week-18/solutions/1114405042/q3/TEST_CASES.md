# Test Cases - Q3: Digit Root (Base 16)

### Case 1: 零
- **輸入**: `digit_root_base16(0)` → `0`
- **狀態**: PASS
- **對應測試**: `test_zero`

### Case 2: 單位數
- **輸入**: `digit_root_base16(8)` → `8`
- **狀態**: PASS
- **對應測試**: `test_single_digit`

### Case 3: 兩位數（題目範例）
- **輸入**: `digit_root_base16(63)` → `3`
  - 63 = 0x3F → 3+15=18 → 0x12 → 1+2=3
- **狀態**: PASS
- **對應測試**: `test_two_hex_digits`

### Case 4: 邊界 0xFF
- **輸入**: `digit_root_base16(255)` → `15` (0xF)
  - 0xFF → 15+15=30 → 0x1E → 1+14=15
- **狀態**: PASS
- **對應測試**: `test_large_number`

### Case 5: 16 的冪
- **輸入**: `digit_root_base16(16)` → `1`, `digit_root_base16(256)` → `1`
- **狀態**: PASS
- **對應測試**: `test_power_of_16`

### Case 6: 反例（負數拋錯）
- **輸入**: `digit_root_base16(-1)` → raise ValueError
- **狀態**: PASS
- **對應測試**: `test_invalid_negative`
