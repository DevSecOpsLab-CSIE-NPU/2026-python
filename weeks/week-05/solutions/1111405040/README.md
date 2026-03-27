# Week 05 Game Design

## 作業主題

以 `week-05/game_design` 的六個階段需求為基礎，完成一個可執行的 Big Two 遊戲。

本次實作重點如下：

1. 先寫測試，再補實作。
2. 將遊戲拆成 `models`、`classifier`、`finder`、`ai`、`game`、`ui` 六個模組。
3. 讓 `main.py` 可以從發牌一路跑到產生贏家。
4. 若本機有安裝 `pygame`，可使用 GUI 模式；未安裝時則自動改用 CLI 模式。

---

## 檔案結構

```text
weeks/week-05/solutions/1111405040/
├─ .gitignore
├─ README.md
├─ TEST_CASES.md
├─ TEST_LOG.md
├─ AI_USAGE.md
└─ bigtwo/
   ├─ game/
   │  ├─ models.py
   │  ├─ classifier.py
   │  ├─ finder.py
   │  ├─ ai.py
   │  └─ game.py
   ├─ ui/
   │  ├─ render.py
   │  ├─ input.py
   │  └─ app.py
   ├─ tests/
   │  ├─ test_models.py
   │  ├─ test_classifier.py
   │  ├─ test_finder.py
   │  ├─ test_ai.py
   │  ├─ test_game.py
   │  └─ test_ui.py
   └─ main.py
```

---

## 完成內容

### 1. Phase 1 - 資料模型

- `Card`：牌面、花色、比較與字串表示。
- `Deck`：建立 52 張牌、洗牌、發牌。
- `Hand`：排序、找出梅花 3、移除手牌。
- `Player`：拿牌與出牌。

### 2. Phase 2 - 牌型判斷

- 實作 `CardType`。
- 辨識單張、對子、三條、順子、同花、葫蘆、四條、同花順。
- 支援 `A-2-3-4-5` 特例。
- 提供牌型比較與是否可出的規則判斷。

### 3. Phase 3 - 可出牌搜尋

- 從手牌找出所有單張、對子、三條與五張牌型。
- 依目前牌桌狀態篩出有效出牌。
- 首回合只允許包含梅花 3 的出牌。

### 4. Phase 4 - AI 策略

- 以牌型、點數、花色與剩餘手牌數做評分。
- 支援首回合優先處理梅花 3。
- 可從有效出牌中挑出較合理的一手。

### 5. Phase 5 - 遊戲流程

- 建立四位玩家，其中一位為人類、三位為 AI。
- 發牌後由持有梅花 3 的玩家先手。
- 支援出牌、pass、三家連續 pass 後重置牌桌。
- 能判斷勝者並結束遊戲。

### 6. Phase 6 - UI 與整合

- `Renderer`：提供卡牌與手牌的繪製介面。
- `InputHandler`：管理選牌與按鈕邏輯。
- `BigTwoApp`：整合遊戲邏輯與執行流程。
- `main.py`：啟動遊戲。

---

## 執行方式

### 方法 1：執行全部測試

```powershell
cd weeks/week-05/solutions/1111405040/bigtwo
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 方法 2：執行單一模組測試

```powershell
cd weeks/week-05/solutions/1111405040/bigtwo

# models
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_models -v

# classifier
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_classifier -v

# finder
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_finder -v

# ai
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_ai -v

# game
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_game -v

# ui
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_ui -v
```

### 方法 3：執行遊戲

```powershell
cd weeks/week-05/solutions/1111405040/bigtwo
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe main.py
```

---

## 依賴套件

- 必要套件：無
- 可選套件：`pygame`

說明：

1. 未安裝 `pygame` 時，程式會改用 CLI 模式執行。
2. 若有安裝 `pygame`，`BigTwoApp` 會使用 GUI 模式。

---

## 驗證結果

1. 共撰寫 6 份測試檔。
2. 共 52 個測試案例，全部通過。
3. `main.py` 已實際執行，可從發牌一路跑到產生贏家。
