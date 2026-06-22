# 第二題 凱撒密碼 (Caesar Cipher)

## 學生資訊
- 學號: 1114405003
- 姓名: 李玉落
- SHIFT = 4 (個位 3 % 25 + 5 + 1 = 4)

## 題目說明
將每行字串中的英文字母向後移 SHIFT 位：
- 大寫在 A-Z 內循環
- 小寫在 a-z 內循環
- 非英文字母字元 (空白、數字、標點) 原樣保留

## 檔案說明
- `caesar_cipher.py` - 主程式
- `test_caesar_cipher.py` - 單元測試 (17 個測試案例)
- `TEST_LOG_Q2.md` - 測試紀錄

## 執行方式

### 執行主程式
```bash
python caesar_cipher.py
```
輸入範例:
```
Hello, NPU!
abc XYZ
```
輸出:
```
Lipps, RTY!
efg BCD
```

### 執行測試
```bash
python -m unittest test_caesar_cipher -v
```

## 測試案例涵蓋
- 範例測資 (SHIFT=4)
- 大小寫循環 (Z→D, z→d)
- 非字母字元保留
- 空字串、單一字元
- SHIFT=0, SHIFT=26

## 範例驗證
| 輸入 | 輸出 |
|------|------|
| Hello, NPU! | Lipps, RTY! |
| abc XYZ | efg BCD |
