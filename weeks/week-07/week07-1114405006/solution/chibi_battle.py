from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from pathlib import Path
from typing import Dict, List, Optional, Tuple

General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattle:
    """赤壁戰役遊戲引擎。"""

    def __init__(self) -> None:
        self.generals: Dict[str, General] = {}
        self.battle_config = {
            "alliance": "蜀吳",
            "enemy": "魏",
            "battle_name": "赤壁",
            "waves": 3,
        }
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }
        self.current_hp: Dict[str, int] = {}

    def _resolve_path(self, filename: str) -> Path:
        raw = Path(filename)
        if raw.is_absolute():
            return raw
        return Path(__file__).resolve().parent.parent / raw

    def load_generals(self, filename: str) -> None:
        """讀取武將資料，遇到 EOF 停止。"""
        self.generals.clear()
        self.current_hp.clear()

        path = self._resolve_path(filename)
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                if line == "EOF":
                    break

                parts = line.split()
                if len(parts) != 7:
                    raise ValueError(f"Invalid general line: {line}")

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

    def load_battle_config(self, filename: str) -> None:
        """讀取戰役設定，格式: 蜀吳 vs 魏 赤壁 3"""
        path = self._resolve_path(filename)
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                if line == "EOF":
                    break

                parts = line.split()
                if len(parts) != 5 or parts[1] != "vs":
                    raise ValueError(f"Invalid battle line: {line}")

                alliance, _, enemy, battle_name, waves = parts
                self.battle_config = {
                    "alliance": alliance,
                    "enemy": enemy,
                    "battle_name": battle_name,
                    "waves": int(waves),
                }
                return

    def reset_stats(self) -> None:
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }
        self.current_hp = {name: general.hp for name, general in self.generals.items()}

    def get_battle_order(self) -> List[General]:
        """依速度排序，速度相同時按名字確保結果穩定。"""
        return sorted(self.generals.values(), key=lambda g: (-g.spd, g.name))

    def get_alive_generals(self, factions: Optional[List[str]] = None) -> List[General]:
        result = []
        for general in self.get_battle_order():
            if self.current_hp.get(general.name, 0) <= 0:
                continue
            if factions and general.faction not in factions:
                continue
            result.append(general)
        return result

    def select_target(self, attacker: General) -> Optional[General]:
        enemy_factions = ["魏"] if attacker.faction in ["蜀", "吳"] else ["蜀", "吳"]
        candidates = self.get_alive_generals(enemy_factions)
        if not candidates:
            return None

        # 先打血量低者，血量相同則優先攻擊高威脅(攻擊高)目標
        return sorted(
            candidates,
            key=lambda g: (self.current_hp[g.name], -g.atk, g.name),
        )[0]

    def calculate_damage(self, attacker_name: str, defender_name: str) -> int:
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]

        damage = max(1, attacker.atk - defender.def_)

        # 赤壁地形優勢：蜀吳對魏 +2，魏對蜀吳 -1
        if attacker.faction in ["蜀", "吳"] and defender.faction == "魏":
            damage += 2
        elif attacker.faction == "魏" and defender.faction in ["蜀", "吳"]:
            damage = max(1, damage - 1)

        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        self.current_hp[defender_name] = max(0, self.current_hp[defender_name] - damage)
        return damage

    def simulate_wave(self, wave_num: int) -> List[Tuple[str, str, int]]:
        """模擬單波戰鬥，回傳每次攻擊事件。"""
        events: List[Tuple[str, str, int]] = []
        for attacker in self.get_alive_generals():
            target = self.select_target(attacker)
            if target is None:
                continue
            damage = self.calculate_damage(attacker.name, target.name)
            events.append((attacker.name, target.name, damage))

        return events

    def simulate_battle(self, waves: Optional[int] = None) -> None:
        if not self.generals:
            raise RuntimeError("No generals loaded")

        if waves is None:
            waves = self.battle_config.get("waves", 3)

        self.reset_stats()
        for wave in range(1, waves + 1):
            if not self.get_alive_generals(["魏"]) or not self.get_alive_generals(["蜀", "吳"]):
                break
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n: int = 5):
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self) -> Dict[str, int]:
        faction_damage = defaultdict(int)
        for general_name, damage in self.stats["damage"].items():
            faction = self.generals[general_name].faction
            faction_damage[faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self) -> List[str]:
        return [name for name, hp in self.current_hp.items() if hp <= 0]

    def print_battle_start(self) -> None:
        print("=" * 62)
        print(f"吞食天地 - {self.battle_config['battle_name']}戰役 | 蜀吳聯軍 vs 魏軍")
        print("=" * 62)
        for faction in ["蜀", "吳", "魏"]:
            print(f"[{faction}軍]")
            members = [g for g in self.get_battle_order() if g.faction == faction]
            for g in members:
                hp = self.current_hp.get(g.name, g.hp)
                filled = max(0, min(10, hp // 10))
                bar = "#" * filled + "." * (10 - filled)
                leader = " (軍師)" if g.is_leader else ""
                print(f"  {g.name:6} HP[{bar}] 攻{g.atk:2} 防{g.def_:2} 速{g.spd:2}{leader}")
            print()

    def print_damage_report(self) -> None:
        print("=" * 62)
        print("赤壁戰役 - 傷害統計報告")
        print("=" * 62)

        print("\n[傷害輸出排名 Top 5]")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            bar_len = min(20, dmg // 3)
            bar = "#" * bar_len + "." * (20 - bar_len)
            print(f"  {i}. {name:6} {bar} {dmg:3} HP")

        print("\n[兵力損失統計 Top 5]")
        losses_sorted = sorted(self.stats["losses"].items(), key=lambda item: item[1], reverse=True)
        for name, loss in losses_sorted[:5]:
            defeated = "Y" if self.current_hp[name] <= 0 else "N"
            print(f"  {name:6} loss={loss:3} defeated={defeated}")

        print("\n[勢力傷害統計]")
        faction_stats = self.get_faction_stats()
        total = sum(faction_stats.values()) or 1
        for faction in ["蜀", "吳", "魏"]:
            dmg = faction_stats.get(faction, 0)
            ratio = int((dmg / total) * 100)
            print(f"  {faction}: {dmg:3} HP ({ratio:2}%)")

    def run_full_battle(self, generals_file: str = "generals.txt", battle_file: str = "battles.txt") -> None:
        self.load_generals(generals_file)
        self.load_battle_config(battle_file)
        self.print_battle_start()
        self.simulate_battle()
        print("\n戰役完成\n")
        self.print_damage_report()


if __name__ == "__main__":
    game = ChibiBattle()
    game.run_full_battle()
