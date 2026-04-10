# solution/chibi_battle.py
# 三國武將 PK 版 - 赤壁戰役遊戲引擎 (手寫版)
# 整合 Week 02 資料結構 + Week 07 檔案 I/O

from collections import namedtuple, Counter, defaultdict

# Week 02: namedtuple 結構體
General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])


class ChibiBattle:
    """吞食天地 - 赤壁戰役引擎"""

    def __init__(self):
        self.generals = {}
        # Week 02: Counter 和 defaultdict
        self.stats = {
            'damage': Counter(),        # 傷害統計
            'losses': defaultdict(int)  # 兵力損失
        }

    # ─────────────────────────────────────────────
    # Stage 1: 資料讀取 (Week 07 檔案 I/O)
    # ─────────────────────────────────────────────

    def load_generals(self, filename):
        """讀取武將資料，EOF 結尾"""
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                # Week 07: EOF 結尾處理
                if line == 'EOF':
                    break
                if not line:
                    continue

                # 解析一行資料: faction name hp atk def_ spd is_leader
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

    # ─────────────────────────────────────────────
    # Stage 2: 戰鬥模擬 (Week 02 資料結構)
    # ─────────────────────────────────────────────

    def get_battle_order(self):
        """Week 02: sorted(key=...) 按速度由高到低排序"""
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name, defender_name):
        """計算傷害: max(1, 攻擊 - 防禦)"""
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]

        damage = max(1, attacker.atk - defender.def_)

        # Week 02: Counter 自動累加傷害
        self.stats['damage'][attacker_name] += damage
        # Week 02: defaultdict 追蹤兵力損失
        self.stats['losses'][defender_name] += damage

        return damage

    def simulate_wave(self, wave_num):
        """模擬一波戰鬥 (蜀軍攻擊魏軍，wave_num 決定出戰人數)"""
        shu = [g for g in self.generals.values() if g.faction == '蜀']
        wei = [g for g in self.generals.values() if g.faction == '魏']

        for i, attacker in enumerate(shu[:wave_num]):
            if i < len(wei):
                self.calculate_damage(attacker.name, wei[i].name)

    def simulate_battle(self):
        """模擬三波完整戰役"""
        for wave in range(1, 4):
            self.simulate_wave(wave)

    # Week 02: Counter.most_common()
    def get_damage_ranking(self, top_n=5):
        """傷害排名 Top N"""
        return self.stats['damage'].most_common(top_n)

    # Week 02: groupby 概念 + defaultdict
    def get_faction_stats(self):
        """按勢力統計傷害"""
        faction_damage = defaultdict(int)
        for name, damage in self.stats['damage'].items():
            faction = self.generals[name].faction
            faction_damage[faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self):
        """取得已戰敗將領 (損失 >= HP)"""
        return [
            name for name, loss in self.stats['losses'].items()
            if loss >= self.generals[name].hp
        ]

    # ─────────────────────────────────────────────
    # Stage 3: ASCII 視覺化報告
    # ─────────────────────────────────────────────

    def print_battle_start(self):
        """列印戰役開始畫面"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║        吞食天地 - 赤壁戰役 │ 蜀吳聯軍 vs 曹操魏軍      ║")
        print("╚═══════════════════════════════════════════════════════╝\n")

        for faction in ['蜀', '吳', '魏']:
            print(f"【{faction}軍】")
            generals = [g for g in self.generals.values() if g.faction == faction]
            for g in sorted(generals, key=lambda x: x.spd, reverse=True):
                filled = g.hp // 10
                bar = '█' * filled + '░' * (10 - filled)
                leader = " (軍師)" if g.is_leader else ""
                print(f"  ⚔ {g.name:4} {bar} 攻{g.atk:2} 防{g.def_:2} 速{g.spd:2}{leader}")
            print()

    def print_damage_report(self):
        """列印傷害統計報告"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║              【赤壁戰役 - 傷害統計報告】                ║")
        print("╚═══════════════════════════════════════════════════════╝\n")

        # Week 02: Counter.most_common()
        print("【傷害輸出排名 Top 5】")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            bar = '█' * (dmg // 5) + '░' * max(0, 20 - dmg // 5)
            print(f"  {i}. {name:4} {bar} {dmg:3} HP")

        print("\n【兵力損失統計】")
        sorted_losses = sorted(
            self.stats['losses'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        for name, loss in sorted_losses:
            defeated = "✓" if loss >= self.generals[name].hp else " "
            print(f"  {defeated} {name:4} → 損失 {loss:3} 兵力")

        # Week 02: groupby 概念
        print("\n【勢力傷害統計】")
        faction_stats = self.get_faction_stats()
        total_all = sum(faction_stats.values()) or 1
        max_damage = max(faction_stats.values()) if faction_stats else 1
        for faction in ['蜀', '吳', '魏']:
            total = faction_stats.get(faction, 0)
            ratio = int(total / max_damage * 20) if max_damage else 0
            bar = '█' * ratio + '░' * (20 - ratio)
            pct = total / total_all * 100
            print(f"  {faction} {bar} {total:3} HP ({pct:5.1f}%)")

        print("\n" + "═" * 57)

    def run_full_battle(self):
        """執行完整戰役"""
        self.print_battle_start()
        print("【開始三波戰鬥...】\n")
        self.simulate_battle()
        print("【戰役完成】\n")
        self.print_damage_report()


# ─────────────────────────────────────────────
# 主程式入口
# ─────────────────────────────────────────────
if __name__ == '__main__':
    import os

    # 取得 generals.txt 絕對路徑 (在 week-07/ 目錄)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generals_path = os.path.join(base_dir, 'generals.txt')

    game = ChibiBattle()
    game.load_generals(generals_path)
    game.run_full_battle()
