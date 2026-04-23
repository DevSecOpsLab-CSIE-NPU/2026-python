"""
赤壁戰役 - 三國武將 PK 版
簡化版本

Week 02 技能整合：sorted, Counter, defaultdict, namedtuple
Week 07 技能整合：檔案 I/O, EOF 輸入處理
"""

from collections import namedtuple, Counter, defaultdict

General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattle:
    def __init__(self):
        self.generals = {}
        self.stats = {"damage": Counter(), "losses": defaultdict(int)}

    def load_generals(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "EOF":
                    break
                if not line:
                    continue
                parts = line.split()
                faction, name, hp, atk, def_, spd, is_leader = parts
                self.generals[name] = General(
                    faction,
                    name,
                    int(hp),
                    int(atk),
                    int(def_),
                    int(spd),
                    is_leader == "True",
                )

    def get_battle_order(self):
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name, defender_name):
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)
        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        return damage

    def simulate_wave(self, wave_num):
        shu = [g for g in self.generals.values() if g.faction == "蜀"]
        wei = [g for g in self.generals.values() if g.faction == "魏"]
        for i, attacker in enumerate(shu[:wave_num]):
            if i < len(wei):
                self.calculate_damage(attacker.name, wei[i].name)

    def simulate_battle(self):
        for wave in range(1, 4):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n=5):
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self):
        faction_damage = defaultdict(int)
        for name, damage in self.stats["damage"].items():
            faction_damage[self.generals[name].faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self):
        return [
            name
            for name, loss in self.stats["losses"].items()
            if loss >= self.generals[name].hp
        ]

    def run(self):
        self.load_generals("generals.txt")
        self.simulate_battle()
        print("【赤壁戰役 - 傷害統計】\n")
        print("【傷害排名】")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            print(f"  {i}. {name}: {dmg} HP")
        print("\n【勢力統計】")
        for faction, total in self.get_faction_stats().items():
            print(f"  {faction}: {total} HP")


if __name__ == "__main__":
    ChibiBattle().run()
