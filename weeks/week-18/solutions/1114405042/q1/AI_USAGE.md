# AI Usage - Q1: Week 02 Homework

## 我問的問題
1. Python 保序去重怎麼做？
2. `sorted()` 多層排序的 key 怎麼寫？
3. `Counter` vs `defaultdict` 的差異？
4. 空輸入邊界如何處理？

## 採用的建議
1. `set` + `list.append` 保序去重（參考 R10-dedupe.py）
2. `sorted(key=lambda s: (-s[1], s[2], s[0]))` 多層排序
3. `Counter` + `most_common(1)` 統計

## 拒絕的建議
1. `OrderedDict.fromkeys()` 去重 → 改用 `set + list` 更直觀
2. 中間插 `print` 除錯 → 改用測試驗證
3. 直接 `set()` 輸出 → 題目要求保序

## 自行修正案例
AI 建議 `key=lambda s: (s[1], -s[2], s[0])`，但 score 應降序、age 應升序。
修正為 `key=lambda s: (-s[1], s[2], s[0])`。
