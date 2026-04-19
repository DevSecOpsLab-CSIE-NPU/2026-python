# AI 使用說明

## 📋 作業背景

本作業是 **TDD (測試驅動開發)** 實習，目標是整合 Week 02 (資料結構) 和 Week 07 (檔案 I/O) 的技能。

**重點**: 學習如何透過「測試先行」的方式來設計程式。

---

## ✅ 允許使用 AI 的時機

### 1️⃣ 寫測試時 (最重要!)
**場景**: 不確定如何寫 unittest 測試

**允許做法**:
```python
# ✅ 可以問 AI:
# "幫我寫一個 unittest 測試，檢查一個函數是否回傳正確的值"

def test_load_generals_from_file(self):
    """測試正確讀取 9 位武將"""
    game = ChibiBattle()
    game.load_generals('generals.txt')
    self.assertEqual(len(game.generals), 9)  # AI 幫忙寫這行
```

**禁止做法**:
```python
# ❌ 不能：直接複製 AI 給的整個測試檔
# ❌ 不能：直接問 AI「幫我寫 test_chibi.py」然後全部複製
```

---

### 2️⃣ 實現遇到 Python 語法問題
**場景**: 不知道如何使用 `namedtuple` 或 `Counter`

**允許做法**:
```python
# ✅ 可以問 AI:
# "如何使用 Python Counter 來統計出現次數？"
# "namedtuple 的基本使用方法是什麼？"

# 然後自己改寫成符合作業需求的版本
```

**禁止做法**:
```python
# ❌ 不能：複製 AI 給的完整實現
# ❌ 不能：直接問「幫我實現 calculate_damage 函數」然後全部用
```

---

### 3️⃣ ASCII 視覺化設計
**場景**: 想做漂亮的報告視覺化

**允許做法**:
```python
# ✅ 可以問 AI:
# "如何在 Python 中使用 Unicode 字符做進度條?"
# "如何對齊文字輸出？"

# 然後自己調整格式
```

**禁止做法**:
```python
# ❌ 不能：直接複製 AI 的視覺化程式碼
```

---

### 4️⃣ 代碼重構和優化
**場景**: 想要改進程式碼結構

**允許做法**:
```python
# ✅ 可以問 AI:
# "這段程式碼可以如何改進可讀性？"
# "如何重構這個函數避免重複代碼？"

# 然後理解後自己改寫
```

---

## ❌ 禁止使用 AI 的地方

### 1️⃣ 完整複製 AI 生成的代碼
```python
# ❌ 禁止！
# 直接問 AI: "幫我寫 chibi_battle.py"
# 然後複製整個檔案

# ✅ 正確做法：
# 分段理解，自己改寫每一部分
```

### 2️⃣ 跳過 TDD 三階段流程
```python
# ❌ 禁止！
# 先寫實現，再補測試

# ✅ 正確做法：
# 1. 先寫測試 (RED)
# 2. 寫最小化實現 (GREEN)
# 3. 重構改進 (REFACTOR)
```

### 3️⃣ 使用 `as any` 或 `@suppress` 壓制錯誤
```python
# ❌ 禁止！
from typing import Any
data: Any = some_value  # type: ignore

# ✅ 正確做法：
# 解決真正的型別問題，而不是隱藏它
```

### 4️⃣ 不理解就直接用
```python
# ❌ 禁止！
# 複製 AI 給的程式碼但不知道在幹什麼

# ✅ 正確做法：
# 先問為什麼要這樣做，然後自己改寫
```

---

## 🎯 推薦作法 (最佳實踐)

### 第 1 步: 先自己寫測試
```python
# 1. 閱讀 HOMEWORK.md
# 2. 根據需求寫測試
# 3. 運行測試，看它們失敗 (RED)

def test_load_generals_from_file(self):
    game = ChibiBattle()
    game.load_generals('generals.txt')
    self.assertEqual(len(game.generals), 9)

# 執行: python -m pytest test_chibi.py
# 結果: FAILED ❌ (預期的！)
```

### 第 2 步: 問 AI 如何使用相關工具
```
# 問 AI: "我要讀取一個 EOF 結尾的 txt 檔案，
#        並解析為 namedtuple，應該如何做？"

# AI 會告訴你：
# 1. 使用 open() 讀檔
# 2. 使用 for line in f 迴圈
# 3. 使用 namedtuple(name, fields) 定義結構
```

### 第 3 步: 根據理解自己實現
```python
from collections import namedtuple

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

def load_generals(self, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == 'EOF':
                break
            # 自己改寫解析邏輯
```

### 第 4 步: 運行測試驗證
```bash
# 執行: python -m pytest test_chibi.py::TestStage1
# 結果: PASSED ✓ (Green!)
```

### 第 5 步: 重構改進
```python
# 重構後：
# - 加入註解
# - 改進可讀性
# - 新增視覺化

# 重新運行所有測試
# 確保全部通過！
```

---

## 📊 AI 使用建議量

| 任務 | 建議用量 | 理由 |
|-----|--------|------|
| 寫測試 | 20-30% | 學習 unittest 框架 |
| 使用 API | 30-40% | 學習如何使用 Python 內建功能 |
| 實現邏輯 | 10-20% | 這是最重要的學習部分 |
| 視覺化 | 30-50% | 純粹的美化，不影響邏輯 |
| 重構優化 | 20-30% | 學習代碼品質 |

**總計**: 不應完全依賴 AI，應該理解 80% 以上的代碼。

---

## 🚨 常見 AI 陷阱

### 陷阱 1: 一次性解決所有問題
```python
# ❌ 不要：
# "幫我完成整個 chibi_battle.py"

# ✅ 應該：
# "我想用 sorted() 按屬性排序，怎麼做？"
```

### 陷阱 2: 複製貼上不理解
```python
# ❌ 不要：
code_from_ai = copy_paste()
# 然後不知道它在幹什麼

# ✅ 應該：
# 一行一行理解，必要時改寫
```

### 陷阱 3: 忽視測試失敗
```python
# ❌ 不要：
# 測試失敗後直接改代碼

# ✅ 應該：
# 讀懂失敗信息，再決定如何改
```

---

## ✨ AI 的最佳使用場景

### 場景 1: 學習新工具時
```
問: "Counter 的 most_common() 如何使用?"
→ AI 給你範例
→ 你理解後自己改寫
```

### 場景 2: 卡在 Python 語法
```
問: "如何在迴圈中跳過 EOF 這一行?"
→ AI 給你 if line == 'EOF': break
→ 你理解後加入程式碼
```

### 場景 3: 測試報告美化
```
問: "如何在 Python 中印出進度條?"
→ AI 給你 Unicode 字符的方法
→ 你自己調整格式和顏色
```

---

## ⚠️ 學術誠實政策

**本作業強調**: 你應該學到真正的技能，而不是依賴 AI。

### 評分標準
- ✅ **程式正確性** (40%): 測試通過
- ✅ **代碼品質** (30%): 可讀性、註解清楚
- ✅ **TDD 流程** (20%): 三階段完成
- ✅ **理解程度** (10%): 能解釋代碼邏輯

### 查重政策
如果發現代碼是完全複製 AI 的，會視為違反學術誠實政策。

---

## 📝 作業提交時應包含

1. ✅ `chibi_battle.py` (手寫版，有註解)
2. ✅ `chibi_battle_easy.py` (簡化版)
3. ✅ `test_chibi.py` (12 個測試)
4. ✅ `TEST_LOG.md` (測試日誌)
5. ✅ `generals.txt` (輸入資料)
6. ✅ `battles.txt` (戰役配置)
7. ✅ `AI_USAGE.md` (本檔案)

---

## 🎓 最後提醒

> **AI 是工具，不是作弊工具。**
>
> 使用 AI 的目的是學習，而不是逃避學習。
>
> 如果你能夠理解並改寫 AI 生成的代碼，那就是成功的使用。

---

**祝你學習順利！如有問題，請先嘗試理解錯誤訊息再尋求協助。** 🚀
