# TEST_LOG

- 日期：2026-03-16
- 學號：week03-1114405048
- Python：3.14.3
- 測試框架：unittest

---

## Run 1 (Red)
- 執行指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 結果摘要：
  - 測試總數：12
  - 通過：11
  - 失敗：1

- 失敗重點：
  - test_n_plus_l_becomes_w 失敗，AssertionError: 'W' != 'E'

- 從失敗到通過做了哪些修改：
  - 修正測試預期值，將 N + L 的期望由 E 改回 W。

---

## Run 2 (Green)
- 執行指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 結果摘要：
  - 測試總數：12
  - 通過：12
  - 失敗：0

- 修改說明：
  - 只調整測試案例預期值，核心邏輯維持不變。
  - 驗證旋轉、越界、scent、LOST 停止與非法指令策略均符合規格。
