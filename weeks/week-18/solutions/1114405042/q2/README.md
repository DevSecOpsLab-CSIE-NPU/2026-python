# Q2: Caesar Cipher (SHIFT=3) - 1114405042

## 完成題目
- ✅ Caesar 加密：字母向後位移 3 位（含 wraparound）

## 執行方式

```bash
# 一般版
echo "Hello, NPU!" | python3 task_caesar_shift.py

# 簡易版
echo "Hello, NPU!" | python3 task_caesar_shift-easy.py

# 測試
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## 演算法
- 小寫字母：`chr((ord(ch) - ord('a') + SHIFT) % 26 + ord('a'))`
- 大寫字母：`chr((ord(ch) - ord('A') + SHIFT) % 26 + ord('A'))`
- 非字母：直接保留

## 資料結構選擇
- 不使用對應表或 dict，純 ASCII 數學運算最簡潔

## TDD 摘要
1. Red: 9 個測試 → 全部失敗
2. Green: 實作 `caesar_encrypt()` → 9 tests pass
3. Refactor: 抽成獨立函式，製作 `-easy` 簡化版
