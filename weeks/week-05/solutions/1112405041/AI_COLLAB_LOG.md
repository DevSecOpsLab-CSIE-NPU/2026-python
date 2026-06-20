# AI 協作紀錄 - Big Two 撲克牌（Phases 1-6）

## 使用者提示詞（User Prompts）

```
read week05 game design folder
已放 CLAUDE.md / AGENTS.md 自動啟用開發訪談模式 要用這個模式做 Week 05 game design
請模仿 07 10 13 and 15 16 17
能不能快點p1 - p6 升級快點 給我在30分鐘搞定
還有都給我先讀裡面的內容再開始考
概念就要給我先講再開始考
還有我給你的提示詞 記得寫進該週solution>1112405041> 你自己取名.md
來不及了 你也快速 commit 紅綠燈
```

## 開發訪談模式（開發訪談助教）

### 概念說明（依 Phase）

| Phase | 主題 | 核心概念 |
|-------|------|---------|
| P1 | 資料模型 | Card(rank,suit)、Deck(52張)、Hand(排序/找3♣)、Player(拿牌/出牌) |
| P2 | 牌型分類 | HandClassifier 8種牌型 (單張→同花順)，先比牌型再比rank再比花色 |
| P3 | 牌型搜尋 | HandFinder 用 combinations 找出所有合法出牌組合 |
| P4 | AI策略 | 貪心評分：type×100 + rank×10 + suit + bonus(剩1張+10000) |
| P5 | 遊戲流程 | BigTwoGame 控制4人回合、出牌/過牌/重置、勝利判定 |
| P6 | GUI | Pygame 渲染牌桌 + 滑鼠/鍵盤輸入 + 主迴圈 |

### 概念問答

| 問題 | 答案 |
|------|------|
| Q: Card rank 範圍？A在哪？2在哪？ | 3~15，A=14，2=15（p1-dev.md 已明確定義） |
| Q: 同花順 vs 四條誰大？ | 同花順(CardType=8) > 四條(7)，依 TYPE_SCORES 數字 |
| Q: 順子 A-2-3-4-5 的 rank 組合？ | 14(A),15(2),3,4,5 |

## TDD 紅綠燈 commit 記錄

| Commit | Phase | Type | Hash |
|--------|-------|------|------|
| test: Phase 1 - Card/Deck/Hand/Player tests (RED) | P1 | RED | e4fbacd |
| feat: Phase 1 - Card/Deck/Hand/Player implementation (GREEN) | P1 | GREEN | 22818d3 |
| test: Phase 2 - HandClassifier tests (RED) | P2 | RED | 362e644 |
| feat: Phase 2 - HandClassifier implementation (GREEN) | P2 | GREEN | 33fc40f |
| test: Phase 3 - HandFinder tests (RED) | P3 | RED | 275a54b |
| feat: Phase 3 - HandFinder implementation (GREEN) | P3 | GREEN | 03dca12 |
| test: Phase 4 - AIStrategy tests (RED) | P4 | RED | 87f2386 |
| feat: Phase 4 - AIStrategy implementation (GREEN) | P4 | GREEN | 4c6a835 |
| test: Phase 5 - BigTwoGame tests (RED) | P5 | RED | c752a38 |
| feat: Phase 5 - BigTwoGame implementation (GREEN) | P5 | GREEN | d191a24 |
| test: Phase 6 - GUI tests (RED) + initial GUI implementation | P6 | RED | 907b912 |
| feat: Phase 6 - GUI implementation + tests (GREEN) | P6 | GREEN | c1000f8 |

## 專案結構

```
bigtwo/
├── game/
│   ├── __init__.py
│   ├── models.py        # Card, Deck, Hand, Player
│   ├── classifier.py    # CardType, HandClassifier
│   ├── finder.py        # HandFinder
│   ├── ai.py            # AIStrategy
│   ├── game.py          # BigTwoGame
│   └── ui/
│       ├── __init__.py
│       ├── render.py    # Renderer (pygame)
│       ├── input.py     # InputHandler
│       └── app.py       # BigTwoApp
├── tests/
│   ├── __init__.py
│   ├── test_models.py   # P1 測試 (21 tests)
│   ├── test_classifier.py # P2 測試 (19 tests)
│   ├── test_finder.py   # P3 測試 (10 tests)
│   ├── test_ai.py       # P4 測試 (7 tests)
│   ├── test_game.py     # P5 測試 (11 tests)
│   └── test_ui.py       # P6 測試 (2 tests)
├── main.py              # 入口
└── requirements.txt
```

## 執行方式

```bash
cd bigtwo
pip install pygame
python main.py          # 啟動遊戲
python -m unittest discover -v  # 執行所有測試
```

## 總計：70 tests，全部 PASS
