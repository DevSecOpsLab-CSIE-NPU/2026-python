"""赤壁戰役遊戲引擎 (Week 02-07 統合)"""

from collections import namedtuple, Counter, defaultdict

# Week 02: namedtuple 結構體
General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])


class ChibiBattle:
    """吞食天地戰役引擎"""
    
    def __init__(self):
        self.generals = {}
        self.stats = {
            'damage': Counter(),        # Week 02: Counter - 傷害統計
            'losses': defaultdict(int)  # Week 02: defaultdict - 兵力損失
        }
    
    # Week 07: 檔案 I/O
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
    
    # Week 02: sorted() - 按速度排序
    def get_battle_order(self):
        """根據速度決定戰鬥順序 (速度由高到低)"""
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
        """模擬一波戰鬥 (蜀軍攻擊魏軍)"""
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
        """取得戰敗將領 (兵力損失 >= 初始 HP)"""
        defeated = []
        for name, total_loss in self.stats['losses'].items():
            if total_loss >= self.generals[name].hp:
                defeated.append(name)
        return defeated
    
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
        """列印傷害統計報告 (ASCII 視覺化)"""
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
        total_damage = sum(faction_stats.values()) if faction_stats else 1
        
        for faction in ['蜀', '吳', '魏']:
            total = faction_stats.get(faction, 0)
            ratio = int(total / total_damage * 20) if total_damage else 0
            bar = '█' * ratio + '░' * (20 - ratio)
            percentage = (total / total_damage * 100) if total_damage else 0
            print(f"  {faction} {bar} {total:3} HP ({percentage:5.1f}%)")
        
        print("\n" + "═" * 57)
    
    def run_full_battle(self):
        """執行完整戰役"""
        self.print_battle_start()
        print("【開始三波戰鬥...】\n")
        
        self.simulate_battle()
        
        print("\n【戰役完成】\n")
        self.print_damage_report()


if __name__ == '__main__':
    game = ChibiBattle()
    game.load_generals('generals.txt')
    game.run_full_battle()
