# Pull Request 說明文件

*   **PR 標題：** `Week 14 - 1114405035 - 戴言廷`
*   **分支名稱：** `submit/week-14-1114405035`
*   **提交路徑：** `weeks/week-14/solutions/1114405035/`

---

## 1. 說明 (Description)

本 PR 已完成 Week 14（綜合練習）的所有要求。

完成了 4 題 CPE 演算法解題，包含：
1.  **11349 (Symmetric Matrix)** - 中心對稱矩陣檢驗與非負值判斷。
2.  **11417 (GCD)** - 計算 1 <= i < j <= N 所有數對的 GCD 總和。
3.  **11461 (Square Numbers)** - 計算閉區間 [a, b] 內的完全平方數個數。
4.  **12019 (Doom's Day Algorithm)** - 推算 2011 年特定月份日期的星期幾。

每題均提供：
*   AI 協助的簡單版（有中文詳細註解）檔案：`*-easy.py`
*   手寫標準版檔案：`*.py`
*   單元測試：`tests/test_*.py`
*   測試 LOG 日誌：`tests/test_*.log`

---

## 2. 測試驗證 (Verification)

已執行 `python -m unittest discover -s tests -p "test_*.py" -v`，所有 4 個單元測試均全數通過（OK）。

```text
test_sample_case (test_11349.Test11349.test_sample_case) ... ok
test_sample_case (test_11417.Test11417.test_sample_case) ... ok
test_sample_case (test_11461.Test11461.test_sample_case) ... ok
test_sample_case (test_12019.Test12019.test_sample_case) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.012s

OK
```
