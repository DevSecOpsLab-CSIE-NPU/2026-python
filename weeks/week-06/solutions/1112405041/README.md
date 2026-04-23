# Week 06 複習與模板整理：生成器與優化暴力法

本週為「沉澱週」，主要任務是複習 W01-W05 的解題邏輯，並針對 Python 的迭代器與常用 I/O 進行模板化整理，以應對後續更複雜的 UVA 題目。

## 🛠️ 1. 核心 I/O 模板 (處理多筆測資)
大一最常卡關的地方就是不知如何處理「直到 EOF 結束」或「指定組數」的輸入。

### 🔹 模式 A：直到 EOF 結束 (UVA 常用)
```python
import sys

def template_eof():
    # 一次讀取所有行並去掉換行符
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        # 處理邏輯...
        print(line)
```

### 🔹 模式 B：指定組數 (T 次)
```python
def template_test_cases():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    t = int(input_data[0])
    curr = 1
    for _ in range(t):
        # 根據題目需求讀取變數
        n = int(input_data[curr])
        curr += 1
        # 處理邏輯...
```

---

## ⚡ 2. 迭代器與生成器 (W06 主題)
針對暴力法解題，使用生成器（Generator）可以有效節省記憶體並優化邏輯。

### 🔹 質數生成器模板
```python
def prime_generator(limit):
    """產生小於等於 limit 的所有質數"""
    primes = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if primes[p]:
            yield p
            for i in range(p * p, limit + 1, p):
                primes[i] = False

# 使用方法：
# for p in prime_generator(100):
#     print(p)
```

---

## 📊 3. 複習心得
回顧 W01 到 W05，我發現很多題目（如 10038 Jolly Jumpers）其實只要用對 **Set (集合)** 或 **Sort (排序)** 就能降維打擊。這週整理完模板後，我更有信心處理之後的實彈炸射。

感謝 AI 旗艦機在整理過程中，幫我優化了 Pythonic 的寫法，讓我的代碼看起來不像「C 語言寫法的 Python」，而是真正的 Python 代碼！
