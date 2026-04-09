"""
赤壁戰役遊戲引擎 - 簡化版
更容易記憶和理解

作者: 1112405062
日期: 2026-04-09
"""

from collections import namedtuple, Counter, defaultdict

# 用 namedtuple 簡單定義武將結構
General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattleEasy:
    """簡化版赤壁戰役引擎"""

    def __init__(self):
        self.generals = {}
        self.damage = Counter()  # 統計傷害
        self.losses = defaultdict(int)  # 統計損失

    def load(self, filename):
        """讀取武將資料"""
        with open(filename, encoding="utf-8") as f:
            for line in f:
                if line.strip() == "EOF":
                    break
                parts = line.split()
                g = General(
                    parts[0],
                    parts[1],
                    int(parts[2]),
                    int(parts[3]),
                    int(parts[4]),
                    int(parts[5]),
                    parts[6] == "True",
                )
                self.generals[parts[1]] = g

    def attack(self, attacker, defender):
        """攻擊計算 (攻-防，最小1)"""
        dmg = max(1, attacker.atk - defender.def_)
        self.damage[attacker.name] += dmg
        self.losses[defender.name] += dmg
        return dmg

    def battle(self):
        """三波戰鬥"""
        shu = [g for g in self.generals.values() if g.faction == "蜀"]
        wei = [g for g in self.generals.values() if g.faction == "魏"]
        for wave in range(3):
            if wave < len(shu) and wave < len(wei):
                self.attack(shu[wave], wei[wave])

    def ranking(self):
        """傷害排名 (使用 most_common)"""
        return self.damage.most_common(5)

    def faction_stat(self):
        """按勢力統計"""
        stat = defaultdict(int)
        for name, dmg in self.damage.items():
            stat[self.generals[name].faction] += dmg
        return dict(stat)


# 主程式
if __name__ == "__main__":
    import os, sys

    if sys.platform == "win32":
        import io

        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    # 從 solutions/1112405062/ 回推到 week-07/
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(os.path.dirname(os.path.dirname(base_dir)), "generals.txt")
    game = ChibiBattleEasy()
    game.load(path)
    game.battle()

    print("═" * 50)
    print("【赤壁戰役 - 傷害報告】")
    print("═" * 50)
    print("\n【傷害排名】")
    for i, (name, dmg) in enumerate(game.ranking(), 1):
        print(f"  {i}. {name}: {dmg}")

    print("\n【勢力統計】")
    for f in ["蜀", "吳", "魏"]:
        print(f"  {f}: {game.faction_stat().get(f, 0)}")
