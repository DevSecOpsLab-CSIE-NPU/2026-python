# Week 10 "August Hell" 任務報告

**學生學號**: 1112405041
**學生姓名**: 李易宸

## 1. 完成項目
本週任務已全面完成，包含：
- **Homework Tasks (1-3)**: CSV 到 JSON 再到 XML 的完整轉換與效能視覺化。
- **CPE 魔改題 (5 題)**: 包含插頭 DP、Tarjan SCC、費馬點等進階演算法。
- **課堂範例鏡像 (6 主題)**: R01-R05, U01 的多版本實作與測試。
- **全套 TDD 證據**: 包含所有題目的 `Red -> Green` 紀錄與單元測試。

## 2. 執行方式

### 執行作業
```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
```

### 執行單元測試
```bash
# 一次執行所有測試
python -m unittest discover -s tests -p "test_*.py" -v
```

### 查看輸出
- JSON 輸出: `output/students.json`
- XML 輸出: `output/students.xml`
- 效能圖表: `output/timing_comparison.png`

## 3. 核心概念：@timeit 裝飾器
`@timeit` 裝飾器使用了 `functools.wraps` 來包裹目標函式。它的運作原理是在函式執行前記錄 `time.perf_counter()`，執行後再次記錄並計算差值，最後印出結果。這讓我們能在不修改原函式邏輯的情況下，輕鬆嵌入效能監控程式碼。

## 4. 生存心得：最難理解的 Bug
在實作 Q10235（插頭 DP）時，最難處理的是「左插頭 (1) 與右插頭 (2)」合併時的括號配對邏輯。當兩個左插頭撞在一起時，必須找到對應右插頭並將其改為左插頭。起初我的掃描方向寫錯，導致在複雜網格下出現負數方法數，最後透過手動追蹤狀態壓縮轉換才成功修正。

---
*本 PR 已嚴格遵守 August 教授的目錄結構與 TDD 規範。*
