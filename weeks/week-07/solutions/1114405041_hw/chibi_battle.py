from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from pathlib import Path
from typing import Iterable
import argparse


General = namedtuple(
    "General",
    ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"],
)

BattleConfig = namedtuple("BattleConfig", ["alliance", "enemy", "battlefield", "waves"])

BASE_DIR = Path(__file__).resolve().parent
GENERALS_FILE = BASE_DIR / "generals.txt"
BATTLES_FILE = BASE_DIR / "battles.txt"


class ChibiBattle:
    """赤壁戰役的可互動模擬器。"""

    def __init__(self) -> None:
        self.generals: dict[str, General] = {}
        self.battle_config: BattleConfig | None = None
        self.stats: dict[str, Counter[str] | defaultdict[str, int]] = {}
        self.current_hp: dict[str, int] = {}
        self.wave_logs: list[list[str]] = []
        self.completed_waves = 0
        self.reset_runtime_state()

    def reset_runtime_state(self) -> None:
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
            "defeats": Counter(),
        }
        self.current_hp = {
            general.name: general.hp for general in self.generals.values()
        }
        self.wave_logs = []
        self.completed_waves = 0

    def load_generals(self, filename: str | Path = GENERALS_FILE) -> None:
        self.generals = {}

        with open(filename, "r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
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
                    is_leader=is_leader == "True",
                )

        self.reset_runtime_state()

    def load_battle_config(self, filename: str | Path = BATTLES_FILE) -> None:
        with open(filename, "r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if line == "EOF":
                    break
                if not line:
                    continue

                alliance, _, enemy, battlefield, waves = line.split()
                self.battle_config = BattleConfig(
                    alliance=alliance,
                    enemy=enemy,
                    battlefield=battlefield,
                    waves=int(waves),
                )
                return

        raise ValueError("找不到有效的戰役設定")

    def setup(self) -> None:
        self.load_generals()
        self.load_battle_config()

    def get_battle_order(self) -> list[General]:
        return sorted(
            self.generals.values(),
            key=lambda general: (general.spd, general.is_leader, general.atk, general.name),
            reverse=True,
        )

    def get_team(self, faction: str) -> str:
        return "聯軍" if faction in {"蜀", "吳"} else "魏軍"

    def get_living_generals(self, factions: Iterable[str] | None = None) -> list[General]:
        selected = self.generals.values()
        if factions is not None:
            faction_set = set(factions)
            selected = [general for general in selected if general.faction in faction_set]

        return [general for general in selected if self.current_hp.get(general.name, 0) > 0]

    def choose_target(self, attacker: General) -> General | None:
        enemy_factions = {"魏"} if attacker.faction in {"蜀", "吳"} else {"蜀", "吳"}
        enemies = self.get_living_generals(enemy_factions)
        if not enemies:
            return None

        return min(
            enemies,
            key=lambda general: (
                self.current_hp[general.name],
                not general.is_leader,
                general.def_,
                general.spd,
                general.name,
            ),
        )

    def calculate_damage(self, attacker_name: str, defender_name: str, wave_num: int = 1) -> int:
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]

        morale_bonus = 2 if attacker.faction in {"蜀", "吳"} else 0
        leader_bonus = 3 if attacker.is_leader else 0
        wave_bonus = max(0, wave_num - 1)
        damage = max(1, attacker.atk + morale_bonus + leader_bonus + wave_bonus - defender.def_)

        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        self.current_hp[defender_name] = max(0, self.current_hp[defender_name] - damage)
        if self.current_hp[defender_name] == 0:
            self.stats["defeats"][attacker_name] += 1

        return damage

    def simulate_wave(self, wave_num: int) -> list[str]:
        if self.battle_config is None:
            raise ValueError("尚未載入戰役設定")

        if self.is_battle_over():
            return []

        events: list[str] = []
        for attacker in self.get_battle_order():
            if self.current_hp[attacker.name] <= 0:
                continue

            target = self.choose_target(attacker)
            if target is None:
                break

            damage = self.calculate_damage(attacker.name, target.name, wave_num)
            hp_left = self.current_hp[target.name]
            events.append(
                f"{attacker.name} 對 {target.name} 造成 {damage} 傷害，{target.name} 剩餘 {hp_left} HP"
            )
            if hp_left == 0:
                events.append(f"{target.name} 已退場")

            if self.is_battle_over():
                break

        self.completed_waves = max(self.completed_waves, wave_num)
        self.wave_logs.append(events)
        return events

    def simulate_battle(self) -> None:
        if self.battle_config is None:
            raise ValueError("尚未載入戰役設定")

        while self.completed_waves < self.battle_config.waves and not self.is_battle_over():
            self.simulate_wave(self.completed_waves + 1)

    def get_damage_ranking(self, top_n: int = 5) -> list[tuple[str, int]]:
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self) -> dict[str, int]:
        faction_damage: defaultdict[str, int] = defaultdict(int)
        for general_name, damage in self.stats["damage"].items():
            faction_damage[self.generals[general_name].faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self) -> list[str]:
        return [
            name for name, hp in self.current_hp.items() if hp == 0
        ]

    def is_battle_over(self) -> bool:
        allied_alive = any(general.faction in {"蜀", "吳"} for general in self.get_living_generals())
        wei_alive = any(general.faction == "魏" for general in self.get_living_generals())
        return not allied_alive or not wei_alive

    def get_winner(self) -> str:
        allied_alive = any(general.faction in {"蜀", "吳"} for general in self.get_living_generals())
        wei_alive = any(general.faction == "魏" for general in self.get_living_generals())
        if allied_alive and not wei_alive:
            return "蜀吳聯軍"
        if wei_alive and not allied_alive:
            return "曹魏軍"

        if self.battle_config is not None and self.completed_waves >= self.battle_config.waves:
            allied_hp = sum(
                self.current_hp[general.name]
                for general in self.generals.values()
                if general.faction in {"蜀", "吳"}
            )
            wei_hp = sum(
                self.current_hp[general.name]
                for general in self.generals.values()
                if general.faction == "魏"
            )
            if allied_hp > wei_hp:
                return "蜀吳聯軍"
            if wei_hp > allied_hp:
                return "曹魏軍"

        return "未分勝負"

    def render_hp_bar(self, name: str, width: int = 10) -> str:
        general = self.generals[name]
        remaining = self.current_hp[name]
        filled = round(remaining / general.hp * width) if general.hp else 0
        filled = max(0, min(width, filled))
        return "█" * filled + "░" * (width - filled)

    def get_status_lines(self) -> list[str]:
        lines: list[str] = []
        for faction in ("蜀", "吳", "魏"):
            lines.append(f"【{faction}軍】")
            faction_generals = [
                general for general in self.get_battle_order() if general.faction == faction
            ]
            for general in faction_generals:
                leader = " 軍師" if general.is_leader else ""
                lines.append(
                    f"  {general.name:4} {self.render_hp_bar(general.name)} "
                    f"HP {self.current_hp[general.name]:>3}/{general.hp:<3}"
                    f" 攻{general.atk:>2} 防{general.def_:>2} 速{general.spd:>2}{leader}"
                )
            lines.append("")
        return lines[:-1]

    def get_damage_report_lines(self) -> list[str]:
        faction_stats = self.get_faction_stats()
        total_damage = sum(faction_stats.values()) or 1
        lines = [
            "╔═══════════════════════════════════════════════════════╗",
            "║              【赤壁戰役 - 傷害統計報告】                ║",
            "╚═══════════════════════════════════════════════════════╝",
            "",
            "【傷害輸出排名 Top 5】",
        ]

        for index, (name, damage) in enumerate(self.get_damage_ranking(), start=1):
            lines.append(f"  {index}. {name:4} {self.render_hp_bar(name, 12)} {damage:>3} HP")

        lines.append("")
        lines.append("【勢力傷害統計】")
        for faction in ("蜀", "吳", "魏"):
            damage = faction_stats.get(faction, 0)
            percentage = damage / total_damage * 100
            bar = "█" * int(round(percentage / 10))
            lines.append(f"  {faction} {bar:<10} {damage:>3} HP ({percentage:>5.1f}%)")

        defeated = self.get_defeated_generals()
        lines.append("")
        lines.append(f"【戰果】 勝方：{self.get_winner()}，退場武將：{', '.join(defeated) if defeated else '無'}")
        return lines

    def run_full_battle(self) -> str:
        header = [
            "╔═══════════════════════════════════════════════════════╗",
            "║        吞食天地 - 赤壁戰役 │ 蜀吳聯軍 vs 曹操魏軍      ║",
            "╚═══════════════════════════════════════════════════════╝",
            "",
        ]
        body = self.get_status_lines() + ["", "【開始三波戰鬥】", ""]

        self.simulate_battle()

        for index, events in enumerate(self.wave_logs, start=1):
            body.append(f"《第 {index} 波》")
            body.extend(f"  - {event}" for event in events)
            body.append("")

        footer = self.get_damage_report_lines()
        return "\n".join(header + body + footer)

    def play_interactive(self) -> None:
        if self.battle_config is None:
            self.setup()

        while True:
            print("\n=== 赤壁戰役互動模式 ===")
            print("1. 查看武將狀態")
            print("2. 進行下一波戰鬥")
            print("3. 自動完成整場戰役")
            print("4. 查看傷害報告")
            print("5. 重置戰役")
            print("0. 離開")
            choice = input("請輸入選項：").strip()

            if choice == "1":
                print("\n".join(self.get_status_lines()))
            elif choice == "2":
                if self.battle_config is None:
                    raise ValueError("尚未載入戰役設定")
                if self.completed_waves >= self.battle_config.waves or self.is_battle_over():
                    print("戰役已結束。")
                    continue
                events = self.simulate_wave(self.completed_waves + 1)
                print("\n".join(events) if events else "本波無事件。")
            elif choice == "3":
                print(self.run_full_battle())
            elif choice == "4":
                print("\n".join(self.get_damage_report_lines()))
            elif choice == "5":
                self.reset_runtime_state()
                print("已重置戰役。")
            elif choice == "0":
                break
            else:
                print("請輸入 0 到 5 之間的選項。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="赤壁戰役遊戲引擎")
    parser.add_argument("--auto", action="store_true", help="直接跑完整場戰役")
    parser.add_argument("--status", action="store_true", help="只顯示目前武將狀態")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    game = ChibiBattle()
    game.setup()

    if args.status:
        print("\n".join(game.get_status_lines()))
        return

    if args.auto:
        print(game.run_full_battle())
        return

    game.play_interactive()


if __name__ == "__main__":
    main()