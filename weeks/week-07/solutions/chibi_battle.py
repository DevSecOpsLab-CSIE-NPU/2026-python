"""
赤壁戰役遊戲引擎 - 手寫版
整合 Week 02 資料結構與 Week 07 檔案 I/O

使用 TDD 開發流程，實現三國武將 PK 系統
"""

from collections import namedtuple, Counter, defaultdict

# Week 02: namedtuple 結構體 - 武將資料結構
General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattle:
    """赤壁戰役引擎 - 整合 Week 02 & Week 07 技能"""

    def __init__(self):
        self.generals = {}
        # Week 02: Counter 和 defaultdict 用於統計
        self.stats = {
            "damage": Counter(),  # 傷害統計
            "losses": defaultdict(int),  # 兵力損失追蹤
        }

    # ========== Week 07: 檔案 I/O ==========

    def load_generals(self, filename):
        """
        讀取武將資料檔案
        使用 EOF 結尾識別資料終止
        """
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                # Week 07: EOF 結尾處理
                if line == "EOF":
                    break
                if not line:
                    continue

                parts = line.split()
                faction, name, hp, atk, def_, spd, is_leader = parts

                # 建立 namedtuple 武將結構體
                general = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == "True"),
                )

                self.generals[name] = general

    def load_battles(self, filename):
        """讀取戰役配置檔案"""
        battles = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "EOF":
                    break
                if not line:
                    continue
                battles.append(line)
        return battles

    # ========== Week 02: sorted() 按速度排序 ==========

    def get_battle_order(self):
        """根據速度決定戰鬥順序 - 使用 sorted()"""
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    # ========== Week 02: 傷害計算 ==========

    def calculate_damage(self, attacker_name, defender_name):
        """
        計算傷害: 攻擊力 - 防禦力
        Week 02: Counter 自動累加傷害統計
        """
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]

        # 傷害公式: 攻擊 - 防禦，最低為 1
        damage = max(1, attacker.atk - defender.def_)

        # Week 02: Counter 自動累加
        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage

        return damage

    # ========== 戰鬥模擬 ==========

    def simulate_wave(self, wave_num):
        """模擬一波戰鬥"""
        # 蜀軍武將攻擊魏軍武將
        shu = [g for g in self.generals.values() if g.faction == "蜀"]
        wei = [g for g in self.generals.values() if g.faction == "魏"]

        for i, attacker in enumerate(shu[:wave_num]):
            if i < len(wei):
                self.calculate_damage(attacker.name, wei[i].name)

    def simulate_battle(self):
        """模擬三波完整戰役"""
        for wave in range(1, 4):
            self.simulate_wave(wave)

    # ========== Week 02: Counter.most_common() ==========

    def get_damage_ranking(self, top_n=5):
        """傷害排名 - Week 02: Counter.most_common()"""
        return self.stats["damage"].most_common(top_n)

    # ========== Week 02: groupby 概念 + defaultdict ==========

    def get_faction_stats(self):
        """按勢力統計傷害 - Week 02: groupby 概念"""
        faction_damage = defaultdict(int)

        for general_name, damage in self.stats["damage"].items():
            faction = self.generals[general_name].faction
            faction_damage[faction] += damage

        return dict(faction_damage)

    def get_defeated_generals(self):
        """取得戰敗將領"""
        defeated = []
        for name, total_loss in self.stats["losses"].items():
            if total_loss >= self.generals[name].hp:
                defeated.append(name)
        return defeated

    # ========== 視覺化報告 ==========

    def print_battle_start(self):
        """列印戰役開始"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║        赤壁戰役 │ 蜀吳聯軍 vs 曹操魏軍              ║")
        print("╚═══════════════════════════════════════════════════════╝\n")

        for faction in ["蜀", "吳", "魏"]:
            print(f"【{faction}軍】")
            generals = [g for g in self.generals.values() if g.faction == faction]
            for g in sorted(generals, key=lambda x: x.spd, reverse=True):
                bar = "█" * (g.hp // 10) + "░" * (10 - g.hp // 10)
                leader = " (軍師)" if g.is_leader else ""
                print(
                    f"  ⚔ {g.name:8} {bar} 攻{g.atk:2} 防{g.def_:2} 速{g.spd:2}{leader}"
                )
            print()

    def print_damage_report(self):
        """列印傷害統計報告"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║              【赤壁戰役 - 傷害統計報告】                ║")
        print("╚═══════════════════════════════════════════════════════╝\n")

        # Week 02: Counter.most_common()
        print("【傷害輸出排名 Top 5】")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            bar = "█" * (dmg // 5) + "░" * (20 - dmg // 5)
            print(f"  {i}. {name:8} {bar} {dmg:3} HP")

        print("\n【兵力損失統計】")
        for name in sorted(
            self.stats["losses"].keys(),
            key=lambda x: self.stats["losses"][x],
            reverse=True,
        )[:5]:
            loss = self.stats["losses"][name]
            defeated = "✓" if loss >= self.generals[name].hp else " "
            print(f"  {defeated} {name:8} → 損失 {loss:3} 兵力")

        # Week 02: groupby 概念
        print("\n【勢力傷害統計】")
        faction_stats = self.get_faction_stats()
        max_damage = max(faction_stats.values()) if faction_stats else 1
        for faction in ["蜀", "吳", "魏"]:
            total = faction_stats.get(faction, 0)
            ratio = int(total / max_damage * 20) if max_damage else 0
            bar = "█" * ratio + "░" * (20 - ratio)
            percentage = (
                (total / sum(faction_stats.values()) * 100) if faction_stats else 0
            )
            print(f"  {faction} {bar} {total:3} HP ({percentage:5.1f}%)")

        print("\n" + "═" * 57)

    def run_full_battle(self):
        """執行完整戰役"""
        self.print_battle_start()
        print("【開始三波戰鬥...】\n")

        self.simulate_battle()

        print("\n【戰役完成】\n")
        self.print_damage_report()


def main():
    """主程式入口"""
    game = ChibiBattle()
    game.load_generals("generals.txt")
    game.run_full_battle()


if __name__ == "__main__":
    main()
