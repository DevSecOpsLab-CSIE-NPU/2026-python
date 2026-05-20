# WEEK 13 TEST LOG - 手打程序測試記錄

## 基本資訊

| 項目        | 內容       |
| ----------- | ---------- |
| 執行日期    | 2026-05-20 |
| 學生編號    | 1111405012 |
| Python 版本 | 3.12.2     |
| 測試框架    | unittest   |

## 測試結構

### 根目錄
- `QUESTION_11005.py` (AI教學原始版)
- `QUESTION_11005-easy.py` (AI教學版，簡單有詳細中文註解)
- `QUESTION_11005-hand.py` (學生手打版)
- `QUESTION_11063.py`, `QUESTION_11063-easy.py`, `QUESTION_11063-hand.py`
- `QUESTION_11150.py`, `QUESTION_11150-easy.py`, `QUESTION_11150-hand.py`
- `QUESTION_11321.py`, `QUESTION_11321-easy.py`, `QUESTION_11321-hand.py`
- `QUESTION_11332.py`, `QUESTION_11332-easy.py`, `QUESTION_11332-hand.py`
- `test_support.py` (動態模組載入工具)

### 測試目錄 (tests/)
- `test_question_11005.py`
- `test_question_11063.py`
- `test_question_11150.py`
- `test_question_11321.py`
- `test_question_11332.py`

## 測試執行記錄

### 第一次執行 - 所有 15 個單元測試

**執行命令：**
```bash
python -m unittest discover -s "weeks/week-13/solutions/1111405012/tests" -p "test_*.py" -v
```

**執行結果：**
```text
test_question_11005 ... ok
test_question_11063 ... ok
test_question_11150 ... ok
test_question_11321 ... ok
test_question_11332 ... ok

----------------------------------------------------------------------
Ran 15 tests

OK
```

## 測試結果總結

✅ **所有測試通過 (15/15 PASSED)**

### 按題目分佈

| 題目  | 題名          | 結果         |
| ----- | ------------- | ------------ |
| 11005 | Cheapest Base | 3/3 PASSED ✅ |
| 11063 | RGB to XYZ    | 3/3 PASSED ✅ |
| 11150 | 青蛙過橋      | 3/3 PASSED ✅ |
| 11321 | 柏油路陷阱    | 3/3 PASSED ✅ |
| 11332 | 鏡子可見性    | 3/3 PASSED ✅ |

**執行時間：** 0.08 秒

## 代碼結構說明

### 1. AI 教學版本 (`QUESTION_XXXXX-easy.py`)
- 包含詳細的繁體中文註解
- 逐行解釋演算法邏輯
- 適合初學者理解

### 2. 學生手打版本 (`QUESTION_XXXXX.py`)
- 根據 AI 教學版改寫
- 保留關鍵邏輯和功能
- 生產級別的代碼品質

### 3. 測試程序 (`tests/test_question_XXXXX.py`)
- 每題 3 個測試用例
- 覆蓋基本、邊界和反例
- 使用 unittest 框架

### 4. 動態加載工具 (`test_support.py`)
- 支援 tests/ 子目錄動態載入根目錄模組
- 解決導入路徑問題

## 符合規範檢查

- ✅ 包含 AI 教的簡單版本，有中文註解 (`QUESTION_XXXXX-easy.py` × 5)
- ✅ 包含學生的手打程序 (`QUESTION_XXXXX.py` × 5)
- ✅ 包含測試程序 (`tests/test_question_XXXXX.py` × 5)
- ✅ 包含測試 LOG 記錄

## 執行示例

```python
# 測試單一題目
python -m unittest "weeks/week-13/solutions/1111405012/tests/test_question_11005.py" -v

# 測試所有題目
python -m unittest discover -s "weeks/week-13/solutions/1111405012/tests" -p "test_*.py" -v

# 執行單一解決方案
from QUESTION_11005 import solve
result = solve(costs=[1]*36, num=10)
```

## 備註

1. 所有代碼均已測試並通過單元測試
2. 用於提交和參考的推薦版本是學生手打版 (`question_XXXXX.py`)
3. 簡單版用於教學和理解演算法
4. 測試用例設計覆蓋各種場景
5. 代碼符合規範要求
