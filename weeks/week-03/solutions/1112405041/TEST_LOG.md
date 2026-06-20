# 測試記錄

## RED → 缺 robot_core.py

- 跑了 2 個測試都掛，說找不到 module
- 補上 robot_core.py 就綠燈

## 再跑 → 27 過 26

- 有一個 `test_same_pos_different_dir_not_protected` 起點設 (0,5)，不會越界
- 改成 (5,5) 就對了

## 全過

- 27/27 全部 PASS
