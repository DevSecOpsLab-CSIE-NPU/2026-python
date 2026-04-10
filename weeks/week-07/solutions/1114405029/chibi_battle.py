import collections
import os

# 定義武將資料結構
General = collections.namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattle:
    def __init__(self):
        self.generals = {}
        self.battle_config = {}
        self.stats = {
            'damage': collections.Counter(),
            'losses': collections.defaultdict(int)
        }

    def load_generals(self, filename):
        """載入武將資料"""
        if not os.path.exists(filename): return
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == 'EOF' or not line: break
                parts = line.split()
                if len(parts) >= 7:
                    faction, name, hp, atk, def_, spd, is_leader = parts[:7]
                    self.generals[name] = General(
                        faction, name, int(hp), int(atk), int(def_), int(spd), is_leader == 'True'
                    )

    def load_battles(self, filename):
        """解析 battles.txt 並確保 key 完整存入"""
        if not os.path.exists(filename): return
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line == 'EOF': continue
                parts = line.split()
                # 預期格式: 蜀吳 vs 魏 赤壁 3
                if len(parts) >= 5:
                    self.battle_config = {
                        'attackers': list(parts[0]), # '蜀吳' -> ['蜀', '吳']
                        'defender': parts[2],
                        'name': parts[3],
                        'waves': int(parts[4])
                    }
                    break

    def is_alive(self, name):
        """檢查武將是否存活"""
        return self.stats['losses'][name] < self.generals[name].hp

    def get_battle_order(self):
        """獲取存活武將的行動順序"""
        alive = [g for n, g in self.generals.items() if self.is_alive(n)]
        return sorted(alive, key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name, defender_name):
        """計算傷害，含領袖加成"""
        if not self.is_alive(attacker_name) or not self.is_alive(defender_name):
            return 0
        atk_g = self.generals[attacker_name]
        def_g = self.generals[defender_name]
        
        # 領袖加成邏輯
        leaders = [n for n, g in self.generals.items() if g.faction == atk_g.faction and g.is_leader and self.is_alive(n)]
        bonus = 1.1 if leaders else 1.0
        
        damage = max(1, int(atk_g.atk * bonus) - def_g.def_)
        self.stats['damage'][attacker_name] += damage
        self.stats['losses'][defender_name] += damage
        return damage

    def simulate_wave(self, wave_num):
        """模擬單波戰鬥"""
        order = self.get_battle_order()
        for attacker in order:
            # 判斷目標陣營
            if attacker.faction in self.battle_config.get('attackers', []):
                target_factions = [self.battle_config['defender']]
            else:
                target_factions = self.battle_config.get('attackers', [])
            
            targets = [n for n, g in self.generals.items() if g.faction in target_factions and self.is_alive(n)]
            if targets:
                # 策略：攻擊防禦最低的存活者
                target_name = min(targets, key=lambda n: self.generals[n].def_)
                self.calculate_damage(attacker.name, target_name)

    def simulate_battle(self):
        """執行完整戰役"""
        waves = self.battle_config.get('waves', 3)
        for i in range(1, waves + 1):
            self.simulate_wave(i)

    def get_damage_ranking(self):
        """獲取傷害排名"""
        return self.stats['damage'].most_common()

    def get_faction_stats(self):
        """計算各陣營總傷害 (修復 AttributeError)"""
        faction_dmg = collections.defaultdict(int)
        for name, dmg in self.stats['damage'].items():
            faction = self.generals[name].faction
            faction_dmg[faction] += dmg
        return faction_dmg

    def get_defeated_generals(self):
        """獲取戰敗名單"""
        return [n for n, g in self.generals.items() if not self.is_alive(n)]

    def print_master_report(self):
        """視覺化結算報表"""
        print("\n" + "═"*60)
        print(f"【 {self.battle_config.get('name', '三國')}戰役結算 】".center(54))
        print("═"*60)
        ranking = self.get_damage_ranking()
        if not ranking: return
        max_dmg = ranking[0][1]
        for name, dmg in ranking:
            bar = "█" * int(dmg/max_dmg * 25)
            print(f"  {name:4} | {bar:<25} {dmg} HP")
        print("═"*60)