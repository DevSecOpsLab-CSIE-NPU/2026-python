# TEST_LOG

## Red

- 執行指令

```powershell
cd weeks/week-03/week3-HW-1114405040
..\..\..\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

- 測試總數：2
- 通過數：0
- 失敗數：2
- 失敗摘要：`test_robot_core` 與 `test_robot_scent` 都因 `ModuleNotFoundError: No module named 'robot_core'` 無法載入
- 從失敗到通過做了哪些修改：建立 `robot_core.py`，補上 `Robot`、`World`、單步命令執行與 scent 規則；之後再把測試路徑與狀態回傳格式對齊。

## Green

- 執行指令

```powershell
cd weeks/week-03/week3-HW-1114405040
..\..\..\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

- 測試總數：13
- 通過數：13
- 失敗數：0
- 摘要：旋轉、邊界越界、LOST、scent 與非法指令處理皆通過
- 從失敗到通過做了哪些修改：把核心邏輯從畫面程式分離到 `robot_core.py`，再補上 `World.clear_scents()` 與多指令執行流程，使兩份測試都能完整驗證。