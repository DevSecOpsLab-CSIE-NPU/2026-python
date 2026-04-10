"""
赤壁戰役核心引擎。
"""

from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from pathlib import Path
from typing import Iterable

General = namedtuple("General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"])
BattleConfig = namedtuple("BattleConfig", ["allies", "enemies", "name", "waves"])


class ChibiBattle:
    """三國武將 PK 版戰役引擎。"""

    def __init__(self) -> None:
        self.generals: dict[str, General] = {}
        self.current_hp: dict[str, int] = {}
        self.battle_config: BattleConfig | None = None
        self.wave_logs: list[str] = []
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }

    def reset_battle_state(self) -> None:
        """清空戰鬥過程資料，保留已載入的武將資料。"""
        self.current_hp = {name: general.hp for name, general in self.generals.items()}
        self.wave_logs = []
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }

    def load_generals(self, filename: str | Path) -> None:
        """讀取武將資料，遇到 EOF 即停止。"""
        self.generals = {}

        with Path(filename).open("r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue
                if line == "EOF":
                    break

                faction, name, hp, atk, defense, speed, is_leader = line.split()
                general = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(defense),
                    spd=int(speed),
                    is_leader=(is_leader == "True"),
                )
                self.generals[name] = general

        self.reset_battle_state()

    def load_battle_config(self, filename: str | Path) -> None:
        """讀取戰役配置。"""
        with Path(filename).open("r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue
                if line == "EOF":
                    break

                allies_text, _, enemies_text, battle_name, waves = line.split()
                self.battle_config = BattleConfig(
                    allies=tuple(allies_text),
                    enemies=tuple(enemies_text),
                    name=battle_name,
                    waves=int(waves),
                )
                return

        raise ValueError("找不到有效的戰役配置")

    def get_battle_order(self) -> list[General]:
        """依速度由高到低決定出手順序。"""
        return sorted(
            self.generals.values(),
            key=lambda general: (-general.spd, general.faction, general.name),
        )

    def is_alive(self, general_name: str) -> bool:
        """判斷武將是否仍可戰鬥。"""
        return self.current_hp.get(general_name, 0) > 0

    def get_alive_generals(self, factions: Iterable[str]) -> list[General]:
        """取得指定勢力目前存活的武將。"""
        faction_set = set(factions)
        return [
            general
            for general in self.generals.values()
            if general.faction in faction_set and self.is_alive(general.name)
        ]

    def get_opponent_factions(self, faction: str) -> tuple[str, ...]:
        """依據戰役配置決定敵方勢力。"""
        if self.battle_config is None:
            raise ValueError("尚未載入戰役配置")

        if faction in self.battle_config.allies:
            return self.battle_config.enemies
        return self.battle_config.allies

    def choose_target(self, attacker_name: str) -> General | None:
        """選出本回合要攻擊的對象。"""
        attacker = self.generals[attacker_name]
        candidates = self.get_alive_generals(self.get_opponent_factions(attacker.faction))
        if not candidates:
            return None

        # 先打目前血量最低者，若相同則優先防禦較低，再以名字固定順序。
        return min(
            candidates,
            key=lambda general: (self.current_hp[general.name], general.def_, general.name),
        )

    def calculate_damage(self, attacker_name: str, defender_name: str) -> int:
        """計算並累加一次傷害。"""
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]

        damage = max(1, attacker.atk - defender.def_)
        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        self.current_hp[defender_name] = max(0, self.current_hp[defender_name] - damage)
        return damage

    def simulate_wave(self, wave_num: int) -> None:
        """模擬一波戰鬥。"""
        if self.battle_config is None:
            raise ValueError("尚未載入戰役配置")

        self.wave_logs.append(f"第 {wave_num} 波戰鬥")

        for attacker in self.get_battle_order():
            if not self.is_alive(attacker.name):
                continue

            target = self.choose_target(attacker.name)
            if target is None:
                continue

            damage = self.calculate_damage(attacker.name, target.name)
            self.wave_logs.append(
                f"{attacker.faction} {attacker.name} 攻擊 {target.faction} {target.name}，造成 {damage} 點傷害"
            )

            if not self.is_alive(target.name):
                self.wave_logs.append(f"{target.faction} {target.name} 戰敗")

    def simulate_battle(self) -> None:
        """模擬完整戰役。"""
        if self.battle_config is None:
            raise ValueError("尚未載入戰役配置")

        self.reset_battle_state()
        for wave in range(1, self.battle_config.waves + 1):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n: int = 5) -> list[tuple[str, int]]:
        """取得傷害排名。"""
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self) -> dict[str, int]:
        """按勢力累加傷害。"""
        faction_damage: defaultdict[str, int] = defaultdict(int)

        for general_name, damage in self.stats["damage"].items():
            faction = self.generals[general_name].faction
            faction_damage[faction] += damage

        return dict(faction_damage)

    def get_defeated_generals(self) -> list[str]:
        """回傳本場戰鬥中已戰敗的武將。"""
        defeated = [name for name, hp in self.current_hp.items() if hp <= 0]
        return sorted(defeated)

    def make_hp_bar(self, current_hp: int, max_hp: int, width: int = 10) -> str:
        """把血量轉成簡單的 ASCII 條。"""
        if max_hp <= 0:
            return "." * width

        filled = int(round(current_hp / max_hp * width))
        filled = max(0, min(width, filled))
        return "#" * filled + "." * (width - filled)

    def generate_battle_start(self) -> str:
        """產生戰役開始畫面。"""
        if self.battle_config is None:
            raise ValueError("尚未載入戰役配置")

        lines = [
            "=========================================================",
            f"吞食天地 - {self.battle_config.name}戰役 | 蜀吳聯軍 vs 曹操魏軍",
            "=========================================================",
            "",
        ]

        for faction in ("蜀", "吳", "魏"):
            lines.append(f"【{faction}軍】")
            faction_generals = sorted(
                [general for general in self.generals.values() if general.faction == faction],
                key=lambda general: (-general.spd, general.name),
            )

            for general in faction_generals:
                bar = self.make_hp_bar(self.current_hp[general.name], general.hp)
                leader = " (軍師)" if general.is_leader else ""
                lines.append(
                    f"  {general.name:4} {bar} HP{self.current_hp[general.name]:3}/{general.hp:3} "
                    f"攻{general.atk:2} 防{general.def_:2} 速{general.spd:2}{leader}"
                )
            lines.append("")

        return "\n".join(lines).rstrip()

    def generate_damage_report(self) -> str:
        """產生戰後統計報告。"""
        lines = [
            "=========================================================",
            "赤壁戰役 - 傷害統計報告",
            "=========================================================",
            "",
            "【傷害輸出排名】",
        ]

        for index, (name, damage) in enumerate(self.get_damage_ranking(), start=1):
            bar = "#" * min(20, damage // 5) + "." * max(0, 20 - damage // 5)
            lines.append(f"  {index}. {name:4} {bar} {damage:3} HP")

        lines.append("")
        lines.append("【兵力損失統計】")
        loss_ranking = sorted(
            self.stats["losses"].items(),
            key=lambda item: (-item[1], item[0]),
        )[:5]
        for name, loss in loss_ranking:
            marker = "*" if name in self.get_defeated_generals() else " "
            lines.append(f"  {marker} {name:4} → 損失 {loss:3} 兵力，剩餘 {self.current_hp[name]:3} HP")

        lines.append("")
        lines.append("【勢力傷害統計】")
        faction_stats = self.get_faction_stats()
        total_damage = sum(faction_stats.values()) or 1
        max_damage = max(faction_stats.values()) if faction_stats else 1

        for faction in ("蜀", "吳", "魏"):
            damage = faction_stats.get(faction, 0)
            ratio = int(damage / max_damage * 20) if max_damage else 0
            bar = "#" * ratio + "." * (20 - ratio)
            percentage = damage / total_damage * 100
            lines.append(f"  {faction} {bar} {damage:3} HP ({percentage:5.1f}%)")

        lines.append("")
        lines.append("【戰敗名單】")
        defeated = self.get_defeated_generals()
        if defeated:
            lines.append("  " + "、".join(defeated))
        else:
            lines.append("  無")

        return "\n".join(lines)

    def run_full_battle(self, print_output: bool = True) -> str:
        """執行完整戰役並輸出文字報告。"""
        self.simulate_battle()
        sections = [
            self.generate_battle_start(),
            "",
            "【開始三波戰鬥】",
            *self.wave_logs,
            "",
            "【戰役完成】",
            "",
            self.generate_damage_report(),
        ]
        report = "\n".join(sections)
        if print_output:
            print(report)
        return report


def default_data_path(filename: str) -> Path:
    """取得和目前檔案同層的資料檔路徑。"""
    return Path(__file__).resolve().parent / filename


def main() -> None:
    game = ChibiBattle()
    game.load_generals(default_data_path("generals.txt"))
    game.load_battle_config(default_data_path("battles.txt"))
    game.run_full_battle(print_output=True)


if __name__ == "__main__":
    main()
