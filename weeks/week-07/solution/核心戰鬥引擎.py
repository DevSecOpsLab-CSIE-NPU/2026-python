from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

General = namedtuple("General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"])


@dataclass(frozen=True)
class AttackEvent:
    wave: int
    attacker: str
    defender: str
    damage: int


class ChibiBattle:
    """赤壁戰役模擬引擎。"""

    def __init__(self) -> None:
        self.generals: Dict[str, General] = {}
        self.current_hp: Dict[str, int] = {}
        self.attack_log: List[AttackEvent] = []
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }

    def load_generals(self, filename: str | Path) -> None:
        """從檔案讀取武將資料，遇到 EOF 即停止。"""
        self.generals.clear()
        self.current_hp.clear()
        self.attack_log.clear()
        self.stats["damage"].clear()
        self.stats["losses"].clear()

        file_path = Path(filename)
        if not file_path.exists():
            raise FileNotFoundError(f"找不到武將檔案: {file_path}")

        with file_path.open("r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue
                if line == "EOF":
                    break

                parts = line.split()
                if len(parts) != 7:
                    raise ValueError(f"資料格式錯誤: {line}")

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

    def get_battle_order(self) -> List[General]:
        """依速度由高到低排序，速度相同則依名字排序保持穩定。"""
        return sorted(self.generals.values(), key=lambda g: (-g.spd, g.name))

    def _alive(self, names: Iterable[str]) -> List[str]:
        return [name for name in names if self.current_hp.get(name, 0) > 0]

    def _faction_names(self, faction: str) -> List[str]:
        return [g.name for g in self.generals.values() if g.faction == faction]

    def _pick_target(self, enemy_names: List[str]) -> str:
        alive = self._alive(enemy_names)
        if not alive:
            raise ValueError("沒有可攻擊的敵方單位")
        return min(alive, key=lambda name: (self.current_hp[name], name))

    def calculate_damage(self, attacker_name: str, defender_name: str, wave: int | None = None) -> int:
        """計算傷害並更新統計。"""
        if attacker_name not in self.generals or defender_name not in self.generals:
            raise KeyError("攻擊方或防守方不存在")

        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        base = max(1, attacker.atk - defender.def_)

        # 軍師在赤壁可提供策略加成，傷害 +2。
        damage = base + 2 if attacker.is_leader else base

        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        self.current_hp[defender_name] = max(0, self.current_hp[defender_name] - damage)

        self.attack_log.append(
            AttackEvent(
                wave=wave if wave is not None else 0,
                attacker=attacker_name,
                defender=defender_name,
                damage=damage,
            )
        )
        return damage

    def simulate_wave(self, wave_num: int) -> None:
        """單波戰鬥: 每方最多派出 wave_num 名存活武將。"""
        if wave_num <= 0:
            raise ValueError("wave_num 必須大於 0")

        allied = self._alive(self._faction_names("蜀") + self._faction_names("吳"))
        wei = self._alive(self._faction_names("魏"))
        if not allied or not wei:
            return

        order = [g for g in self.get_battle_order() if self.current_hp[g.name] > 0]
        participated = 0

        for general in order:
            if participated >= wave_num * 2:
                break
            if self.current_hp[general.name] <= 0:
                continue

            if general.faction in {"蜀", "吳"}:
                if not self._alive(wei):
                    break
                target = self._pick_target(wei)
                self.calculate_damage(general.name, target, wave=wave_num)
                participated += 1
            elif general.faction == "魏":
                if not self._alive(allied):
                    break
                target = self._pick_target(allied)
                self.calculate_damage(general.name, target, wave=wave_num)
                participated += 1

    def simulate_battle(self, waves: int = 3) -> None:
        for wave in range(1, waves + 1):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n: int = 5) -> List[Tuple[str, int]]:
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self) -> Dict[str, int]:
        faction_damage: defaultdict[str, int] = defaultdict(int)
        for name, dmg in self.stats["damage"].items():
            faction_damage[self.generals[name].faction] += dmg
        return dict(faction_damage)

    def get_defeated_generals(self) -> List[str]:
        defeated = [name for name, hp in self.current_hp.items() if hp <= 0]
        return sorted(defeated)

    def print_battle_start(self) -> None:
        print("=" * 58)
        print("赤壁之戰開打: 蜀吳聯軍 vs 曹操魏軍")
        print("=" * 58)
        for faction in ["蜀", "吳", "魏"]:
            print(f"[{faction}軍]")
            for general in [g for g in self.get_battle_order() if g.faction == faction]:
                role = "軍師" if general.is_leader else "武將"
                print(
                    f"  {general.name:<4} HP:{general.hp:>3} 攻:{general.atk:>2} 防:{general.def_:>2} 速:{general.spd:>2} {role}"
                )
            print()

    def print_damage_report(self) -> None:
        print("=" * 58)
        print("戰後統計")
        print("=" * 58)
        print("傷害排行 Top 5")
        for idx, (name, dmg) in enumerate(self.get_damage_ranking(5), 1):
            print(f"  {idx}. {name:<6} {dmg:>3}")

        print("\n勢力傷害")
        for faction in ["蜀", "吳", "魏"]:
            print(f"  {faction}: {self.get_faction_stats().get(faction, 0)}")

        defeated = self.get_defeated_generals()
        print("\n戰敗武將")
        if defeated:
            print("  " + "、".join(defeated))
        else:
            print("  無")

    def run_full_battle(self, waves: int = 3) -> None:
        self.print_battle_start()
        self.simulate_battle(waves=waves)
        self.print_damage_report()


def _default_input_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / filename


def _resolve_generals_path() -> Path:
    base = Path(__file__).resolve().parent.parent
    for name in ("generals.txt", "角色資料主檔.txt"):
        path = base / name
        if path.exists() and path.is_file():
            return path
    return base / "generals.txt"


if __name__ == "__main__":
    game = ChibiBattle()
    game.load_generals(_resolve_generals_path())
    game.run_full_battle(waves=3)
