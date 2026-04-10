from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from pathlib import Path
from typing import Dict, List, Tuple

General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattle:
    """Week 02 + Week 07 integrated battle engine."""

    def __init__(self) -> None:
        self.generals: Dict[str, General] = {}
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }

    def reset_stats(self) -> None:
        self.stats["damage"].clear()
        self.stats["losses"].clear()

    def load_generals(self, filename: str) -> None:
        """Read generals from text file and stop on EOF."""
        path = Path(filename)
        with path.open("r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue
                if line == "EOF":
                    break

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

    def get_battle_order(self) -> List[General]:
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def _hp_left(self, name: str) -> int:
        return self.generals[name].hp - self.stats["losses"][name]

    def _is_alive(self, name: str) -> bool:
        return self._hp_left(name) > 0

    def calculate_damage(self, attacker_name: str, defender_name: str) -> int:
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]

        base_damage = max(1, attacker.atk - defender.def_)
        if attacker.is_leader:
            base_damage += 2

        self.stats["damage"][attacker_name] += base_damage
        self.stats["losses"][defender_name] += base_damage
        return base_damage

    def _pick_target(self, attacker: General) -> str | None:
        if attacker.faction in {"蜀", "吳"}:
            enemies = [
                g.name
                for g in self.generals.values()
                if g.faction == "魏" and self._is_alive(g.name)
            ]
        else:
            enemies = [
                g.name
                for g in self.generals.values()
                if g.faction in {"蜀", "吳"} and self._is_alive(g.name)
            ]

        if not enemies:
            return None

        # Focus fire on the enemy with lowest remaining HP.
        return min(enemies, key=self._hp_left)

    def simulate_wave(self, wave_num: int) -> None:
        if wave_num < 1:
            return

        for attacker in self.get_battle_order():
            if not self._is_alive(attacker.name):
                continue
            target_name = self._pick_target(attacker)
            if target_name is None:
                continue
            self.calculate_damage(attacker.name, target_name)

    def simulate_battle(self) -> None:
        for wave in range(1, 4):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n: int = 5) -> List[Tuple[str, int]]:
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self) -> Dict[str, int]:
        faction_damage: defaultdict[str, int] = defaultdict(int)
        for name, damage in self.stats["damage"].items():
            faction_damage[self.generals[name].faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self) -> List[str]:
        return [name for name in self.generals if not self._is_alive(name)]

    def print_battle_start(self) -> None:
        print("=" * 60)
        print("Three Kingdoms Battle Engine - Chibi")
        print("=" * 60)
        for faction in ["蜀", "吳", "魏"]:
            print(f"[{faction}]")
            for g in sorted(
                [x for x in self.generals.values() if x.faction == faction],
                key=lambda x: x.spd,
                reverse=True,
            ):
                hp_bar = "#" * max(1, g.hp // 10)
                leader_tag = " (Leader)" if g.is_leader else ""
                print(
                    f"  {g.name:<6} HP:{g.hp:<3} ATK:{g.atk:<2} "
                    f"DEF:{g.def_:<2} SPD:{g.spd:<2} {hp_bar}{leader_tag}"
                )
        print()

    def print_damage_report(self) -> None:
        print("=" * 60)
        print("Damage Ranking Top 5")
        print("=" * 60)
        for idx, (name, dmg) in enumerate(self.get_damage_ranking(), start=1):
            print(f"{idx}. {name:<8} {dmg:>3}")

        print("\nFaction Damage")
        faction_stats = self.get_faction_stats()
        for faction in ["蜀", "吳", "魏"]:
            print(f"{faction}: {faction_stats.get(faction, 0)}")

        print("\nDefeated")
        defeated = self.get_defeated_generals()
        if defeated:
            print(", ".join(defeated))
        else:
            print("None")

    def run_full_battle(self) -> None:
        self.print_battle_start()
        self.simulate_battle()
        self.print_damage_report()


if __name__ == "__main__":
    base = Path(__file__).parent
    game = ChibiBattle()
    game.load_generals(str(base / "generals.txt"))
    game.run_full_battle()
