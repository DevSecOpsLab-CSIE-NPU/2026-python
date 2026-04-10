from collections import namedtuple, Counter, defaultdict

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattle:
    def __init__(self):
        self.generals = {}
        self.stats = {'damage': Counter(), 'losses': defaultdict(int)}
    
    def load_generals(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() == 'EOF': break
                if not line.strip(): continue
                fac, name, hp, atk, d, s, lead = line.strip().split()
                self.generals[name] = General(fac, name, int(hp), int(atk), int(d), int(s), lead=='True')
                
    def get_battle_order(self): return sorted(self.generals.values(), key=lambda x: x.spd, reverse=True)
    
    def calculate_damage(self, atk, dfn):
        dmg = max(1, self.generals[atk].atk - self.generals[dfn].def_)
        self.stats['damage'][atk] += dmg
        self.stats['losses'][dfn] += dmg
        return dmg
        
    def simulate_wave(self, wave):
        for faction in ['蜀', '吳', '魏']:
            attackers = [g for g in self.generals.values() if g.faction == faction]
            targets = [g for g in self.generals.values() if g.faction != faction and g.hp > self.stats['losses'][g.name]]
            for a in attackers[:wave]:
                if targets:
                    self.calculate_damage(a.name, targets[0].name)
                    
    def simulate_battle(self):
        for w in range(1, 4): self.simulate_wave(w)
        
    def get_damage_ranking(self, top_n=5): return self.stats['damage'].most_common(top_n)
    
    def get_faction_stats(self):
        return {f: sum(dmg for n, dmg in self.stats['damage'].items() if self.generals[n].faction == f) for f in ['蜀', '吳', '魏']}
        
    def get_defeated_generals(self):
        return [n for n, loss in self.stats['losses'].items() if loss >= self.generals[n].hp]
