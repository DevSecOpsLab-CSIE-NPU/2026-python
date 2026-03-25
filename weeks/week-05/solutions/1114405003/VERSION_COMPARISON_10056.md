# UVA 10056 - 骰子遊戲獲勝機率【版本比較】

## 📊 總覽

| 項目 | 完整版 | Easy版 | 手打版 |
|------|-------|--------|-------|
| 檔案 | test_solution_10056.py | test_solution_10056_easy.py | solution_10056_easy.py |
| 測試數量 | 12 個 | 6 個 | - |
| 代碼行數 | ~270行 | ~100行 | ~12行 |
| 難度等級 | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| 最佳用途 | 深入學習 | 普通複習 | 考試速寫 |
| 測試通過率 | ✅ 100% (12/12) | ✅ 100% (6/6) | ✅ 邏輯驗證通過 |

---

## 🔍 核心算法對比

### 完整版 - 詳細註解版本

```python
@staticmethod
def calculate_win_probability(n: int, p: float, i: int) -> float:
    """計算第 i 個玩家的獲勝機率"""
    
    # 特殊情況：p = 1（必然成功）
    if p == 1.0:
        return 1.0 if i == 1 else 0.0
    
    # 一般情況
    fail_prob = 1 - p
    numerator = (fail_prob ** (i - 1)) * p
    denominator = 1 - (fail_prob ** n)
    probability = numerator / denominator
    
    return probability
```

**特點：**
- 類別式封裝 `DiceGameSolver`
- 詳細的中文註解與數學推導
- 4個測試類別分類（BasicLogic、ProbabilityDistribution、EdgeCases、RealWorldCases）
- 包含12個全面的單元測試
- 涵蓋邊界情況、精度測試、真實案例

### Easy版 - 簡化記憶版本

```python
@staticmethod
def win_prob(n, p, i):
    """計算玩家 i 的獲勝機率"""
    if p == 1.0:
        return 1.0 if i == 1 else 0.0
    
    fail = 1 - p
    numerator = (fail ** (i - 1)) * p
    denominator = 1 - (fail ** n)
    
    return numerator / denominator
```

**特點：**
- 簡短函數名稱 (`win_prob` 而非 `calculate_win_probability`)
- 變數命名更簡潔 (`fail` 而非 `fail_prob`)
- 參數不包含類型註解
- 用1️⃣到5️⃣標記核心步驟
- 核心測試專注於基本概率驗證

### 手打版 - 考試準備版本

```python
def win_prob(n, p, i):
    if p == 1.0:
        return 1.0 if i == 1 else 0.0
    fail = 1 - p
    numerator = (fail ** (i - 1)) * p
    denominator = 1 - (fail ** n)
    return numerator / denominator
```

**特點：**
- 最簡潔的代碼結構（8行）
- 無任何註解，純邏輯代碼
- 易於快速輸入考試
- 直接可用的測試示例

---

## 📋 測試覆蓋對比

### 完整版 - 12 個測試

| 測試類別 | 測試名稱 | 驗證重點 |
|---------|---------|---------|
| **BasicLogic** | single_player | 單玩家=1.0 |
| | guaranteed_success | p=1時特殊情況 |
| | two_players_equal_probability | 2玩家p=0.5 |
| | first_player_advantage | 先手優勢 |
| **ProbabilityDistribution** | three_players_all_equal | 三玩家概率和=1 |
| | low_probability_player_three | 後位玩家概率 |
| | high_success_rate | 高p=0.9情況 |
| **EdgeCases** | many_players_first_vs_last | N=10時先手優勢明顯 |
| | probability_precision | 精確到小數點後4位 |
| | very_small_probability | p=0.01極小值 |
| **RealWorldCases** | standard_dice_three_players | p=1/6真實案例 |
| | coin_flip_two_players | p=0.5擲硬幣案例 |

### Easy版 - 6 個測試

| 測試類別 | 測試名稱 | 驗證重點 |
|---------|---------|---------|
| **TestBasic** | single_player | 單玩家 |
| | must_win | p=1特殊情況 |
| | two_player_fair | 2玩家平公平 |
| **TestProbability** | sum_equals_one | 概率和=1 |
| | first_player_advantage | 先手優勢 |
| | dice_six_numbers | 骰子案例 |

---

## 🎯 核心公式

```
P(i) = (1-p)^(i-1) × p / (1 - (1-p)^N)

其中：
- (1-p)^(i-1) = 前i-1個玩家都失敗的概率
- p = 玩家i成功的概率
- (1-p)^N = 一整輪所有玩家都失敗的概率

特殊情況：
如果 p = 1.0：
  - 玩家1成功機率 = 1.0
  - 其他玩家機率 = 0.0
```

---

## 📊 使用建議

### 何時使用完整版？
✅ 初次學習此演算法
✅ 需要理解概率數學原理
✅ 進行深度的單元測試
✅ 研究各種邊界條件

### 何時使用Easy版？
✅ 複習核心概率計算
✅ 學習後驗證理解
✅ 準備筆試或小考
✅ 需要簡潔明瞭的示例

### 何時使用手打版？
✅ 正式考試時參考
✅ 練習快速輸入代碼
✅ 時間限制情況
✅ 驗證核心邏輯

---

## ✅ 測試執行結果

### 完整版
```
Ran 12 tests in 0.004s
OK
```

### Easy版
```
Ran 6 tests in 0.002s
OK
```

### 手打版（邏輯驗證）
```
win_prob(1, 0.5, 1) = 1.0000 ✅
win_prob(2, 0.5, 1) = 0.6667 ✅
win_prob(2, 0.5, 2) = 0.3333 ✅
win_prob(3, 1/6, 1) = 0.3956 ✅
```

---

## 🔑 核心知識點

### 概率遞推邏輯
```
玩家 i 獲勝 = 前i-1人失敗 且 玩家i成功 (首次)
           或 全部N人都失敗 且 遊戲重新開始後玩家i獲勝

設 P(i) = 玩家i最終獲勝機率

P(i) = (1-p)^(i-1) × p + (1-p)^N × P(i)

解出：
P(i) = (1-p)^(i-1) × p / (1 - (1-p)^N)
```

### 先手優勢
```
P(1) > P(2) > P(3) > ... > P(N)

因為：
- P(1) = p / (1 - (1-p)^N)
- P(i) = (1-p)^(i-1) × p / (1 - (1-p)^N)
- (1-p)^(i-1) 隨著 i 增加而減小
```

### 機率和驗證
```
Σ P(i) = 1.0 （必然有人獲勝）

驗證：
P(1) + P(2) + ... + P(N)
= p × [1 + (1-p) + (1-p)^2 + ... + (1-p)^(N-1)] / (1 - (1-p)^N)
= p × [1 - (1-p)^N] / [(1 - (1-p)) × (1 - (1-p)^N)]
= p / p
= 1 ✓
```

---

## 📝 檔案位置

```
d:\1114405003李玉蓉\2026-python\weeks\week-05\solutions\1114405003\
├── test_solution_10056.py           # 完整版測試程式
├── test_solution_10056_easy.py      # Easy版測試程式
├── solution_10056_easy.py           # 考試手打版本
├── test_result_10056.txt            # 完整版測試記錄
└── test_result_10056_easy.txt       # Easy版測試記錄
```

---

## 💾 建立時間與驗證

- **完整版**：✅ 12/12 測試通過
- **Easy版**：✅ 6/6 測試通過
- **手打版**：✅ 邏輯驗證通過（4個案例）

所有版本均已驗證，可直接使用！

---

## 🎓 學習路徑

建議按以下順序學習：

1. **先讀手打版** (3分鐘)
   - 快速理解核心公式
   - 掌握特殊情況處理

2. **再做Easy版測試** (8分鐘)
   - 驗證基本邏輯
   - 理解概率計算步驟

3. **最後研究完整版** (20分鐘)
   - 深入概率數學原理
   - 理解各種邊界情況

這樣可以從簡到繁逐步掌握！
