# 0617 Starter — timeit + 搜尋效能評估

> 本日是 6/18 完整實驗室的**預演**:先把 `timeit` 做出來,再用它對搜尋做一次粗略評估。  
> 細節與課堂節奏見 [`../0617-search-eval.md`](../0617-search-eval.md)。

## 使用方式

```bash
cp -r weeks/week-17/in_class/0617-starter weeks/week-17/solutions/<學號>/0617
cd weeks/week-17/solutions/<學號>/0617
```

## 固定循環

**Read spec → Dev for red(`test:` commit)→ Dev for green(`feat:` commit)→ push**。

## 檔案說明

- `timing.py`: 實作 `timeit` 裝飾器，測量函式執行時間，並計算平均時間。
- `search.py`: 包含兩個搜尋函式：`linear_search` 和 `binary_search`，前者進行逐一比對，後者需對已排序的資料進行搜尋。
- `tests/test_timing.py`: 單元測試 `timeit` 裝飾器，驗證其功能正確性。
- `tests/test_search.py`: 單元測試 `search.py` 中的搜尋函式，檢查其正確性。
- `AI_LOG.md`: 記錄與 AI 的互動，包括問題和回答。
- `TEST_LOG.md`: 記錄測試結果，包括遇到的問題及其解決方案。
- `README.md`: 提供專案概述，包括設置和使用說明，以及已實作功能的詳細資訊。
- `requirements.txt`: 列出專案所需的依賴包。
- `pyproject.toml`: 專案的配置文件，指定建構系統需求及其他專案元數據。

## 專案功能

1. **計時裝飾器**: `timeit` 裝飾器可測量函式的執行時間，並計算平均值。
2. **搜尋功能**: 提供線性搜尋和二元搜尋，滿足不同的搜尋需求。
3. **測試覆蓋**: 透過單元測試確保功能的正確性和穩定性。

## 開發規則

- 確保每個功能都有相應的測試。
- 在開發過程中，記錄所有的測試結果和問題解決過程。
- 按照規範進行版本控制，確保每次提交都有清晰的描述。