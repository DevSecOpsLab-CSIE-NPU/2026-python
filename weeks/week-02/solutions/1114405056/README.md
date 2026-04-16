# Week 02 Solution — 1114405056

> Python 版本：3.12+

---

## 完成題目清單

| 題目 | 狀態 |
|------|------|
| Task 1：Sequence Clean | ✅ 完成 |
| Task 2：Student Ranking | ✅ 完成 |
| Task 3：Log Summary | ✅ 完成 |

---

## 執行方式

### 程式執行

```bash
# Task 1（從 stdin 輸入）
echo "5 3 5 2 9 2 8 3 1" | python task1_sequence_clean.py

# Task 2（從 stdin 輸入）
python task2_student_ranking.py << EOF
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
EOF

# Task 3（從 stdin 輸入）
python task3_log_summary.py << EOF
8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
EOF
```

### 測試執行

```bash
# 於 solutions/1114405056/ 目錄下執行
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 資料結構選擇理由

- **Task 1**：使用 `set` 做已見元素的 O(1) 查詢，搭配 `list` 保留順序；`sorted()` 依題意維持穩定排序語意。
- **Task 2**：直接使用 `sorted(..., key=lambda ...)`，以 tuple 的字典序作為多鍵比較，避免手刻比較邏輯，排序穩定且可讀。
- **Task 3**：`defaultdict(int)` 讓計數器不需初始化；`Counter.most_common(1)` 可直接取最大值，與手動 `max()` 相比更語意清晰。

---

## 遇到的一個錯誤與修正

**問題**：Task 1 初稿直接用 `list(set(nums))` 去重，導致順序不固定，測試
`test_normal_case` 偶爾失敗。

**修正**：改為逐元素遍歷，搭配輔助 `set` 記錄已出現過的元素，確保輸出順序與
第一次出現的位置一致。

---

## Red → Green → Refactor 摘要

### Task 1

- **Red**：先寫 `test_normal_case`，執行後 `dedupe_ordered` 尚未實作，得到
  `AttributeError`，確認失敗。
- **Green**：完成 `dedupe_ordered`（遍歷 + set）、`sort_asc/desc`、
  `filter_evens` 的最小實作，所有 Task 1 測試通過。
- **Refactor**：將四個函式分開命名並加上型別提示；`sequence_clean` 負責 I/O，
  邏輯函式保持純粹（無副作用），方便測試。

### Task 2

- **Red**：先寫 `test_tie_break_by_age`，在 `rank_students` 只依 `score` 降序
  排列而未處理次要鍵時失敗。
- **Green**：`key=lambda s: (-s[1], s[2], s[0])` 一行解決三鍵排序，測試全過。
- **Refactor**：拆出 `parse_students` 函式，讓 `student_ranking` 職責單一；
  型別提示讓呼叫端一眼看出資料結構。

### Task 3

- **Red**：先寫 `test_empty_input`，未處理 `m=0` 時 `Counter.most_common(1)[0]`
  拋出 `IndexError`，確認失敗。
- **Green**：在函式開頭加 `if m == 0` 的早返回分支，輸出 `(none) 0`，測試通過。
- **Refactor**：將 `defaultdict` 計數與 `Counter` 分開職責（前者追蹤 user，後者
  追蹤 action），提高可讀性；排序邏輯同樣收進一行 `sorted(..., key=...)`。
