# Phase 6: GUI - 開發設計

## 目標

實作 Pygame GUI，提供完整的遊戲介面。

## 檔案結構

```
bigtwo/
├── ui/
│   ├── __init__.py
│   ├── render.py    # 渲染器
│   ├── input.py    # 輸入處理
│   └── app.py      # 主應用
└── main.py          # 入口
```

---

## 1. render.py - 渲染器

```
類別：Renderer

屬性：
  COLORS = {
    background: (45,45,45)
    card_back: (74,144,217)
    spade_club: (255,255,255)
    heart_diamond: (231,76,60)
    player: (46,204,113)
    ai: (149,165,166)
    selected: (241,196,15)
    button: (52,152,219)
  }
  
  CARD_WIDTH = 60
  CARD_HEIGHT = 90

方法：
  draw_card(card, x, y, selected=False)
    - 繪製單張牌
    - 數字/花色顏色處理
    
  draw_hand(hand, x, y, selected_indices)
    - 繪製手牌（重疊顯示）
    
  draw_player(player, x, y, is_current)
    - 繪製玩家名稱
    
  draw_last_play(cards, player_name, x, y)
    - 繪製上家出牌
    
  draw_buttons(buttons, x, y)
    - 繪製按鈕
```

---

## 2. input.py - 輸入處理

```
類別：InputHandler

屬性：
  renderer: Renderer
  selected_indices: List[int]
  buttons: Dict

方法：
  handle_event(event, game) -> bool
    - 處理事件
    
  handle_click(pos, game) -> bool
    - 處理點擊
    - 檢查按鈕
    - 檢查選牌
    
  handle_key(key, game) -> bool
    - 處理鍵盤
    - Enter: 出牌
    - P: 過牌
    
  try_play(game) -> bool
    - 嘗試出牌
```

---

## 3. app.py - 主應用

```
類別：BigTwoApp

屬性：
  screen: pygame.Surface
  renderer: Renderer
  input_handler: InputHandler
  game: BigTwoGame
  buttons: Dict

方法：
  __init__()
    - 初始化pygame
    - 建立遊戲
    
  run()
    - 主迴圈
    - handle_events()
    - render()
    - pygame.display.flip()
    
  handle_events()
    - 處理所有事件
    - 遊戲結束時跳過
    
  render()
    - 背景
    - 所有玩家（AI顯示背面）
    - 人類玩家手牌
    - 上家出牌
    - 按鈕
    - 遊戲結束訊息
```

---

## 4. main.py - 入口

```
from ui.app import BigTwoApp

if __name__ == "__main__":
    app = BigTwoApp()
    app.run()
```

---

## 控制說明

```
滑鼠點擊：選取/取消選取牌
Enter：確認出牌
P：過牌
```

---

## 執行遊戲

```bash
cd bigtwo
pip install pygame
python main.py
```

---

## 重構檢查清單

- [ ] 加入動畫效果
- [ ] 優化牌面設計
- [ ] 加入遊戲記錄
- [ ] 支援鍵盤導航