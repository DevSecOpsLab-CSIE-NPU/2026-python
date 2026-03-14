# AI_USAGE

## 我向 GitHub Copilot 詢問的問題

1. Robot Lost 的核心資料結構應該如何設計，才能清楚表示機器人的狀態？
2. scent 為什麼需要同時記錄 `(x, y, direction)`，而不是只記錄位置？
3. 如何將 Robot Lost 的規則拆成多個函式，讓程式更容易測試？
4. 在 Python 中要如何使用 `unittest` 設計測試，來覆蓋旋轉、越界、LOST、scent 等情況？
5. 如何設計演算法，使時間複雜度與空間複雜度保持在合理且有效率的範圍？

---

## 我採用的 Copilot 建議與原因

### 1. 使用 `dataclass` 表示 Robot 狀態

我使用 `Robot(x, y, direction, lost)` 來表示機器人的狀態。  
這樣可以讓資料結構更清楚，也讓程式碼更容易閱讀與維護。

使用 `dataclass` 的好處是：

- 可以自動產生 `__init__`
- 程式結構更清楚
- 在測試時建立物件比較方便

---

### 2. 使用 `set` 儲存 scent

我使用：

set[tuple[int, int, str]]

來儲存 scent，例如：

(3, 2, "E")

使用 `set` 的原因：

- 查找時間複雜度為 **O(1)**
- 適合用來快速判斷某個 scent 是否存在
- 結構簡單且效率高

這樣在每次檢查 scent 時都可以快速完成判斷。

---

### 3. 將核心邏輯與畫面程式分離

我將程式分成兩個模組：

robot_core.py  
robot_game.py

`robot_core.py` 負責：

- 機器人移動
- 方向旋轉
- 邊界判定
- scent
- LOST

`robot_game.py` 負責：

- pygame 畫面
- 鍵盤操作
- 顯示機器人位置

這樣的設計讓核心邏輯可以單獨測試，也讓程式結構更清楚。

---

### 4. 使用多個函式拆分邏輯

我將功能拆分為多個小函式，例如：

turn_left()  
turn_right()  
forward_position()  
is_out_of_bounds()  
execute_instruction()  
execute_commands()

這樣每個函式只負責一個功能，程式會更容易閱讀，也更方便測試與除錯。

---

## 我沒有採用的 Copilot 建議與原因

### 1. 將所有邏輯寫在 pygame 主程式中

Copilot 曾建議將機器人的移動邏輯直接寫在 `robot_game.py` 中。

我沒有採用這個做法，原因是：

- 會讓畫面程式與邏輯高度耦合
- 不利於單元測試
- 程式會變得比較難維護

因此我將核心邏輯獨立在 `robot_core.py`。

---

### 2. 只用 `(x, y)` 記錄 scent

Copilot 曾建議只用 `(x, y)` 記錄 scent。

我沒有採用這個做法，因為：

- 同一個位置不同方向可能會有不同結果
- 題目規則要求 scent 必須包含方向
- 如果只記錄位置，可能會造成判斷錯誤

因此我使用 `(x, y, direction)` 來記錄 scent。

---

## Copilot 建議不完整，我自行修正的案例

Copilot 在最初提供測試範例時，直接使用：

from robot_core import ...

但在專案根目錄執行 `unittest discover` 時，Python 找不到 `robot_core.py`，導致測試失敗。

因此我在測試檔開頭加入：

import os  
import sys  
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

讓測試程式可以正確找到 `robot_core.py`。

---

## 我的心得

在這次作業中，我利用 GitHub Copilot 協助理解題目與產生程式雛形，但仍然需要自己理解題目的規則並調整程式。

透過實作與測試，我更理解了：

- scent 為什麼需要記錄方向
- 為什麼機器人 LOST 後必須停止執行
- 如何利用單元測試驗證程式邏輯
- 如何選擇合適的資料結構來提升效率

這次作業也讓我更熟悉如何將程式邏輯拆分為多個模組，使程式更容易維護與測試。