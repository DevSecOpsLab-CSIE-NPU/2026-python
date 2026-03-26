# Big Two Game - 完整项目提交

## 学号：1114405028
## 提交日期：2026-03-26

---

## 📋 项目概览

完整实现一个 **Big Two（大贰/两王）** 卡牌游戏，包含从数据模型到游戏逻辑的所有组件。

### 🎯 实现范围

| Phase | 模块 | 类别 | 文件 | 测试套件 | 状态 |
|-------|-----|------|------|----------|------|
| 1 | models | Card, Deck, Hand, Player | models.py | test_models.py | ✅ 完成 |
| 2 | classifier | CardType, HandClassifier | classifier.py | test_classifier.py | ✅ 完成 |
| 3 | finder | HandFinder | finder.py | test_finder.py | ✅ 完成 |
| 4 | ai | AIStrategy | ai.py | test_ai.py | ✅ 完成 |
| 5 | game | BigTwoGame | game.py | test_game.py | ✅ 完成 |

---

## 📊 测试统计

### 总体结果

```
✅ 总测试数：94
✅ 通过：94
❌ 失败：0
⏱️ 执行时间：0.002s
📈 成功率：100%
```

### 按 Phase 分布

| Phase | 测试套件 | 测试数 | 状态 |
|-------|---------|--------|------|
| Phase 1 (Models) | test_models.py | 29 | ✅ |
| Phase 2 (Classifier) | test_classifier.py | 23 | ✅ |
| Phase 3 (Finder) | test_finder.py | 14 | ✅ |
| Phase 4 (AI) | test_ai.py | 16 | ✅ |
| Phase 5 (Game) | test_game.py | 12 | ✅ |

---

## 📦 文件结构

```
1114405028/
├── game/
│   ├── __init__.py           # 模块初始化
│   ├── models.py             # Phase 1: 数据模型 (Card, Deck, Hand, Player)
│   ├── classifier.py         # Phase 2: 牌型分类 (CardType, HandClassifier)
│   ├── finder.py             # Phase 3: 牌型搜索 (HandFinder)
│   ├── ai.py                 # Phase 4: AI 策略 (AIStrategy)
│   └── game.py               # Phase 5: 游戏流程 (BigTwoGame)
├── tests/
│   ├── __init__.py
│   ├── test_models.py        # Phase 1 测试 (29 个)
│   ├── test_classifier.py    # Phase 2 测试 (23 个)
│   ├── test_finder.py        # Phase 3 测试 (14 个)
│   ├── test_ai.py            # Phase 4 测试 (16 个)
│   └── test_game.py          # Phase 5 测试 (12 个)
├── README.md                 # Phase 1 说明
├── SUBMISSION_CHECKLIST.md   # Phase 1 清单
└── PHASES_2_5_SUMMARY.md    # 本文件
```

---

## 🎮 功能清单

### Phase 1: 数据模型

**Card 类别** (10 个测试)
- ✅ 初始化、表示、比较、排序
- ✅ 支持所有比较运算符
- ✅ 哈希值支持 set/dict

**Deck 类别** (8 个测试)
- ✅ 初始化 52 张牌
- ✅ 洗牌功能
- ✅ 发牌功能（含超额保护）

**Hand 类别** (7 个测试)
- ✅ 继承 list，支持迭代
- ✅ 倒序排列
- ✅ 查找梅花三
- ✅ 安全移除牌

**Player 类别** (4 个测试)
- ✅ 玩家初始化
- ✅ 拿牌、出牌

### Phase 2: 牌型分类

**CardType 枚举** (1 个测试)
- ✅ 8 种牌型：单张、对子、三条、顺子、同花、葫芦、四条、同花顺

**HandClassifier 静态方法** (22 个测试)
- ✅ `_is_straight()` - 检查顺子
- ✅ `_is_flush()` - 检查同花
- ✅ `classify()` - 分类牌型
- ✅ `compare()` - 比较两手牌
- ✅ `can_play()` - 检查合法性

### Phase 3: 牌型搜索

**HandFinder 静态方法** (14 个测试)
- ✅ `find_singles()` - 所有单张
- ✅ `find_pairs()` - 所有对子
- ✅ `find_triples()` - 所有三条
- ✅ `find_fives()` - 所有五张牌型
- ✅ `get_all_valid_plays()` - 合法出牌

### Phase 4: AI 策略

**AIStrategy 静态方法** (16 个测试)
- ✅ `score_play()` - 评估出牌分数
- ✅ `select_best()` - 选择最佳出牌
- ✅ 贪心算法实现
- ✅ 评分公式：牌型 × 100 + 牌值 × 10 + 奖励

### Phase 5: 游戏流程

**BigTwoGame 类别** (12 个测试)
- ✅ `setup()` - 游戏初始化
- ✅ `play()` - 玩家出牌
- ✅ `pass_()` - 玩家过牌
- ✅ `next_turn()` - 轮转
- ✅ `check_winner()` - 检测获胜者
- ✅ `ai_turn()` - AI 自动回合

---

## 🔧 核心算法

### 牌型识别

```
5张牌分类优先级：
1. 同花顺 (STRAIGHT_FLUSH) = 顺子 + 同花
2. 四条 (FOUR_OF_A_KIND) = 4张相同
3. 葫芦 (FULL_HOUSE) = 3张 + 2张对
4. 同花 (FLUSH) = 5张同花
5. 顺子 (STRAIGHT) = 5张连续
```

### 顺子识别

```
特殊情况：A-2-3-4-5
- 检查 set 是否为 {14, 15, 3, 4, 5}
- 最大点数为 5

正常情况：
- 检查连续性：rank[i] = rank[i-1] + 1
```

### AI 贪心策略

```
评分 = 牌型分数 × 100 + 牌值分数 × 10 + 奖励

奖励：
- 剩1张：+10000
- 剩≤3张：+500
- 黑桃牌：+5/张
```

---

## 🚀 快速开始

### 运行测试

```bash
cd 1114405028
python -m unittest discover -s tests -p "test_*.py" -v
```

### 使用示例

```python
from game.models import Card, Deck, Hand, Player
from game.classifier import HandClassifier
from game.finder import HandFinder
from game.ai import AIStrategy
from game.game import BigTwoGame

# 创建游戏
game = BigTwoGame(num_human=1)
game.setup()

# 获取当前玩家
player = game.get_current_player()

# 查找可出的牌
valid_plays = HandFinder.get_all_valid_plays(
    player.hand, 
    game.last_play[0] if game.last_play else None
)

# AI 选择最佳出牌
if player.is_ai:
    best = AIStrategy.select_best(valid_plays, player.hand)
    if best:
        game.play(player, best)
    else:
        game.pass_(player)
```

---

## 📈 代码品质

- ✅ 完整的类型注解 (Type Hints)
- ✅ 詳細的文档字符串 (Docstrings)
- ✅ 中文注释清晰易懂
- ✅ PEP 8 命名规范遵循
- ✅ 无语法错误和警告
- ✅ 94/94 测试通过

---

## 🎓 设计模式

| 模式 | 应用 |
|------|------|
| **静态方法** | HandClassifier、HandFinder、AIStrategy |
| **枚举** | CardType (IntEnum) |
| **继承** | Hand (list) |
| **组合** | Game 包含 Deck、Player、Hand |
| **策略模式** | AIStrategy 提供不同的评分策略 |

---

## 🔍 关键实现细节

### 花色顺序
```
♠ (Spade) > ♥ (Heart) > ♦ (Diamond) > ♣ (Club)
0 = ♣, 1 = ♦, 2 = ♥, 3 = ♠
```

### 点数顺序
```
3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < J < Q < K < A < 2
rank: 3-14 (A=14), 15 (2=15)
```

### 对子强度等级
```
对2 > 对A > 对K > ... > 对3
```

---

## ✨ 特色功能

1. **完整的牌型系统** - 支持所有 8 种标准牌型
2. **智能 AI** - 贪心算法选择最优出牌
3. **安全的游戏流程** - 完善的合法性检查
4. **高效的搜索** - 使用 combinations 库优化
5. **可扩展设计** - 易于添加新功能

---

## 📝 持续改进方向

- [ ] 添加游戏记录和回放功能
- [ ] 支持暂停/恢复功能
- [ ] 实现计分系统
- [ ] 优化 AI 策略（考虑对手牌）
- [ ] 添加 GUI 界面 (Pygame)
- [ ] 网络对战支持
- [ ] 数据统计和分析

---

## 提交声明

本项目为原创实现，遵循所有编码规范和最佳实践。所有 94 个单元测试均已通过，代码经过完整的文档化和注释。

**提交者**：1114405028  
**项目版本**：1.0 (Phase 1-5 完成)  
**完成度**：100%

---

*最后更新：2026-03-26*
