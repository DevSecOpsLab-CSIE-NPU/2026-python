from collections import Counter, defaultdict, namedtuple
from pathlib import Path

General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattle:
    """三國武將 PK 版 - 赤壁戰役遊戲引擎"""

    def __init__(self):
        self.generals = {}
        self.current_hp = {}
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }

    def _resolve_path(self, filename):
        path = Path(filename)
        if path.exists():
            return path

        base_dir = Path(__file__).resolve().parent.parent
        alt = base_dir / filename
        if alt.exists():
            return alt

        raise FileNotFoundError(f"Cannot find input file: {filename}")

    def load_generals(self, filename):
        """讀取武將資料，遇到 EOF 停止。"""
        self.generals.clear()
        self.current_hp.clear()
        self.stats["damage"].clear()
        self.stats["losses"].clear()

        path = self._resolve_path(filename)
        with open(path, "r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue
                if line == "EOF":
                    break

                parts = line.split()
                if len(parts) != 7:
                    continue

                faction, name, hp, atk, def_, spd, is_leader = parts
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
                self.current_hp[name] = general.hp

    def get_battle_order(self):
        """依速度高到低排序。"""
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name, defender_name):
        """傷害公式：max(1, 攻擊 - 防禦)。"""
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)

        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage

        if defender_name in self.current_hp:
            self.current_hp[defender_name] = max(0, self.current_hp[defender_name] - damage)

        return damage

    def _living_team(self, factions):
        living = []
        for g in self.get_battle_order():
            if g.faction in factions and self.current_hp.get(g.name, 0) > 0:
                living.append(g)
        return living

    def simulate_wave(self, wave_num):
        """模擬一波戰鬥。"""
        shu_wu_attack_index = 0
        wei_attack_index = 0

        for _ in range(max(1, wave_num)):
            for attacker in self.get_battle_order():
                if self.current_hp.get(attacker.name, 0) <= 0:
                    continue

                if attacker.faction in {"蜀", "吳"}:
                    enemies = self._living_team({"魏"})
                    if not enemies:
                        continue
                    target = enemies[shu_wu_attack_index % len(enemies)]
                    shu_wu_attack_index += 1
                else:
                    enemies = self._living_team({"蜀", "吳"})
                    if not enemies:
                        continue
                    target = enemies[wei_attack_index % len(enemies)]
                    wei_attack_index += 1

                self.calculate_damage(attacker.name, target.name)

    def simulate_battle(self):
        """模擬三波完整戰役。"""
        for wave in range(1, 4):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n=5):
        """取得傷害排行榜。"""
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self):
        """按勢力彙總傷害。"""
        faction_damage = defaultdict(int)
        for name, damage in self.stats["damage"].items():
            faction = self.generals[name].faction
            faction_damage[faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self):
        """回傳已倒下武將名單。"""
        defeated = []
        for name, hp in self.current_hp.items():
            if hp <= 0:
                defeated.append(name)
        return defeated

    def print_battle_start(self):
        """列印開戰資訊。"""
        print("+-------------------------------------------------------+")
        print("|   吞食天地 - 赤壁戰役  蜀吳聯軍 vs 曹操魏軍            |")
        print("+-------------------------------------------------------+\n")

        for faction in ["蜀", "吳", "魏"]:
            print(f"[{faction}軍]")
            team = [g for g in self.generals.values() if g.faction == faction]
            team = sorted(team, key=lambda x: x.spd, reverse=True)
            for g in team:
                bar = "#" * (g.hp // 10) + "-" * (10 - g.hp // 10)
                role = " (軍師)" if g.is_leader else ""
                print(
                    f"  {g.name:4} HP[{bar}] 攻{g.atk:2} 防{g.def_:2} 速{g.spd:2}{role}"
                )
            print()

    def print_damage_report(self):
        """列印戰後統計。"""
        print("+-------------------------------------------------------+")
        print("|                 赤壁戰役 - 傷害統計                   |")
        print("+-------------------------------------------------------+")

        print("\n[傷害輸出排名 Top 5]")
        for idx, (name, dmg) in enumerate(self.get_damage_ranking(), start=1):
            bar = "#" * min(20, dmg // 5)
            print(f"  {idx}. {name:4} {bar:<20} {dmg:3} HP")

        print("\n[兵力損失 Top 5]")
        losses_sorted = sorted(
            self.stats["losses"].items(), key=lambda item: item[1], reverse=True
        )[:5]
        for name, loss in losses_sorted:
            mark = "X" if self.current_hp.get(name, 0) <= 0 else " "
            print(f"  {mark} {name:4} -> 損失 {loss:3}，剩餘 {self.current_hp.get(name, 0):3}")

        print("\n[勢力傷害統計]")
        faction_stats = self.get_faction_stats()
        total_damage = sum(faction_stats.values()) or 1
        max_damage = max(faction_stats.values()) if faction_stats else 1
        for faction in ["蜀", "吳", "魏"]:
            value = faction_stats.get(faction, 0)
            ratio = int((value / max_damage) * 20) if max_damage else 0
            percentage = (value / total_damage) * 100
            print(f"  {faction} {'#' * ratio:<20} {value:3} HP ({percentage:5.1f}%)")

    def run_full_battle(self):
        """執行完整流程。"""
        self.print_battle_start()
        print("[開始三波戰鬥...]\n")
        self.simulate_battle()
        print("\n[戰役完成]\n")
        self.print_damage_report()


if __name__ == "__main__":
    game = ChibiBattle()
    game.load_generals("generals.txt")
    game.run_full_battle()
