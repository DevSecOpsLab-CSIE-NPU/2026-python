# AI_LOG.md - Caesar Cipher (SHIFT=2) 實作日誌

## 任務概述
- **題目**：凱撒密碼（Caesar Cipher）
- **位移值**：SHIFT = 2
- **分支**：feature-0622-2
- **日期**：2026-06-22

---

## 📋 步驟 2：Test Cases 拆解

### Test Case 1：基本功能測試（小寫 + 特殊字符）
```python
Input:  "Hello, NPU!"
Expected: "Jgnnq, PRW!"
說明：測試基本的字母位移和特殊字符保留
```

### Test Case 2：邊界案例（字母環繞）
```python
Input:  "xyz XYZ"
Expected: "zab ZAB"
說明：測試 XYZ 環繞至 AB 的邊界情況
```

### Test Case 3：混合字符測試（數字 + 符號 + 空白）
```python
Input:  "abc123!@# ABC"
Expected: "cde123!@# CDE"
說明：驗證非字母字符保持不變
```

### Test Case 4：全大寫測試
```python
Input:  "ABCXYZ"
Expected: "CDEZAB"
說明：測試大寫字母的位移和環繞
```

### Test Case 5：純特殊字符測試（Edge Case）
```python
Input:  "123 !@# $%^"
Expected: "123 !@# $%^"
說明：驗證沒有字母的字符串保持不變
```

---

## 🔴 步驟 3：測試紅燈確認

**命令**：
```bash
python test_caesar_cipher.py
```

**結果**：
```
FFFFF
FAILED (failures=5)
```

✅ 所有 5 個測試失敗（符合預期的紅燈）

**提交**：
```bash
git commit -m "test: Add 5 test cases for Caesar Cipher (SHIFT=2) - RED"
```

---

## 🟢 步驟 4：實作綠燈

### 實作方案

使用字符偏移計算實現凱撒密碼：

```python
def caesar_cipher(text):
    SHIFT = 2
    result = []
    
    for char in text:
        if 'a' <= char <= 'z':
            # Shift lowercase letters
            new_char = chr((ord(char) - ord('a') + SHIFT) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            # Shift uppercase letters
            new_char = chr((ord(char) - ord('A') + SHIFT) % 26 + ord('A'))
            result.append(new_char)
        else:
            # Keep other characters unchanged
            result.append(char)
    
    return ''.join(result)
```

### 核心邏輯
1. **字母檢測**：區分大小寫字母
2. **位移計算**：`(ord(char) - ord('A') + SHIFT) % 26`
   - 轉換為 0-25 的位置
   - 加上位移值
   - 模 26 實現環繞
3. **字符保留**：非字母字符保持不變

### 測試結果
```bash
Ran 5 tests in 0.001s
OK
```

✅ 所有測試通過（綠燈）

**提交**：
```bash
git commit -m "feat: Implement Caesar Cipher (SHIFT=2) - GREEN"
```

---

## 📤 步驟 5：Push 到分支

```bash
git push -u origin feature-0622-2
```

✅ 分支已推送到遠端倉庫

---

## 📊 測試覆蓋分析

| Test Case | 類型 | 覆蓋場景 |
|-----------|------|---------|
| Test 1 | 功能性 | 基本位移 + 特殊字符 |
| Test 2 | Edge Case | 字母環繞（XYZ → ZAB） |
| Test 3 | 功能性 | 數字和符號保留 |
| Test 4 | 功能性 | 大寫字母位移 |
| Test 5 | Edge Case | 純特殊字符（無變化） |

✅ 涵蓋 5 個測試案例，包含 2 個 Edge Case

---

## 📝 關鍵實現細節

### 位移計算步驟
對於字符 'Y'（位置24）：
```
Y: pos=24
Y + SHIFT: 24 + 2 = 26
Modulo 26: 26 % 26 = 0
結果: chr(0 + ord('A')) = 'A'
```

對於字符 'Z'（位置25）：
```
Z: pos=25
Z + SHIFT: 25 + 2 = 27
Modulo 26: 27 % 26 = 1
結果: chr(1 + ord('A')) = 'B'
```

### 特殊字符處理
- **空格、標點、數字**：直接保留，不進行位移
- **大小寫區分**：分別使用 `ord('a')` 和 `ord('A')` 計算

---

## ✅ 完成檢查表

- [x] 測試案例拆解（≥3 個，含 ≥1 個 Edge Case）
- [x] 測試代碼編寫
- [x] 紅燈確認
- [x] 實作代碼編寫
- [x] 綠燈確認
- [x] 代碼提交（2 commits）
- [x] Push 到分支
- [x] AI_LOG.md 文檔

---

## 📋 提交歷史

```
commit 18cc63c: feat: Implement Caesar Cipher (SHIFT=2) - GREEN
commit d5d5d1d: test: Add 5 test cases for Caesar Cipher (SHIFT=2) - RED
```

---

## 🎯 下一步

- [ ] 步驟 6：開 PR（feature-0622-2 → 課程 repo main）
- [ ] 步驟 7：PR 附帶此 AI_LOG.md

---

**AI 助手**：GitHub Copilot (Claude Haiku 4.5)  
**完成時間**：2026-06-22  
**狀態**：✅ 實作完成，所有測試通過
