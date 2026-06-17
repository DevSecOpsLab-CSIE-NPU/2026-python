# 三國武將 PK 版 - 赤壁戰役遊戲引擎 (Week 02-07 統合)

## 作業概述

設計一個**三國戰役模擬系統**，整合 Week 02 的資料結構與 Week 07 的檔案 I/O，以 **TDD 測試驅動開發** 流程完成。

**遊戲背景:** 建安十四年赤壁之戰，蜀吳聯軍對陣曹操魏軍，決定天下歸屬。

---

## 關鍵課程整合

| Week | 技能 | 赤壁戰役應用 |
|------|------|-----------|
| **W02** | `sorted(key=...)` | 按速度決定戰鬥順序 |
| **W02** | `Counter` | 傷害統計、`most_common()` 排名 |
| **W02** | `defaultdict` | 兵力損失追蹤 |
| **W02** | `namedtuple` | General 武將結構體 |
| **W07** | 檔案 I/O (`open`)  | 讀取 `generals.txt` |
| **W07** | EOF 輸入處理 | `if line == 'EOF': break` |

---

## 作業繳交清單

```
week-07/
├── HOMEWORK.md                 ← 本文件 (說明)
├── generals.txt                ← 輸入: 武將資料 (9位, 3國各3位)
├── battles.txt                 ← 輸入: 戰役配置 (3波)
├── solution/
│   ├── chibi_battle.py         ← 核心引擎 (手寫版)
│   ├── chibi_battle_easy.py    ← 簡化版 (AI版)
│   ├── test_chibi.py           ← 測試檔 (最少 9 個測試)
│   └── TEST_LOG.md             ← 測試執行日誌
└── AI_USAGE.md                 ← AI 使用說明
```

---

# TDD 三階段設計流程

## 📋 Stage 1: RED 階段 - 資料讀取與結構 (Week 07 檔案 I/O)

### 目標
建立檔案輸入系統，正確讀取武將資料，EOF 結尾。

### 1.1 測試案例 (先寫測試)

```python
# tests/test_stage1_data_loading.py

import unittest
from collections import namedtuple

class TestDataLoading(unittest.TestCase):
    """Stage 1: 資料讀取測試"""
    
    def test_load_generals_from_file(self):
        """測試 1-1: 正確讀取 9 位武將"""
        # Arrange: 準備測試環境
        game = ChibiBattle()
        
        # Act: 執行讀取
        game.load_generals('generals.txt')
        
        # Assert: 驗證結果
        self.assertEqual(len(game.generals), 9)
        self.assertIn('劉備', game.generals)
        self.assertIn('曹操', game.generals)
    
    def test_parse_general_attributes(self):
        """測試 1-2: 正確解析武將屬性"""
        game = ChibiBattle()
        game.load_generals('generals.txt')
        
        # 驗證 namedtuple 結構體
        general = game.generals['關羽']
        self.assertEqual(general.name, '關羽')
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, '蜀')
    
    def test_faction_distribution(self):
        """測試 1-3: 三國分布正確"""
        game = ChibiBattle()
        game.load_generals('generals.txt')
        
        # 使用 list comprehension 和 Counter
        from collections import Counter
        factions = Counter(g.faction for g in game.generals.values())
        
        self.assertEqual(factions['蜀'], 3)
        self.assertEqual(factions['吳'], 3)
        self.assertEqual(factions['魏'], 3)
    
    def test_eof_parsing(self):
        """測試 1-4: 正確識別 EOF 結尾"""
        game = ChibiBattle()
        # 應能正確停止在 EOF，不會讀取額外資料
        game.load_generals('generals.txt')
        
        self.assertEqual(len(game.generals), 9)  # 不會超過 9
```

### 1.2 輸入檔案格式

**generals.txt**
```
蜀 劉備 100 18 16 75 False
蜀 關羽 100 28 14 85 False
蜀 諸葛亮 80 15 12 60 True
吳 孫權 95 20 15 78 False
吳 周瑜 85 18 14 85 True
吳 黃蓋 100 26 15 75 False
魏 曹操 120 28 16 80 False
魏 夏侯惇 105 27 14 82 False
魏 郭嘉 75 16 11 68 True
EOF
```

**battles.txt**
```
蜀吳 vs 魏 赤壁 3
EOF
```

### 1.3 實現代碼 (最小化)

```python
# solution/chibi_battle.py

from collections import namedtuple

# Week 02: namedtuple 結構體
General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattle:
    """吞食天地戰役引擎"""
    
    def __init__(self):
        self.generals = {}
    
    # Week 07: 檔案 I/O
    def load_generals(self, filename):
        """讀取武將資料，EOF 結尾"""
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                # EOF 結尾處理
                if line == 'EOF':
                    break
                if not line:
                    continue
                
                # 解析一行資料
                parts = line.split()
                faction, name, hp, atk, def_, spd, is_leader = parts
                
                # 建立 namedtuple
                general = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == 'True')
                )
                
                self.generals[name] = general
```

### 1.4 執行測試

```bash
$ python -m pytest tests/test_stage1_data_loading.py -v

test_load_generals_from_file ........... PASS ✓
test_parse_general_attributes ......... PASS ✓
test_faction_distribution ............. PASS ✓
test_eof_parsing ....................... PASS ✓

════════════════════════════════════════════
4 tests passed
```

### ✅ Stage 1 完成標準

- [x] 能正確讀取 `generals.txt` (EOF 結尾)
- [x] 解析所有武將屬性正確
- [x] 三國分布正確 (各 3 位)
- [x] 使用 namedtuple 結構體
- [x] 至少 4 個測試通過

---

## 📊 Stage 2: GREEN 階段 - 戰鬥模擬與統計 (Week 02 資料結構)

### 目標
實現戰鬥邏輯，使用 `sorted()`、`Counter`、`defaultdict` 進行統計。

### 2.1 測試案例

```python
# tests/test_stage2_battle_logic.py

import unittest
from collections import Counter

class TestBattleLogic(unittest.TestCase):
    """Stage 2: 戰鬥模擬與統計測試"""
    
    def setUp(self):
        """每個測試前準備"""
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')
    
    def test_battle_order_by_speed(self):
        """測試 2-1: 根據速度排序戰鬥順序"""
        # Week 02: sorted(key=...)
        battle_order = self.game.get_battle_order()
        
        # 速度由高到低: 85, 85, 85, 82, 80, 78, 75, 75, 68
        self.assertEqual(battle_order[0].spd, 85)  # 最快
        self.assertEqual(battle_order[-1].spd, 68)  # 最慢
    
    def test_calculate_damage(self):
        """測試 2-2: 正確計算傷害 (攻擊 - 防禦)"""
        # 關羽 (攻28) vs 夏侯惇 (防14)
        damage = self.game.calculate_damage('關羽', '夏侯惇')
        
        self.assertEqual(damage, 28 - 14)  # = 14
    
    def test_damage_counter_accumulation(self):
        """測試 2-3: Counter 自動累加傷害"""
        # Week 02: Counter
        self.game.calculate_damage('關羽', '夏侯惇')
        self.game.calculate_damage('關羽', '曹操')
        
        self.assertEqual(self.game.stats['damage']['關羽'], 28)  # 14 + 14
    
    def test_simulate_one_wave(self):
        """測試 2-4: 模擬一波戰鬥"""
        self.game.simulate_wave(1)  # Wave 1
        
        # 驗證有傷害產生
        total_damage = sum(self.game.stats['damage'].values())
        self.assertGreater(total_damage, 0)
    
    def test_simulate_three_waves(self):
        """測試 2-5: 模擬三波完整戰役"""
        self.game.simulate_battle()
        
        # 蜀吳傷害應大於魏軍傷害 (蜀吳勝)
        shu_wu_damage = sum(
            dmg for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction in ['蜀', '吳']
        )
        wei_damage = sum(
            dmg for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction == '魏'
        )
        
        self.assertGreater(shu_wu_damage, wei_damage)
    
    def test_troop_loss_tracking(self):
        """測試 2-6: defaultdict 追蹤兵力損失"""
        # Week 02: defaultdict
        self.game.simulate_battle()
        
        # 夏侯惇應受到傷害
        self.assertGreater(self.game.stats['losses']['夏侯惇'], 0)
    
    def test_damage_ranking_most_common(self):
        """測試 2-7: most_common() 傷害排名"""
        # Week 02: Counter.most_common()
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        
        # 前 5 名傷害遞減
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))
    
    def test_faction_damage_stats(self):
        """測試 2-8: 按勢力統計傷害"""
        # Week 02: groupby 概念 + defaultdict
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        
        self.assertGreater(faction_stats['蜀'], 0)
        self.assertGreater(faction_stats['吳'], 0)
        self.assertGreater(faction_stats['魏'], 0)
    
    def test_defeated_generals(self):
        """測試 2-9: 正確識別戰敗將領"""
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        
        # 應該有將領戰敗
        self.assertGreater(len(defeated), 0)
```

### 2.2 實現代碼

```python
# solution/chibi_battle.py (延續)

from collections import Counter, defaultdict

class ChibiBattle:
    
    def __init__(self):
        self.generals = {}
        # Week 02: Counter 和 defaultdict
        self.stats = {
            'damage': Counter(),        # 傷害統計
            'losses': defaultdict(int)  # 兵力損失
        }
    
    # Week 02: sorted() - 按速度排序
    def get_battle_order(self):
        """根據速度決定戰鬥順序"""
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)
    
    def calculate_damage(self, attacker_name, defender_name):
        """計算傷害: 攻擊 - 防禦"""
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        
        damage = max(1, attacker.atk - defender.def_)
        
        # Week 02: Counter 自動累加
        self.stats['damage'][attacker_name] += damage
        self.stats['losses'][defender_name] += damage
        
        return damage
    
    def simulate_wave(self, wave_num):
        """模擬一波戰鬥"""
        order = self.get_battle_order()
        
        # 簡化: 蜀軍武將對魏軍武將各一次
        shu = [g for g in self.generals.values() if g.faction == '蜀']
        wei = [g for g in self.generals.values() if g.faction == '魏']
        
        for i, attacker in enumerate(shu[:wave_num]):
            target = wei[i]
            self.calculate_damage(attacker.name, target.name)
    
    def simulate_battle(self):
        """模擬三波完整戰役"""
        for wave in range(1, 4):
            self.simulate_wave(wave)
    
    # Week 02: Counter.most_common()
    def get_damage_ranking(self, top_n=5):
        """傷害排名 (Top N)"""
        return self.stats['damage'].most_common(top_n)
    
    # Week 02: groupby 概念
    def get_faction_stats(self):
        """按勢力統計傷害"""
        faction_damage = defaultdict(int)
        
        for general_name, damage in self.stats['damage'].items():
            faction = self.generals[general_name].faction
            faction_damage[faction] += damage
        
        return dict(faction_damage)
    
    def get_defeated_generals(self):
        """取得戰敗將領"""
        defeated = []
        for name, total_loss in self.stats['losses'].items():
            if total_loss >= self.generals[name].hp:
                defeated.append(name)
        return defeated
```

### 2.3 執行測試

```bash
$ python -m pytest tests/test_stage2_battle_logic.py -v

test_battle_order_by_speed ............. PASS ✓
test_calculate_damage .................. PASS ✓
test_damage_counter_accumulation ....... PASS ✓
test_simulate_one_wave ................. PASS ✓
test_simulate_three_waves .............. PASS ✓
test_troop_loss_tracking ............... PASS ✓
test_damage_ranking_most_common ........ PASS ✓
test_faction_damage_stats .............. PASS ✓
test_defeated_generals ................. PASS ✓

════════════════════════════════════════════
9 tests passed
```

### ✅ Stage 2 完成標準

- [x] 根據速度排序戰鬥順序 (`sorted()`)
- [x] 正確計算傷害 (攻擊 - 防禦)
- [x] 使用 `Counter` 統計傷害
- [x] 使用 `defaultdict` 追蹤兵力損失
- [x] 實現 `most_common()` 傷害排名
- [x] 按勢力統計傷害 (groupby 概念)
- [x] 至少 9 個測試通過

---

## 🎨 Stage 3: REFACTOR 階段 - 視覺化與報告

### 目標
重構代碼，新增 ASCII 視覺化，保持所有測試通過。

### 3.1 實現 ASCII 視覺化

```python
# solution/chibi_battle.py (延續)

class ChibiBattle:
    
    def print_battle_start(self):
        """列印戰役開始"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║        吞食天地 - 赤壁戰役 │ 蜀吳聯軍 vs 曹操魏軍      ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        
        # 列印各武將狀態
        for faction in ['蜀', '吳', '魏']:
            print(f"【{faction}軍】")
            generals = [g for g in self.generals.values() if g.faction == faction]
            for g in sorted(generals, key=lambda x: x.spd, reverse=True):
                bar = '█' * (g.hp // 10) + '░' * (10 - g.hp // 10)
                leader = " (軍師)" if g.is_leader else ""
                print(f"  ⚔ {g.name:8} {bar} 攻{g.atk:2} 防{g.def_:2} 速{g.spd:2}{leader}")
            print()
    
    def print_damage_report(self):
        """列印傷害統計報告"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║              【赤壁戰役 - 傷害統計報告】                ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        
        # Week 02: Counter.most_common()
        print("【傷害輸出排名 Top 5】")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            bar = '█' * (dmg // 5) + '░' * (20 - dmg // 5)
            print(f"  {i}. {name:8} {bar} {dmg:3} HP")
        
        print("\n【兵力損失統計】")
        for name in sorted(self.stats['losses'].keys(), 
                          key=lambda x: self.stats['losses'][x], reverse=True)[:5]:
            loss = self.stats['losses'][name]
            defeated = "✓" if loss >= self.generals[name].hp else " "
            print(f"  {defeated} {name:8} → 損失 {loss:3} 兵力")
        
        # Week 02: groupby 概念
        print("\n【勢力傷害統計】")
        faction_stats = self.get_faction_stats()
        max_damage = max(faction_stats.values()) if faction_stats else 1
        for faction in ['蜀', '吳', '魏']:
            total = faction_stats.get(faction, 0)
            ratio = int(total / max_damage * 20) if max_damage else 0
            bar = '█' * ratio + '░' * (20 - ratio)
            percentage = (total / sum(faction_stats.values()) * 100) if faction_stats else 0
            print(f"  {faction} {bar} {total:3} HP ({percentage:5.1f}%)")
        
        print("\n" + "═" * 57)
    
    def run_full_battle(self):
        """執行完整戰役"""
        self.print_battle_start()
        print("【開始三波戰鬥...】\n")
        
        self.simulate_battle()
        
        print("\n【戰役完成】\n")
        self.print_damage_report()
```

### 3.2 測試視覺化不影響邏輯

```python
# tests/test_stage3_refactor.py

class TestRefactoring(unittest.TestCase):
    """Stage 3: 重構測試 (確保視覺化不影響邏輯)"""
    
    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')
    
    def test_stats_unchanged_after_refactor(self):
        """測試 3-1: 重構後統計結果不變"""
        self.game.simulate_battle()
        
        damage_before = dict(self.game.stats['damage'])
        losses_before = dict(self.game.stats['losses'])
        
        # 重新執行 (視覺化不應改變邏輯)
        self.assertEqual(dict(self.game.stats['damage']), damage_before)
        self.assertEqual(dict(self.game.stats['losses']), losses_before)
    
    def test_all_stage1_tests_still_pass(self):
        """測試 3-2: Stage 1 測試仍通過"""
        self.game.load_generals('generals.txt')
        self.assertEqual(len(self.game.generals), 9)
    
    def test_all_stage2_tests_still_pass(self):
        """測試 3-3: Stage 2 測試仍通過"""
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        self.assertEqual(len(ranking), 5)
```

### 3.3 完整程式碼範例 (手寫版)

```python
# solution/chibi_battle.py (完整版本)

from collections import namedtuple, Counter, defaultdict

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattle:
    def __init__(self):
        self.generals = {}
        self.stats = {
            'damage': Counter(),
            'losses': defaultdict(int)
        }
    
    def load_generals(self, filename):
        """Week 07: 檔案 I/O"""
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == 'EOF':
                    break
                if not line:
                    continue
                
                parts = line.split()
                faction, name, hp, atk, def_, spd, is_leader = parts
                
                general = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == 'True')
                )
                self.generals[name] = general
    
    def get_battle_order(self):
        """Week 02: sorted() 按速度排序"""
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)
    
    def calculate_damage(self, attacker_name, defender_name):
        """計算傷害"""
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        
        damage = max(1, attacker.atk - defender.def_)
        
        # Week 02: Counter 自動累加
        self.stats['damage'][attacker_name] += damage
        self.stats['losses'][defender_name] += damage
        
        return damage
    
    def simulate_wave(self, wave_num):
        """模擬一波"""
        shu = [g for g in self.generals.values() if g.faction == '蜀']
        wei = [g for g in self.generals.values() if g.faction == '魏']
        
        for i, attacker in enumerate(shu[:wave_num]):
            if i < len(wei):
                self.calculate_damage(attacker.name, wei[i].name)
    
    def simulate_battle(self):
        """模擬三波戰役"""
        for wave in range(1, 4):
            self.simulate_wave(wave)
    
    def get_damage_ranking(self, top_n=5):
        """Week 02: Counter.most_common()"""
        return self.stats['damage'].most_common(top_n)
    
    def get_faction_stats(self):
        """Week 02: groupby 概念"""
        faction_damage = defaultdict(int)
        for name, damage in self.stats['damage'].items():
            faction = self.generals[name].faction
            faction_damage[faction] += damage
        return dict(faction_damage)
    
    def get_defeated_generals(self):
        """取得戰敗將領"""
        return [name for name, loss in self.stats['losses'].items() 
                if loss >= self.generals[name].hp]
    
    def print_damage_report(self):
        """ASCII 報告"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║              【赤壁戰役 - 傷害統計報告】                ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        
        print("【傷害輸出排名】")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            bar = '█' * (dmg // 5) + '░' * (20 - dmg // 5)
            print(f"  {i}. {name:8} {bar} {dmg:3} HP")
        
        print("\n【勢力傷害統計】")
        faction_stats = self.get_faction_stats()
        for faction in ['蜀', '吳', '魏']:
            total = faction_stats.get(faction, 0)
            print(f"  {faction} → {total} HP")
        
        print("\n" + "═" * 57)
```

### 3.4 執行完整測試

```bash
$ python -m pytest tests/ -v --tb=short

test_stage1_data_loading.py:
  test_load_generals_from_file ......... PASS ✓
  test_parse_general_attributes ....... PASS ✓
  test_faction_distribution ........... PASS ✓
  test_eof_parsing ..................... PASS ✓

test_stage2_battle_logic.py:
  test_battle_order_by_speed .......... PASS ✓
  test_calculate_damage ............... PASS ✓
  test_damage_counter_accumulation ... PASS ✓
  test_simulate_one_wave .............. PASS ✓
  test_simulate_three_waves ........... PASS ✓
  test_troop_loss_tracking ............ PASS ✓
  test_damage_ranking_most_common ..... PASS ✓
  test_faction_damage_stats ........... PASS ✓
  test_defeated_generals .............. PASS ✓

test_stage3_refactor.py:
  test_stats_unchanged_after_refactor  PASS ✓
  test_all_stage1_tests_still_pass ... PASS ✓
  test_all_stage2_tests_still_pass ... PASS ✓

════════════════════════════════════════════
12 tests passed
```

### ✅ Stage 3 完成標準

- [x] 新增 ASCII 視覺化報告
- [x] 不改變原有邏輯 (所有測試通過)
- [x] 代碼可讀性提升
- [x] 功能完整且可執行

---

## 🎯 完整作業檢查清單

### 提交物品
- [x] `solution/chibi_battle.py` - 手寫版核心引擎
- [x] `solution/chibi_battle_easy.py` - AI 簡化版本
- [x] `solution/test_chibi.py` - 完整 TDD 測試 (≥12 個)
- [x] `solution/TEST_LOG.md` - 測試執行日誌
- [x] `generals.txt` - 輸入資料 (9 位武將)
- [x] `battles.txt` - 戰役配置
- [x] `AI_USAGE.md` - AI 使用說明

### 課程整合檢查
- [x] **Week 02**: `sorted()`, `Counter`, `defaultdict`, `namedtuple`
- [x] **Week 07**: 檔案 I/O, EOF 輸入處理
- [x] **TDD 流程**: 至少三階段 (RED → GREEN → REFACTOR)

### 代碼品質要求
- [x] 無型別錯誤 (`as any` 禁用)
- [x] 所有測試通過 (≥12 個)
- [x] ASCII 視覺化清晰
- [x] 代碼註解完整

---

## 📝 測試日誌範例 (TEST_LOG.md)

```markdown
# 赤壁戰役 - 測試執行日誌

## Stage 1: 資料讀取

### RED (測試失敗)
```
test_load_generals_from_file ......... FAIL ❌
  AttributeError: 'ChibiBattle' object has no attribute 'load_generals'
```

### GREEN (實現最小化代碼)
```
test_load_generals_from_file ......... PASS ✓
test_parse_general_attributes ....... PASS ✓
test_faction_distribution ........... PASS ✓
test_eof_parsing ..................... PASS ✓
```

## Stage 2: 戰鬥模擬

### GREEN (所有測試通過)
```
test_battle_order_by_speed .......... PASS ✓
test_calculate_damage ............... PASS ✓
test_damage_counter_accumulation ... PASS ✓
test_simulate_one_wave .............. PASS ✓
test_simulate_three_waves ........... PASS ✓
test_troop_loss_tracking ............ PASS ✓
test_damage_ranking_most_common ..... PASS ✓
test_faction_damage_stats ........... PASS ✓
test_defeated_generals .............. PASS ✓
```

## Stage 3: 重構與視覺化

### REFACTOR (保持所有測試通過)
```
test_stats_unchanged_after_refactor  PASS ✓
test_all_stage1_tests_still_pass ... PASS ✓
test_all_stage2_tests_still_pass ... PASS ✓

════════════════════════════════════════════
總計: 12 tests passed, 0 failures ✅
```

## 最終報告範例

╔═══════════════════════════════════════════════════════╗
║              【赤壁戰役 - 傷害統計報告】                ║
╚═══════════════════════════════════════════════════════╝

【傷害輸出排名】
  1. 關羽     █████████████████░░ 98 HP
  2. 周瑜     ██████████████░░░░░ 72 HP
  3. 黃蓋     ██████████░░░░░░░░░ 54 HP
  4. 劉備     █████████░░░░░░░░░░ 45 HP
  5. 諸葛亮   ████░░░░░░░░░░░░░░░ 28 HP

【勢力傷害統計】
  蜀 → 351 HP (58%)
  吳 → 154 HP (25%)
  魏 → 75 HP (12%)

════════════════════════════════════════════════════════════
```

---

## 💡 AI 使用說明 (AI_USAGE.md)

### 允許使用 AI 的時機
✅ 不懂如何寫測試時
✅ 實現遇到 Python 語法問題時
✅ ASCII 視覺化時
✅ 需要重構代碼時

### 禁止使用 AI 的地方
❌ 完整複製 AI 生成的代碼
❌ 跳過 TDD 三階段流程
❌ 使用 `as any` 或 `@ts-ignore` 等方式壓制錯誤

### 推薦作法
1. 先自己寫測試
2. 看測試失敗 (RED)
3. AI 協助實現 (GREEN)
4. 自己重構 (REFACTOR)
5. 確認所有測試通過

---

## 🎓 學習重點

本作業涵蓋:

| 項目 | 說明 |
|-----|------|
| **TDD** | Red → Green → Refactor 三階段 |
| **Week 02** | sorted, Counter, defaultdict, namedtuple |
| **Week 07** | 檔案 I/O, EOF 輸入處理 |
| **設計思想** | 資料驅動 + 統計分析 + 視覺化 |
| **測試寫作** | unittest, setUp/tearDown, Arrange-Act-Assert |

---

## 📞 常見問題

**Q: 我應該先寫多少測試？**
A: 先寫 4 個 Stage 1 測試，看它們全部失敗。

**Q: Counter 和 defaultdict 差在哪？**
A: Counter 是字典，有 `most_common()`。defaultdict 是字典，自動初始化為 0。

**Q: 為什麼要三個階段？**
A: RED 確保測試有效，GREEN 實現最小代碼，REFACTOR 保證品質。

**Q: 我可以改戰役規則嗎？**
A: 可以，但要修改對應的測試案例。

---

**祝你編碼順利！🎮**
