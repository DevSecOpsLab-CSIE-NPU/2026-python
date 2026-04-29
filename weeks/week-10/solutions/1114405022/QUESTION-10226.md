# 題目 10226

**題名**: Hardwood Species

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a219)
- [Yui Huang 題解](https://yuihuang.com/zj-a219/)

## 題目敘述

統計森林調查數據中各樹種出現的百分比。輸入為多筆測資，每筆以空行分隔，每行為一個樹種名稱。
要求依字典序輸出每個樹種及其百分比（四位小數）。

## 解題思路

### Easy 版本（好記版）
- 使用 `split("\n\n")` 按空行切分測資（符合題意）
- 用 Counter 快速統計樹種次數
- 依字典序排序後計算百分比
- 注重流程固定，便於考場快速回想

### 一般版本（逐行掃描版）
- 用 `splitlines()` 逐行讀取，更精確控制狀態
- 用 defaultdict 統計，可處理任意格式變異
- 邊讀邊維護測資狀態指針
- 適合複雜或不規則的輸入格式

## 程式檔案

- AI 教你的簡單版本，有中文註解: [10226_easy.py](./10226_easy.py)
  - 使用 split("\n\n") 技巧，流程明確
  - 最適合考場回想

- 你手打的程式: [10226.py](./10226.py)
  - 逐行掃描版本，更穩健
  - 可應對格式變異

- 測試程式: [test_10226.py](./test_10226.py)
  - 包含 3 個完整測試用例
  - 驗證多樹種、單一樹種、多測資等情況

- 你手打程式的測試 LOG 記錄: [manual-test-log.txt](./manual-test-log.txt)
  - 最終測試通過紀錄

## 測試用例

### Case 1：一般多樹種統計
```
輸入：
1

Oak
Pine
Oak
Maple
Pine
Oak

預期輸出：
Maple 16.6667
Oak 50.0000
Pine 33.3333
```

### Case 2：單一樹種 100%
```
輸入：
1

Red Maple
Red Maple
Red Maple

預期輸出：
Red Maple 100.0000
```

### Case 3：多測資 + 大小寫視為不同字串
```
輸入：
2

oak
Oak
oak

Beech
Ash
Beech

預期輸出：
Oak 33.3333
oak 66.6667

Ash 33.3333
Beech 66.6667
```

## 優化紀錄

**2026-04-29 版本更新**：
- 從 0422 分支復原優化版本
- 加強了 easy 版本的中文註解
- 擴展測試用例，涵蓋邊界情況
- 升級手打版本的穩健性（逐行掃描 + 狀態管理）


