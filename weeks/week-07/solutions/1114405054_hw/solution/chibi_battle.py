from collections import Counter, defaultdict, namedtuple
from pathlib import Path

General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattle:
    """三國赤壁戰役模擬引擎。"""

    ALLY_FACTIONS = {"蜀", "吳"}
    ENEMY_FACTIONS = {"魏"}

    def __init__(self):
        self.generals = {}
        self.wave_count = 3
        self.battle_name = "赤壁"
        self.stats = {"damage": Counter(), "losses": defaultdict(int)}
        self.current_hp = {}

    def load_generals(self, filename):
        """Week 07: 讀取武將檔，遇 EOF 停止。"""
        with Path(filename).open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "EOF":
                    break
                if not line:
                    continue

                faction, name, hp, atk, def_, spd, is_leader = line.split()
                self.generals[name] = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == "True"),
                )

    def load_battle_config(self, filename):
        with Path(filename).open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "EOF":
                    break
                if not line:
                    continue
                parts = line.split()
                if len(parts) >= 5:
                    self.battle_name = parts[3]
                    self.wave_count = int(parts[4])

    def reset_battle_state(self):
        self.stats["damage"].clear()
        self.stats["losses"].clear()
        self.current_hp = {name: g.hp for name, g in self.generals.items()}

    def get_battle_order(self):
        """Week 02: sorted(key=...) 依速度決定順序。"""
        return sorted(self.generals.values(), key=lambda g: (-g.spd, g.name))

    def calculate_damage(self, attacker_name, defender_name):
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)

        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage

        if not self.current_hp:
            self.current_hp = {name: g.hp for name, g in self.generals.items()}
        self.current_hp[defender_name] = max(0, self.current_hp[defender_name] - damage)
        return damage

    def _alive_names(self, factions):
        return [
            name
            for name, g in self.generals.items()
            if g.faction in factions and self.current_hp.get(name, g.hp) > 0
        ]

    def _pick_target(self, target_factions):
        alive = self._alive_names(target_factions)
        if not alive:
            return None
        return max(alive, key=lambda n: self.generals[n].spd)

    def simulate_wave(self, wave_num):
        if not self.current_hp:
            self.current_hp = {name: g.hp for name, g in self.generals.items()}

        order = self.get_battle_order()
        for _ in range(wave_num):
            for general in order:
                if self.current_hp.get(general.name, general.hp) <= 0:
                    continue

                if general.faction in self.ALLY_FACTIONS:
                    target_name = self._pick_target(self.ENEMY_FACTIONS)
                else:
                    target_name = self._pick_target(self.ALLY_FACTIONS)

                if target_name is None:
                    return
                self.calculate_damage(general.name, target_name)

    def simulate_battle(self):
        for wave in range(1, self.wave_count + 1):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n=5):
        """Week 02: Counter.most_common() 傷害排名。"""
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self):
        """Week 02: defaultdict 按勢力彙整總傷害。"""
        faction_damage = defaultdict(int)
        for general_name, damage in self.stats["damage"].items():
            faction = self.generals[general_name].faction
            faction_damage[faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self):
        return [
            name
            for name, total_loss in self.stats["losses"].items()
            if total_loss >= self.generals[name].hp
        ]

    def print_battle_start(self):
        print("=" * 60)
        print(f"  吞食天地 - {self.battle_name}戰役 | 蜀吳聯軍 vs 曹操魏軍")
        print("=" * 60)
        for faction in ["蜀", "吳", "魏"]:
            print(f"[{faction}軍]")
            faction_generals = [g for g in self.generals.values() if g.faction == faction]
            for g in sorted(faction_generals, key=lambda x: x.spd, reverse=True):
                bar = "#" * (g.hp // 10)
                leader = " (軍師)" if g.is_leader else ""
                print(
                    f"  {g.name:<6} HP:{g.hp:>3} {bar:<12} "
                    f"ATK:{g.atk:>2} DEF:{g.def_:>2} SPD:{g.spd:>2}{leader}"
                )
            print()

    def print_damage_report(self):
        print("=" * 60)
        print("  [赤壁戰役 - 傷害統計報告]")
        print("=" * 60)

        print("\n[傷害輸出排名 Top 5]")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            bar_len = min(20, dmg // 5)
            bar = "#" * bar_len + "." * (20 - bar_len)
            print(f"  {i}. {name:<6} {bar} {dmg:>3} HP")

        print("\n[兵力損失統計 Top 5]")
        loss_sorted = sorted(self.stats["losses"].items(), key=lambda x: x[1], reverse=True)[:5]
        for name, loss in loss_sorted:
            defeated_mark = "X" if loss >= self.generals[name].hp else " "
            print(f"  [{defeated_mark}] {name:<6} loss={loss:>3}")

        print("\n[勢力傷害統計]")
        faction_stats = self.get_faction_stats()
        total = sum(faction_stats.values()) or 1
        for faction in ["蜀", "吳", "魏"]:
            dmg = faction_stats.get(faction, 0)
            ratio = dmg / total * 100
            print(f"  {faction}: {dmg:>3} HP ({ratio:>5.1f}%)")

        print("\n" + "=" * 60)

    def run_full_battle(self):
        self.print_battle_start()
        print("開始三波戰鬥...\n")
        self.reset_battle_state()
        self.simulate_battle()
        print("戰役完成。\n")
        self.print_damage_report()


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    game = ChibiBattle()
    game.load_generals(str(root / "generals.txt"))
    game.load_battle_config(str(root / "battles.txt"))
    game.run_full_battle()
