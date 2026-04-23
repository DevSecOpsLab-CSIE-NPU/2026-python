from collections import namedtuple, Counter, defaultdict

# Week 02: 使用 namedtuple 定義武將結構
General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattle:
    def __init__(self):
        self.generals = {}
        # Week 02: Counter 統計傷害, defaultdict 統計損失
        self.stats = {
            'damage': Counter(),
            'losses': defaultdict(int)
        }

    def load_generals(self, filename):
        """Week 07: 檔案讀取與 EOF 處理"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line == 'EOF': break
                    if not line: continue
                    parts = line.split()
                    faction, name, hp, atk, def_, spd, is_leader = parts
                    self.generals[name] = General(
                        faction, name, int(hp), int(atk), int(def_), int(spd), is_leader == 'True'
                    )
        except FileNotFoundError:
            pass

    def get_battle_order(self):
        """Week 02: sorted() 按速度排序"""
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name, defender_name):
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)
        self.stats['damage'][attacker_name] += damage
        self.stats['losses'][defender_name] += damage
        return damage

    def simulate_battle(self):
        """模擬戰役流程"""
        shu_wu = [g for g in self.generals.values() if g.faction in ['蜀', '吳']]
        wei = [g for g in self.generals.values() if g.faction == '魏']
        # 簡單模擬三波攻勢
        for i in range(min(len(shu_wu), len(wei))):
            self.calculate_damage(shu_wu[i].name, wei[i].name)
            self.calculate_damage(wei[i].name, shu_wu[i].name)

    def get_damage_ranking(self):
        return self.stats['damage'].most_common(5)

    def get_faction_stats(self):
        faction_dmg = defaultdict(int)
        for name, dmg in self.stats['damage'].items():
            faction_dmg[self.generals[name].faction] += dmg
        return dict(faction_dmg)
