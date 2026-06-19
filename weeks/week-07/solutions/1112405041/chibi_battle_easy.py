from collections import namedtuple, Counter, defaultdict

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattle:
    def __init__(self):
        self.generals = {}
        self.stats = {'damage': Counter(), 'losses': defaultdict(int)}

    def load_generals(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == 'EOF':
                    break
                if not line:
                    continue
                parts = line.split()
                g = General(parts[0], parts[1], int(parts[2]), int(parts[3]),
                            int(parts[4]), int(parts[5]), parts[6] == 'True')
                self.generals[g.name] = g

    def get_battle_order(self):
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, a, b):
        dmg = max(1, self.generals[a].atk - self.generals[b].def_)
        self.stats['damage'][a] += dmg
        self.stats['losses'][b] += dmg
        return dmg

    def simulate_wave(self, n):
        allies = [g for g in self.generals.values() if g.faction in ['蜀', '吳']]
        wei = [g for g in self.generals.values() if g.faction == '魏']
        for a in allies:
            for t in wei:
                self.calculate_damage(a.name, t.name)
        for a in wei:
            for t in allies[:n]:
                self.calculate_damage(a.name, t.name)

    def simulate_battle(self):
        for w in range(1, 4):
            self.simulate_wave(w)

    def get_damage_ranking(self, top_n=5):
        return self.stats['damage'].most_common(top_n)

    def get_faction_stats(self):
        r = defaultdict(int)
        for n, d in self.stats['damage'].items():
            r[self.generals[n].faction] += d
        return dict(r)

    def get_defeated_generals(self):
        return [n for n, l in self.stats['losses'].items() if l >= self.generals[n].hp]

    def print_damage_report(self):
        print("╔═══════════════════════════════════════════════════════╗")
        print("║              【赤壁戰役 - 傷害統計報告】                ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        print("【傷害輸出排名 Top 5】")
        for i, (n, d) in enumerate(self.get_damage_ranking(), 1):
            print(f"  {i}. {n:8} {'█'*(d//5)}{'░'*(20-d//5)} {d:3} HP")
        print("\n【勢力傷害統計】")
        for f in ['蜀', '吳', '魏']:
            print(f"  {f} → {self.get_faction_stats().get(f, 0)} HP")
        print("\n" + "═" * 57)

    def run_full_battle(self):
        self.simulate_battle()
        self.print_damage_report()
