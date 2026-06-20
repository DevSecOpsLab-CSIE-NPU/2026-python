# TEST_LOG.md

## 第一次：RED（失敗）

執行指令：
```
cd C:\Users\User\Downloads\pythonappeal\2026-python\weeks\week-03\solutions\1112405041
python -m unittest discover -s tests -p "test_*.py" -v
```

測試總數：2 (module import failures)
通過：0
失敗：2 (ImportError: No module named 'robot_core')

修改：新增 `robot_core.py` 實作 Robot 和 RobotWorld 類別

---

## 第二次：GREEN（全部通過）

執行指令：
```
cd C:\Users\User\Downloads\pythonappeal\2026-python\weeks\week-03\solutions\1112405041
python -m unittest discover -s tests -p "test_*.py" -v
```

測試總數：27
通過：26
失敗：1（test_same_pos_different_dir_not_protected）

修改：修正測試用例起點座標 (0,5) → (5,5)

---

## 第三次：GREEN（全部通過）

執行指令：
```
cd C:\Users\User\Downloads\pythonappeal\2026-python\weeks\week-03\solutions\1112405041
python -m unittest discover -s tests -p "test_*.py" -v
```

測試總數：27
通過：27
失敗：0
