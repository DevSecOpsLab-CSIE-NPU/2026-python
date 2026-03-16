# Week 03 回家作業：Robot Lost（pygame 規則模擬 + 視覺化）

> 依據 Week 01 先備（容器、迴圈、函式）與 Week 02 作業方法（TDD、測試紀錄），結合 Week 03 題型（模擬、字串指令解析）設計。
>
> 本作業核心對應 UVA 118：把文字規則模擬，轉成可互動的 pygame 小遊戲。

---

## 作業目標

- 熟悉 2D 格子座標系與方向運算（N/E/S/W）
- 熟悉狀態機設計（ALIVE / LOST）
- 熟悉集合資料結構在規則記錄上的應用（`scent`）
- 練習把演算法規則做成互動視覺化（pygame）
- 延續 Test-Oriented Development：先測試再實作，再重構

---

## 題目與交付

請在 `weeks/week-03/solutions/<student-id>/` 建立以下檔案：

```text
weeks/week-03/solutions/<student-id>/
├── robot_game.py                 # pygame 主程式（互動畫面）
├── robot_core.py                 # 核心邏輯（不依賴 pygame，便於測試）
├── assets/
│   └── gameplay.png              # 你實際操作遊戲的截圖（必交）
│   └── replay.gif                # play 過程重播檔（建議）
├── tests/
│   ├── test_robot_core.py
│   └── test_robot_scent.py
├── TEST_CASES.md
├── TEST_LOG.md
├── AI_USAGE.md
└── README.md
```

### AI 使用原則（本作業適用）

- 可以使用 AI 協助拆解規格、產生雛形、建議測試案例
- 不可直接貼上 AI 回答後不驗證就提交
- 你必須能口頭解釋：
  - 為什麼 `scent` 要記錄方向
  - 為什麼 LOST 後要停止該機器人
  - 你的測試如何覆蓋旋轉、越界、scent 三大重點

---

## 規格說明（必做）

### 地圖與座標

- 地圖為矩形格子，範圍是 `(0, 0)` 到 `(W, H)`（含邊界）
- 機器人狀態為：`(x, y, dir, lost)`
- 方向僅允許：`N`, `E`, `S`, `W`

建議位移表：

- `N -> (0, +1)`
- `E -> (+1, 0)`
- `S -> (0, -1)`
- `W -> (-1, 0)`

### 指令規則

玩家每次輸入一串指令，字元僅允許：`L`, `R`, `F`

- `L`：原地左轉 90 度
- `R`：原地右轉 90 度
- `F`：朝目前方向前進一格

### LOST 與 scent 規則（核心）

- 若執行 `F` 會走出地圖：
  - 該機器人立刻標記 `LOST`
  - 在「掉落前最後位置 + 當前方向」留下一筆 `scent`
  - 該機器人不再執行後續指令
- 後續機器人若位在相同 `(x, y, dir)`，再次遇到會越界的 `F`：
  - 忽略該指令（不移動、不 LOST）
  - 繼續執行下一個指令

`scent` 建議資料結構：

- `set[tuple[int, int, str]]`
- 例如 `(3, 2, 'E')`

---

## pygame MVP 要求（必做）

至少完成以下互動功能：

- 顯示格子地圖
- 顯示機器人目前位置與朝向（箭頭或三角形皆可）
- 顯示 `scent`（點或圖示皆可）
- 可透過鍵盤輸入 `L/R/F` 執行一步
- 可重置新機器人（保留 `scent`）
- 可清除 `scent`
- 可重播 play 過程（例如：匯出 `replay.gif` 或提供回放機制）

建議操作鍵：

- `L` / `R` / `F`
- `N`：新機器人
- `C`：清除 scent
- `G`：輸出回放 GIF（建議）
- `ESC`：離開

### 遊玩證明截圖（必交）

- 請在 `assets/gameplay.png` 放入你實際遊玩畫面截圖
- 截圖中需同時看得到：地圖、機器人、scent 或狀態資訊（HUD）
- 建議在 README 內嵌圖片：`![gameplay](assets/gameplay.png)`

---

## Test-Oriented Development（本作業必做）

請至少完成 1 次 `Red → Green → Refactor`：

1. **Red**：先寫測試，確認會失敗
2. **Green**：實作最小可行邏輯讓測試通過
3. **Refactor**：重構命名/函式切分，測試仍全綠

### 測試要求

- 測試檔至少 2 份（`test_robot_core.py`, `test_robot_scent.py`）
- 測試函式至少 10 個
- 至少覆蓋以下三大面向：
  - 方向旋轉
  - 越界判定
  - scent 生效
- 建議使用 Python 內建 `unittest`

### 測試執行指令

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 測試執行紀錄（必交）

請在 `TEST_LOG.md` 貼上至少 2 次摘要：

1. 一次 Red（失敗）
2. 一次 Green（全通過）

每次需包含：

- 執行指令
- 測試總數、通過數、失敗數
- 從失敗到通過做了哪些修改（1~2 句）

---

## 最低測試清單（必含）

以下案例至少都要出現在你的測試中：

1. `N + L = W`
2. `N + R = E`
3. 連續 4 次 `R` 回原方向
4. 邊界往外 `F` 會 LOST
5. 邊界內移動不會 LOST
6. 第一台越界後留下 scent
7. 第二台同 `(x,y,dir)` 會忽略危險 `F`
8. 同格但不同方向不該共用 scent
9. LOST 後不再執行後續指令
10. 非法指令（如 `X`）有明確處理策略

---

## README.md 內容要求

![img](imgs/replay.gif)

在 `weeks/week-03/solutions/<student-id>/README.md` 至少包含：

1. 功能清單（你實作了哪些互動功能）
2. 執行方式（Python 版本、安裝 pygame、啟動遊戲）
3. 測試方式（測試指令與結果摘要）
4. 你的資料結構選擇理由（至少 3 點）
5. 你踩到的一個 bug 與修正方式
6. 內嵌遊玩截圖（`assets/gameplay.png`）
7. 重播方式說明（如何產生與檢視 `assets/replay.gif` 或等效回放）

---

## TEST_CASES.md 內容要求

至少 8 組你自行設計的測資，需包含：

1. 正常情況
2. 邊界情況
3. 反例（容易寫錯）
4. scent 方向差異情況
5. LOST 後仍有後續指令的情況

每組請寫：

- 輸入（初始狀態 + 指令）
- 預期結果
- 實際結果
- PASS/FAIL
- 對應測試函式名稱

---

## AI_USAGE.md 內容要求

請記錄：

1. 你問 AI 的 3~5 個問題
2. 你採用的建議與原因
3. 你拒絕的建議與原因
4. 至少 1 個 AI 建議不完整、你自行修正的案例

---

## 評分標準（100 分）

- 規則正確性（L/R/F、LOST、scent）：40 分
- 測試完整度（數量與覆蓋面）：30 分
- 程式結構與可讀性（模組分離、命名、註解）：20 分
- 互動與視覺呈現（pygame MVP 完整度）：10 分

### 加分項目（最多 +10 分）

- 中文呈現完整（介面文字、狀態訊息、操作提示具一致性）：+5 分
- 額外提供 10x10 字串矩陣呈現，且可觀察容器狀態（如 `scent` 內容或矩陣快照）：+5 分

扣分項目：

- 測試函式少於 10 個：-10 分
- 缺 `TEST_LOG.md`：-10 分
- 缺 `AI_USAGE.md`：-10 分
- 缺 `assets/gameplay.png` 或 README 未內嵌截圖：-10 分
- 無法執行（程式或測試）：-10 分
- `robot_core.py` 與畫面邏輯高度耦合、難以測試：-10 分

---

## 提交規範（沿用課程規則）

- 分支：`submit/week-03`
- PR 標題：`Week 03 - <student-id> - <name>`
- 僅允許提交路徑：`weeks/week-03/solutions/<student-id>/`

參考：

- `weeks/week-02/GITHUB_WORKFLOW.md`
- `docs/SUBMISSION_GUIDE.md`
