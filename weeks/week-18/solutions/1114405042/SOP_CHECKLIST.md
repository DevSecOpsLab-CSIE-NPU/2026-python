# 期末考 SOP 檢查表

> 學生：1114405042 | D=4
> - Q1: Week 02（Sequence Clean / Student Ranking / Log Summary）
> - Q2: Caesar Cipher SHIFT=3

## Step 2：Test Case 拆解

| 題目 | Test Case | Edge? |
|------|-----------|-------|
| Q1-T1 | 正常輸入 | |
| Q1-T1 | 全部相同 | ✅ |
| Q1-T1 | 單一元素 | ✅ |
| Q1-T1 | 空輸入 | ✅ |
| Q1-T1 | 負數 | |
| Q1-T2 | 正常 6 筆取 3 名 | |
| Q1-T2 | 同分比 age | ✅ |
| Q1-T2 | 同年齡比 name | ✅ |
| Q1-T2 | k < n | |
| Q1-T2 | k > n | ✅ |
| Q1-T3 | 正常 8 筆記錄 | |
| Q1-T3 | 空輸入 m=0 | ✅ |
| Q1-T3 | 單一使用者 | ✅ |
| Q1-T3 | 同次數依名稱 | ✅ |
| Q2 | Hello, NPU! 範例 | |
| Q2 | abc XYZ wraparound | |
| Q2 | xyz→abc wraparound | ✅ |
| Q2 | XYZ→ABC wraparound | ✅ |
| Q2 | 非字母不變 | ✅ |
| Q2 | 空字串 | ✅ |

## Step 3 → Step 4：Red → Green 摘要

| 題目 | 測試數 | Red | Green |
|------|--------|-----|-------|
| Q1 | 16 | ❌ 0/16 | ✅ 16/16 |
| Q2 | 9 | ❌ 0/9 | ✅ 9/9 |

## 自我檢測
- [✔] 分支命名：`submit/week-XX`
- [✔] commit 前綴：Red → `test:` / Green → `feat:`
- [✔] 紅燈 → 綠燈順序不可反
