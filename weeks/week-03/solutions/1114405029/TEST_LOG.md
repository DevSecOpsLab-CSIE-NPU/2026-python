# TEST_LOG

## 1. Red - 初次測試失敗

執行指令：

python -m unittest discover -s weeks/week-03/solutions/1114405029/tests -p "test_*.py" -v

測試總數：1  
通過數：0  
失敗數：1  

失敗原因：

最初執行測試時，Python 無法找到 `robot_core.py`，出現錯誤：

ModuleNotFoundError: No module named 'robot_core'

之後修正 import 路徑後，又出現：

ImportError: cannot import name 'Robot' from 'robot_core'

經檢查後發現 `robot_core.py` 檔案內容為空，因此測試無法載入 `Robot` 類別與相關函式。

修改內容：

- 在測試檔加入

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

讓測試可以找到 `robot_core.py`。

- 重新實作 `robot_core.py`，加入以下核心邏輯：

  - `Robot` 類別
  - `turn_left`
  - `turn_right`
  - `forward_position`
  - `is_out_of_bounds`
  - `execute_instruction`
  - `execute_commands`

完成後重新執行測試。

---

## 2. Green - 測試全部通過

執行指令：

python -m unittest discover -s weeks/week-03/solutions/1114405029/tests -p "test_*.py" -v

測試總數：20
通過數：20
失敗數：0

執行結果：

Ran 20 tests

OK

測試覆蓋內容：

- 方向旋轉測試  
  - `N + L = W`
  - `N + R = E`
  - 連續四次右轉回到原方向

- 邊界與 LOST 判定  
  - 機器人在邊界外移動會 LOST
  - 機器人在邊界內移動不會 LOST
  - LOST 後不再執行後續指令

- scent 機制測試  
  - 第一台機器人越界後留下 scent
  - 第二台機器人在相同 `(x, y, dir)` 會忽略危險 `F`
  - 同一格但不同方向不共用 scent
  - scent 只會忽略危險移動並繼續下一指令

結論：

所有測試均通過，核心邏輯（旋轉、越界、LOST、scent）運作正常。