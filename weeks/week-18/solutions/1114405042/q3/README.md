# Q3: Digit Root (Base 16) - 1114405042

## 題目
實作 `digit_root_base16(n: int) -> int`：
- 反覆將 n 的 16 進位各位數相加，直到剩一位數（0–15）
- n < 0 → raise `ValueError`
- n = 0 → 0

## 範例
| n | hex | 過程 | 結果 |
|---|-----|------|------|
| 0 | 0x0 | — | 0 |
| 8 | 0x8 | — | 8 |
| 63 | 0x3F | 3+15=18 → 0x12 → 1+2 | 3 |
| 255 | 0xFF | 15+15=30 → 0x1E → 1+14 | 15 |

## 執行方式

```bash
# 測試
python3 -m unittest discover -s tests -p "test_*.py" -v

# 使用
python3 -c "from digit_root_base16 import digit_root_base16; print(digit_root_base16(63))"
```

## 演算法
數學公式：`1 + (n - 1) % 15`（base-16，b-1 = 15）
