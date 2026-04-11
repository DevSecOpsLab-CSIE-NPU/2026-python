from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from pathlib import Path
import argparse


General = namedtuple("General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"])

BASE_DIR = Path(__file__).resolve().parent


class ChibiBattleEasy:
    """比較好記的版本，保留同一份資料結構與戰鬥流程。"""

    def __init__(self) -> None:
        self.generals: dict[str, General] = {}
        self.max_waves = 3
        self.stats = {"damage": Counter(), "losses": defaultdict(int)}
        self.current_hp: dict[str, int] = {}
        self.finished_waves = 0

    def load_generals(self, file_name: str | Path = BASE_DIR / "generals.txt") -> None:
        self.generals.clear()
        with open(file_name, "r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if line == "EOF":
                    break
                if not line:
                    continue
                faction, name, hp, atk, def_, spd, is_leader = line.split()
                self.generals[name] = General(faction, name, int(hp), int(atk), int(def_), int(spd), is_leader == "True")

        self.current_hp = {name: general.hp for name, general in self.generals.items()}
        self.stats = {"damage": Counter(), "losses": defaultdict(int)}
        self.finished_waves = 0

    def get_battle_order(self) -> list[General]:
        return sorted(self.generals.values(), key=lambda general: (general.spd, general.atk), reverse=True)

    def get_living(self, factions: set[str]) -> list[General]:
        return [general for general in self.generals.values() if general.faction in factions and self.current_hp[general.name] > 0]

    def choose_target(self, attacker: General) -> General | None:
        enemy_factions = {"魏"} if attacker.faction in {"蜀", "吳"} else {"蜀", "吳"}
        enemies = self.get_living(enemy_factions)
        if not enemies:
            return None
        return min(enemies, key=lambda general: (self.current_hp[general.name], general.def_, general.name))

    def calculate_damage(self, attacker_name: str, defender_name: str, wave_num: int = 1) -> int:
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        extra = 2 if attacker.faction in {"蜀", "吳"} else 0
        extra += 2 if attacker.is_leader else 0
        damage = max(1, attacker.atk + extra + wave_num - defender.def_)
        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        self.current_hp[defender_name] = max(0, self.current_hp[defender_name] - damage)
        return damage

    def simulate_wave(self, wave_num: int) -> list[str]:
        logs: list[str] = []
        for attacker in self.get_battle_order():
            if self.current_hp[attacker.name] <= 0:
                continue
            target = self.choose_target(attacker)
            if target is None:
                break
            damage = self.calculate_damage(attacker.name, target.name, wave_num)
            logs.append(f"{attacker.name} -> {target.name}: {damage} ({self.current_hp[target.name]} HP)")
        self.finished_waves = max(self.finished_waves, wave_num)
        return logs

    def simulate_battle(self) -> None:
        while self.finished_waves < self.max_waves and self.get_winner() == "未分勝負":
            self.simulate_wave(self.finished_waves + 1)

    def get_damage_ranking(self, top_n: int = 5) -> list[tuple[str, int]]:
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self) -> dict[str, int]:
        answer = defaultdict(int)
        for name, damage in self.stats["damage"].items():
            answer[self.generals[name].faction] += damage
        return dict(answer)

    def get_defeated_generals(self) -> list[str]:
        return [name for name, hp in self.current_hp.items() if hp == 0]

    def get_winner(self) -> str:
        allies_alive = bool(self.get_living({"蜀", "吳"}))
        wei_alive = bool(self.get_living({"魏"}))
        if allies_alive and not wei_alive:
            return "蜀吳聯軍"
        if wei_alive and not allies_alive:
            return "曹魏軍"

        if self.finished_waves >= self.max_waves:
            allies_hp = sum(
                self.current_hp[general.name]
                for general in self.generals.values()
                if general.faction in {"蜀", "吳"}
            )
            wei_hp = sum(
                self.current_hp[general.name]
                for general in self.generals.values()
                if general.faction == "魏"
            )
            if allies_hp > wei_hp:
                return "蜀吳聯軍"
            if wei_hp > allies_hp:
                return "曹魏軍"

        return "未分勝負"

    def render_status(self) -> str:
        lines = []
        for faction in ("蜀", "吳", "魏"):
            lines.append(f"【{faction}軍】")
            for general in [g for g in self.get_battle_order() if g.faction == faction]:
                lines.append(f"  {general.name}: {self.current_hp[general.name]}/{general.hp}")
        return "\n".join(lines)

    def run_full_battle(self) -> str:
        self.simulate_battle()
        ranking = "\n".join(f"  {name}: {damage}" for name, damage in self.get_damage_ranking())
        return "\n".join([
            "赤壁戰役簡單版",
            self.render_status(),
            "【傷害排名】",
            ranking,
            f"勝方：{self.get_winner()}",
        ])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="赤壁戰役簡單版")
    parser.add_argument("--auto", action="store_true", help="直接自動打完")
    parser.add_argument("--status", action="store_true", help="只顯示狀態")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    game = ChibiBattleEasy()
    game.load_generals()

    if args.status:
        print(game.render_status())
        return

    if args.auto:
        print(game.run_full_battle())
        return

    print("輸入 Enter 依序打三波，輸入 q 離開。")
    while game.finished_waves < game.max_waves and game.get_winner() == "未分勝負":
        answer = input("下一步：").strip().lower()
        if answer == "q":
            break
        print("\n".join(game.simulate_wave(game.finished_waves + 1)))
    print(game.run_full_battle())


if __name__ == "__main__":
    main()