import collections
import os
import random
import time

# 核心數據結構
General = collections.namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattleSupreme:
    def __init__(self):
        self.generals = {}
        self.battle_config = {}
        self.stats = {'damage': collections.Counter(), 'losses': collections.defaultdict(int)}
        self.skills = {
            "劉備": "雙股劍縱橫", "關羽": "青龍偃月斬", "張飛": "丈八蛇矛刺",
            "曹操": "倚天劍氣", "夏侯惇": "剛烈拔矢", "張遼": "威震逍遙津",
            "周瑜": "火燒赤壁", "孫權": "紫髯劍法", "陸遜": "火燒連營"
        }

    def load_data(self, gen_file, bat_file):
        """一次載入所有必要資料"""
        # 載入武將
        with open(gen_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == 'EOF' or not line: break
                p = line.split()
                if len(p) >= 7:
                    self.generals[p[1]] = General(p[0], p[1], int(p[2]), int(p[3]), int(p[4]), int(p[5]), p[6] == 'True')
        # 載入戰役
        with open(bat_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line == 'EOF': continue
                p = line.split()
                if len(p) >= 5:
                    self.battle_config = {'attackers': list(p[0]), 'defender': p[2], 'name': p[3], 'waves': p[4]}
                    break

    def is_alive(self, name):
        return self.stats['losses'][name] < self.generals[name].hp

    def run_battle(self):
        """至尊版戰鬥流程：含日誌與即時判斷"""
        print(f"\n{'='*20} 戰役開始：{self.battle_config['name']} {'='*20}")
        
        for w in range(1, int(self.battle_config['waves']) + 1):
            print(f"\n--- 第 {w} 波攻勢 ---")
            # 取得目前還活著的武將順序
            order = sorted([g for n, g in self.generals.items() if self.is_alive(n)], key=lambda x: x.spd, reverse=True)
            
            for attacker in order:
                if not self.is_alive(attacker.name): continue
                
                # 決定目標
                is_atk_side = attacker.faction in self.battle_config['attackers']
                targets = [n for n, g in self.generals.items() if self.is_alive(n) and 
                           (g.faction == self.battle_config['defender'] if is_atk_side else g.faction in self.battle_config['attackers'])]
                
                if targets:
                    target_name = random.choice(targets)
                    # 領袖加成
                    has_leader = any(g.is_leader for n, g in self.generals.items() if g.faction == attacker.faction and self.is_alive(n))
                    dmg = max(1, int(attacker.atk * (1.1 if has_leader else 1.0)) - self.generals[target_name].def_)
                    
                    self.stats['damage'][attacker.name] += dmg
                    self.stats['losses'][target_name] += dmg
                    
                    print(f" ⚔️  {attacker.name} 使用【{self.skills.get(attacker.name, '猛攻')}】擊向 {target_name}，造成 {dmg} 點傷害")
                    if not self.is_alive(target_name):
                        print(f" 💀 【戰報】{target_name} 負傷敗退！")
            time.sleep(0.3)

    def print_final_report(self):
        """高質感結算圖表"""
        print("\n" + "█"*60)
        print(f"║ 最終戰果：{self.battle_config['name']} 戰役結算 ║".center(54))
        print("█"*60)
        
        ranking = self.stats['damage'].most_common()
        if not ranking: return
        max_dmg = ranking[0][1]
        
        print("\n[ 🏆 傷害輸出榜 ]")
        for i, (name, dmg) in enumerate(ranking, 1):
            bar = "█" * int(dmg/max_dmg * 25)
            print(f"  {i}. {name:4} |{bar:<25}| {dmg} HP")

        print("\n[ 🚩 陣營統計 ]")
        f_stats = collections.defaultdict(int)
        for n, d in self.stats['damage'].items(): f_stats[self.generals[n].faction] += d
        for f, d in f_stats.items():
            print(f"  {f}軍總部隊造成 {d} 點傷害")
        print("\n" + "═"*60)

if __name__ == "__main__":
    game = ChibiBattleSupreme()
    game.load_data('generals.txt', 'battles.txt')
    game.run_battle()
    game.print_final_report()