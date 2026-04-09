"""
赤壁戰役遊戲引擎
三國武將 PK 版 - Week 02 & Week 07 統合

日期: 2026-04-09

使用技術:
- Week 02: namedtuple, Counter, defaultdict, sorted(key=...)
- Week 07: 檔案 I/O, EOF 輸入處理
"""

from collections import namedtuple, Counter, defaultdict

# Week 02: namedtuple 結構體 - 定义武將資料結構
General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattle:
    """吞食天地 - 赤壁戰役遊戲引擎"""

    def __init__(self):
        """初始化遊戲引擎"""
        self.generals = {}  # 武將字典 {名字: General物件}

        # Week 02: Counter 和 defaultdict 用於統計
        self.stats = {
            "damage": Counter(),  # 傷害統計 (自動累加)
            "losses": defaultdict(int),  # 兵力損失 (自動初始化為 0)
        }

    def load_generals(self, filename):
        """
        Week 07: 讀取武將資料檔案
        檔案格式: 陣營 名字 HP 攻擊 防禦 速度 是否領袖
        結束標記: EOF
        """
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                # EOF 結尾處理 (Week 07 重點)
                if line == "EOF":
                    break
                if not line:
                    continue

                # 解析一行資料
                parts = line.split()
                faction, name, hp, atk, def_, spd, is_leader = parts

                # 建立 namedtuple 結構體 (Week 02)
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

    def get_battle_order(self):
        """
        Week 02: sorted(key=...) 按速度決定戰鬥順序
        速度高的武將先行動
        """
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name, defender_name):
        """
        計算傷害公式: 攻擊力 - 防禦力 (最小值為 1)
        使用 Week 02: Counter 自動累加傷害統計
        """
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]

        # 傷害計算 (最低 1 點)
        damage = max(1, attacker.atk - defender.def_)

        # Week 02: Counter 自動累加
        self.stats["damage"][attacker_name] += damage
        # Week 02: defaultdict(int) 自動初始化為 0
        self.stats["losses"][defender_name] += damage

        return damage

    def simulate_wave(self, wave_num):
        """
        模擬一波戰鬥
        簡化規則: 蜀軍武將依序攻擊魏軍武將
        """
        order = self.get_battle_order()

        # 取得各陣營武將
        shu = [g for g in self.generals.values() if g.faction == "蜀"]
        wei = [g for g in self.generals.values() if g.faction == "魏"]

        # 蜀軍武將依序攻擊魏軍
        for i, attacker in enumerate(shu[:wave_num]):
            if i < len(wei):
                self.calculate_damage(attacker.name, wei[i].name)

    def simulate_battle(self):
        """模擬三波完整戰役"""
        for wave in range(1, 4):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n=5):
        """
        Week 02: Counter.most_common() 傷害排名
        返回傷害最高的 top_n 位武將
        """
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self):
        """
        Week 02: defaultdict + groupby 概念
        按勢力統計總傷害
        """
        faction_damage = defaultdict(int)

        for general_name, damage in self.stats["damage"].items():
            faction = self.generals[general_name].faction
            faction_damage[faction] += damage

        return dict(faction_damage)

    def get_defeated_generals(self):
        """
        取得戰敗將領 (HP <= 損失兵力)
        """
        defeated = []
        for name, total_loss in self.stats["losses"].items():
            if name in self.generals:
                if total_loss >= self.generals[name].hp:
                    defeated.append(name)
        return defeated

    def print_battle_start(self):
        """列印戰役開始資訊 (ASCII 視覺化)"""
        print("╔═══════════════════════════════════════════════════════╗")
        print("║        吞食天地 - 赤壁戰役 │ 蜀吳聯軍 vs 曹操魏軍      ║")
        print("╚═══════════════════════════════════════════════════════╝\n")

        # 列印各武將狀態
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
        """列印傷害統計報告 (ASCII 視覺化)"""
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
            if name in self.generals:
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
        """執行完整戰役流程"""
        self.print_battle_start()
        print("【開始三波戰鬥...】\n")

        self.simulate_battle()

        print("\n【戰役完成】\n")
        self.print_damage_report()


# 主程式入口
if __name__ == "__main__":
    import os
    import sys

    # 設定 UTF-8 編碼輸出 (解決 Windows PowerShell 中文顯示問題)
    if sys.platform == "win32":
        import io

        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    # 取得 generals.txt 路徑 (從 solutions/1112405062/ 回推到 week-07/)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    generals_file = os.path.join(
        os.path.dirname(os.path.dirname(base_dir)), "generals.txt"
    )

    # 建立遊戲實例並執行
    game = ChibiBattle()
    game.load_generals(generals_file)
    game.run_full_battle()
