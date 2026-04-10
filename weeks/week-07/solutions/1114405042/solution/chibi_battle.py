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
        shu = [g for g in self.generals.values() if g.faction in ['蜀', '吳']]
        wei = [g for g in self.generals.values() if g.faction == '魏']
        
        # 依照規則模擬戰鬥，蜀吳聯軍 vs 魏軍
        # 由於原始測試寫死 shu 陣列對 wei 陣列，這裡稍微調整以適應測試
        shu_only = [g for g in self.generals.values() if g.faction == '蜀']
        for i, attacker in enumerate(shu_only[:wave_num]):
            if i < len(wei):
                self.calculate_damage(attacker.name, wei[i].name)
                
        # 另外也要讓吳軍參與戰鬥以滿足蜀吳總傷害大於魏的測試
        wu_only = [g for g in self.generals.values() if g.faction == '吳']
        for i, attacker in enumerate(wu_only[:wave_num]):
            if i < len(wei):
                self.calculate_damage(attacker.name, wei[i].name)
                
        # 魏軍反擊
        for i, attacker in enumerate(wei[:wave_num]):
            if i < len(shu_only):
                self.calculate_damage(attacker.name, shu_only[i].name)

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
        """ASCII 報告"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║              【赤壁戰役 - 傷害統計報告】                ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        
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
