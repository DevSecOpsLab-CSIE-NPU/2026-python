"""赤壁戰役遊戲引擎 - AI 簡化版"""

from chibi_battle import ChibiBattle, General
from collections import Counter, defaultdict


class ChibiBattleEasy(ChibiBattle):
    """簡化版: 使用 AI 協助的快速實現"""
    
    def __init__(self):
        super().__init__()
        self.ai_assists = []  # 記錄 AI 協助
    
    def load_generals_easy(self, filename):
        """
        簡化版讀取: 無 EOF 檢查
        (實際生產應使用 load_generals)
        """
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line == 'EOF':
                    break
                
                parts = line.split()
                if len(parts) >= 7:
                    faction, name, hp, atk, def_, spd, is_leader = parts[:7]
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
    
    def simulate_battle_easy(self):
        """簡化版戰鬥: 所有武將對所有敵方"""
        all_generals = list(self.generals.values())
        
        for attacker in all_generals:
            # 每位將領對敵方進行攻擊
            for defender in all_generals:
                if attacker.faction != defender.faction:
                    # 計算傷害
                    damage = max(1, attacker.atk - defender.def_)
                    self.stats['damage'][attacker.name] += damage
                    self.stats['losses'][defender.name] += damage
    
    def get_winner(self):
        """判定勝者: 蜀吳 vs 魏"""
        faction_damage = self.get_faction_stats()
        
        shu_wu_damage = faction_damage.get('蜀', 0) + faction_damage.get('吳', 0)
        wei_damage = faction_damage.get('魏', 0)
        
        if shu_wu_damage > wei_damage:
            return "蜀吳聯軍"
        elif wei_damage > shu_wu_damage:
            return "曹操魏軍"
        else:
            return "平手"
    
    def print_easy_report(self):
        """簡化版報告"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║          赤壁戰役 - 簡化版 (AI 輔助)                   ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        
        faction_stats = self.get_faction_stats()
        print("【各勢力傷害輸出】")
        for faction in ['蜀', '吳', '魏']:
            total = faction_stats.get(faction, 0)
            print(f"  {faction} → {total} HP")
        
        print(f"\n【戰役勝者】{self.get_winner()}\n")
        
        print("═" * 57)
    
    def run_easy_battle(self):
        """執行簡化版戰役"""
        self.print_battle_start()
        print("【使用 AI 簡化版進行戰鬥...】\n")
        
        self.simulate_battle_easy()
        
        print("\n【戰役完成】\n")
        self.print_easy_report()


if __name__ == '__main__':
    game = ChibiBattleEasy()
    game.load_generals_easy('generals.txt')
    game.run_easy_battle()
