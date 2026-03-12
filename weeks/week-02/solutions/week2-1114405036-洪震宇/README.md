# Week 02 作業 (Student: yehallen)

本資料夾包含 Week-02 的三個題目實作，以及對應的測試與說明檔。

## 結構

- `task1_sequence_clean.py`：實作序列清理與排序
- `task2_student_ranking.py`：實作學生排名輸出
- `task3_log_summary.py`：實作日誌統計輸出
- `tests/`：對應的 `unittest` 測試
- `TEST_CASES.md`：測試案例說明
- `TEST_LOG.md`：測試執行紀錄（Red / Green）
- `AI_USAGE.md`：AI 使用紀錄

## 執行測試

在此資料夾中，執行：
 
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```


## 執行各題目範例

### Task 1

```bash
echo "5 3 5 2 9 2 8 3 1" | python task1_sequence_clean.py
```

### Task 2

```bash
cat <<'EOF' | python task2_student_ranking.py
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
EOF
```

### Task 3

```bash
cat <<'EOF' | python task3_log_summary.py
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
