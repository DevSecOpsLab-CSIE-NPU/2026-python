# Test Log

Environment: `/Users/yehallen/Desktop/交作業暫存用/.venv/bin/python`

## Unit Test

```text
Ran 7 tests in 0.000s

OK
```

## TDD / Git SOP Note

本地開發時先依題目設計測試案例，再完成實作並確認測試通過；但本次整理提交前沒有保留「紅燈失敗測試」的獨立 commit，因此 Git 歷史無法完整呈現先紅後綠流程。最後狀態已用單元測試與樣例輸出確認為綠燈。

## Sample Outputs

Q1:

```text
4
NONE
```

Q2:

```text
Khoor, QSX!
def ABC
```

Q3:

```text
0
8
3
```

Q4:

```text
FOUND 112 cmp=25
linear: 0.4927 s
binary: 0.1930 s
=> binary faster
```

**測試說明：**
- 資料集：10,000 個升冪整數 (0 至 9,999)
- 搜尋目標：112
- 時間測量：100,000 次重複執行，使用 `time.perf_counter()`
- 結果：二分搜尋比線性搜尋快 **2.55 倍** (0.4927 / 0.1930)
- 雷達圖已生成到 `assets/radar.png`
