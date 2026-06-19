from collections import namedtuple, Counter, defaultdict
from pathlib import Path

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattle:
    """吞食天地戰役引擎"""

    def __init__(self):
        self.generals = {}
        self.stats = {
            'damage': Counter(),
            'losses': defaultdict(int)
        }

    def load_generals(self, filename):
        """讀取武將資料，EOF 結尾"""
        if not filename or not isinstance(filename, (str, Path)):
            raise ValueError("filename 必須為非空字串或 Path")
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == 'EOF':
                    break
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 7:
                    raise ValueError(f"格式錯誤：每行需 7 欄，得到 {len(parts)} 欄：{line}")
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
        """按速度決定戰鬥順序（高到低）"""
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name, defender_name):
        """計算傷害，至少 1"""
        if attacker_name not in self.generals:
            raise ValueError(f"找不到攻擊者：{attacker_name}")
        if defender_name not in self.generals:
            raise ValueError(f"找不到防禦者：{defender_name}")
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)
        self.stats['damage'][attacker_name] += damage
        self.stats['losses'][defender_name] += damage
        return damage

    def simulate_wave(self, wave_num):
        """模擬一波戰鬥（蜀吳聯軍先攻，魏反擊）"""
        if not isinstance(wave_num, int) or wave_num < 1:
            raise ValueError("wave_num 必須為正整數")
        allies = [g for g in self.generals.values() if g.faction in ['蜀', '吳']]
        wei = [g for g in self.generals.values() if g.faction == '魏']
        for attacker in allies:
            for target in wei:
                self.calculate_damage(attacker.name, target.name)
        for attacker in wei:
            for target in allies[:wave_num]:
                self.calculate_damage(attacker.name, target.name)

    def simulate_battle(self):
        """模擬三波完整戰役"""
        for wave in range(1, 4):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n=5):
        """傷害排名 Top N"""
        return self.stats['damage'].most_common(top_n)

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

    def print_damage_report(self):
        """列印傷害統計報告"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║              【赤壁戰役 - 傷害統計報告】                ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        print("【傷害輸出排名 Top 5】")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            bar = '█' * (dmg // 5) + '░' * (20 - dmg // 5)
            print(f"  {i}. {name:8} {bar} {dmg:3} HP")
        print("\n【勢力傷害統計】")
        faction_stats = self.get_faction_stats()
        for faction in ['蜀', '吳', '魏']:
            total = faction_stats.get(faction, 0)
            print(f"  {faction} → {total} HP")
        print("\n" + "═" * 57)

    def run_full_battle(self):
        """執行完整戰役"""
        self.simulate_battle()
        self.print_damage_report()
