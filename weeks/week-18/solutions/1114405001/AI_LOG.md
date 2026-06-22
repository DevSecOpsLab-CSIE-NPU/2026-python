# AI_LOG.md - 第三題「任意進位的數字根」作答記錄

**學號：** 1114405001  
**分支：** `dev-0622`  
**題目：** 第三題「任意進位的數字根」（進位基底 = 8）

---

## 📋 每題開工前先澄清 - AI 反問清單

### ❓ AI 反問 1：函式簽名
**Q：函式叫什麼？吃什麼參數、回傳什麼型別？**  
**A：**
- 函式名：`digit_root_base8(n)`
- 參數：`n` (int) - 十進位整數
- 回傳值：(int) - 該數在 8 進位下的數字根（0-7）

### ❓ AI 反問 2：輸入邊界
**Q：資料範圍、筆數上限、輸入到 EOF 還是請回定行數？**  
**A：**
- 資料範圍：非負整數 (n ≥ 0)
- 筆數上限：題目範例給 3 個（0, 8, 63）
- 輸入方式：單筆測試用 unit test（不需讀 EOF）

### ❓ AI 反問 3：例外處理
**Q：非法輸入/空輸入/格式錯誤要怎麼處理？**  
**A：**
- 假設輸入合法（都是非負整數）
- 不需特殊例外處理（題目未要求）
- 邊界值由 test case 涵蓋

### ❓ AI 反問 4：Edge Case
**Q：至少列出 1 個邊界案例（如 0、空集合、全部被刪除、剛好等於門檻）**  
**A：**
- **Edge Case 1：** n=0（最小值） → 預期輸出 0
- **Edge Case 2：** n=64（8^2，冪次邊界） → 預期輸出 1
- **Edge Case 3：** n=511（8^3-1，全 F） → 預期輸出 7（需多層迭代）

### ❓ AI 反問 5：驗收標準
**Q：什麼樣的輸出才算對？依你學號的參數值是多少？**  
**A：**
- **驗收標準：** 數字根 = 將 n 轉換為 8 進位，重複相加各位數字，直到得到 0-7 之間的個位數
- **學號參數：** 進位基底 = 8（題目已指定）
- **測試依據：** 題目 Sample I/O
  - Input: 0, 8, 63
  - Output: 0, 1, 7

---

## 🔴 **步驟 1：先測試（紅燈）** → commit

### 設計 6 個 Test Case

#### Test 1️⃣：基礎案例（Sample I/O）
```python
Input:  [0, 8, 63]
Output: [0, 1, 7]
說明：題目提供的範例
```

#### Test 2️⃣：Edge - 零值
```python
Input:  0
Output: 0
說明：最小邊界，0 的數字根就是 0
```

#### Test 3️⃣：Edge - 8 的冪次（64 = 8²）
```python
Input:  64
Output: 1
說明：八進位 100 → 1+0+0 = 1
```

#### Test 4️⃣：複雜案例 - 多層迭代（511 = 8³-1）
```python
Input:  511
Output: 7
說明：
  511 八進位 = 777
  7+7+7 = 21（十進位）
  21 八進位 = 25
  2+5 = 7
```

#### Test 5️⃣：邊界 - 八進位個位數
```python
Input:  7
Output: 7
說明：7 本身已是八進位個位數，直接返回
```

#### Test 6️⃣：進階案例（100）
```python
Input:  100
Output: 2
說明：
  100 八進位 = 144
  1+4+4 = 9（十進位）
  9 八進位 = 11
  1+1 = 2
```

### 📊 測試執行結果（紅燈）

```
$ python test_digit_root.py -v

test_case_1_basic_sample ... FAIL
test_case_2_edge_zero ... FAIL
test_case_3_edge_power_of_8 ... FAIL
test_case_4_multiple_iterations ... FAIL
test_case_5_single_digit_in_base8 ... FAIL
test_case_6_large_number ... FAIL

Ran 6 tests in 0.007s
FAILED (failures=6)
```

✅ **確認紅燈** - 所有 6 個測試失敗（因實作為 `pass`）

### 📝 Commit

```bash
git add test_digit_root.py
git commit -m "test: 新增 6 個 digit root base 8 測試案例（含邊界值、多層相加）"
```

**Commit Hash:** `fe9c982`

---

## 🟢 **步驟 2：再寫實作（綠燈）** → commit

### 實作演算法

```python
def digit_root_base8(n):
    """計算 n 在 8 進位下的數字根"""
    # 特例：0 的數字根是 0
    if n == 0:
        return 0
    
    base = 8
    
    # 迴圈直到得到個位數（n < 8）
    while n >= base:
        digit_sum = 0
        # 計算 n 在 base 8 下各位數字的和
        while n > 0:
            digit_sum += n % base    # 取個位
            n //= base               # 移除個位
        n = digit_sum
    
    return n
```

### 📊 測試執行結果（綠燈）

```
$ python test_digit_root.py -v

test_case_1_basic_sample ... ok
test_case_2_edge_zero ... ok
test_case_3_edge_power_of_8 ... ok
test_case_4_multiple_iterations ... ok
test_case_5_single_digit_in_base8 ... ok
test_case_6_large_number ... ok

Ran 6 tests in 0.002s
OK
```

✅ **確認綠燈** - 全部 6 個測試通過

### 📝 Commit

```bash
git add digit_root.py
git commit -m "feat: 實作 digit root base 8 函數 - 轉換進位 + 反複相加至個位數"
```

**Commit Hash:** `e3c2d58`

---

## 📤 **步驟 3-5：Push + PR 準備**

### Push 到 Fork 分支

```bash
git push origin dev-0622
```

### PR 附上 AI_LOG.md

```bash
git add AI_LOG.md
git commit -m "docs: 新增 AI_LOG.md - 完整記錄題目解答過程"
git push origin dev-0622
```

**Commit Hash:** `932b143`

---

## 📋 **AI 協作過程記錄**

| 階段 | AI 反問內容 | 我的澄清 |
|------|------------|--------|
| 開工前 | ① 函式簽名 | `digit_root_base8(n)` 回傳 int |
| 開工前 | ② 輸入邊界 | 非負整數，無筆數限制 |
| 開工前 | ③ 例外處理 | 假設輸入合法 |
| 開工前 | ④ Edge Case | 零值、冪次、全 F |
| 開工前 | ⑤ 驗收標準 | 依題目 Sample I/O |
| 測試設計 | 需要幾個 test case？ | ≥6 個，含 ≥2 個 edge case |
| 測試設計 | 如何涵蓋邊界？ | 包括 0、冪次、多層迭代 |
| 實作驗證 | 演算法是否正確？ | 手動驗證 511 → 7 的計算 |

---

## ✅ **完成清單**

| 項目 | 完成度 | 備註 |
|------|--------|------|
| 開 feature 分支 | ✅ | `dev-0622` |
| 紅燈測試 + commit | ✅ | 6/6 失敗 |
| 綠燈實作 + commit | ✅ | 6/6 通過 |
| Push 到 fork | ✅ | `origin/dev-0622` |
| AI_LOG.md + commit | ✅ | 本檔案 |
| 開 PR（待手動） | ⏳ | From: `dev-0622` → To: `main` |

---

**完成日期：** 2026-06-22  
**狀態：** ✅ 代碼工作完成，等待開 PR
