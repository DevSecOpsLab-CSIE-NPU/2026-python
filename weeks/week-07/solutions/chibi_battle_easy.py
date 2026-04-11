"""
赤壁戰役遊戲引擎 - AI 簡化版
適用於初學者的簡易版本
"""

from collections import namedtuple, Counter, defaultdict

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])


class ChibiBattleEasy:
    """簡化版赤壁戰役引擎"""
    
    def __init__(self):
        self.generals = {}
        self.stats = {
            'damage': Counter(),
            'losses': defaultdict(int)
        }
    
    def load_generals(self, filename):
        """讀取武將資料"""
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
        """按速度排序"""
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)
    
    def calculate_damage(self, attacker_name, defender_name):
        """計算傷害"""
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)
        self.stats['damage'][attacker_name] += damage
        self.stats['losses'][defender_name] += damage
        return damage
    
    def simulate_battle(self):
        """模擬戰鬥"""
        shu = [g for g in self.generals.values() if g.faction == '蜀']
        wei = [g for g in self.generals.values() if g.faction == '魏']
        
        for i, attacker in enumerate(shu):
            if i < len(wei):
                self.calculate_damage(attacker.name, wei[i].name)
    
    def get_damage_ranking(self, top_n=5):
        """傷害排名"""
        return self.stats['damage'].most_common(top_n)
    
    def get_faction_stats(self):
        """勢力統計"""
        faction_damage = defaultdict(int)
        for name, damage in self.stats['damage'].items():
            faction = self.generals[name].faction
            faction_damage[faction] += damage
        return dict(faction_damage)


def main():
    """主程式"""
    game = ChibiBattleEasy()
    game.load_generals('generals.txt')
    game.simulate_battle()
    
    print("【傷害排名】")
    for i, (name, dmg) in enumerate(game.get_damage_ranking(), 1):
        print(f"  {i}. {name}: {dmg} HP")
    
    print("\n【勢力統計】")
    for faction, dmg in game.get_faction_stats().items():
        print(f"  {faction}: {dmg} HP")


if __name__ == '__main__':
    main()
