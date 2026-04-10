from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from pathlib import Path

General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattle:
    """三國赤壁戰役的簡化模擬引擎。"""

    def __init__(self) -> None:
        self.generals: dict[str, General] = {}
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }

    def _resolve_input(self, filename: str | Path) -> Path:
        candidate = Path(filename)
        if candidate.is_absolute():
            return candidate

        cwd_path = Path.cwd() / candidate
        if cwd_path.exists():
            return cwd_path

        # 預設從 week-07 根目錄尋找資料檔，讓測試與執行都穩定。
        week07_path = Path(__file__).resolve().parents[1] / candidate
        return week07_path

    def load_generals(self, filename: str | Path) -> None:
        path = self._resolve_input(filename)
        with path.open("r", encoding="utf-8") as file:
            for line in file:
                text = line.strip()
                if not text:
                    continue
                if text == "EOF":
                    break

                faction, name, hp, atk, def_, spd, is_leader = text.split()
                self.generals[name] = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == "True"),
                )

    def get_battle_order(self) -> list[General]:
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name: str, defender_name: str) -> int:
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)

        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        return damage

    def _remaining_hp(self, name: str) -> int:
        return self.generals[name].hp - self.stats["losses"][name]

    def _living_names(self, names: list[str]) -> list[str]:
        return [name for name in names if self._remaining_hp(name) > 0]

    def _pick_weakest_target(self, names: list[str]) -> str | None:
        living = self._living_names(names)
        if not living:
            return None
        return min(living, key=self._remaining_hp)

    def simulate_wave(self, wave_num: int) -> None:
        shu_wu = [
            g.name
            for g in self.get_battle_order()
            if g.faction in {"蜀", "吳"} and self._remaining_hp(g.name) > 0
        ]
        wei = [
            g.name
            for g in self.get_battle_order()
            if g.faction == "魏" and self._remaining_hp(g.name) > 0
        ]

        ally_attack_count = min(len(shu_wu), wave_num + 2)
        for attacker_name in shu_wu[:ally_attack_count]:
            target_name = self._pick_weakest_target(wei)
            if target_name is None:
                break
            self.calculate_damage(attacker_name, target_name)

        wei_attack_count = min(len(wei), wave_num)
        for attacker_name in wei[:wei_attack_count]:
            target_name = self._pick_weakest_target(shu_wu)
            if target_name is None:
                break
            self.calculate_damage(attacker_name, target_name)

    def simulate_battle(self) -> None:
        for wave in range(1, 4):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n: int = 5) -> list[tuple[str, int]]:
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self) -> dict[str, int]:
        faction_damage = defaultdict(int)
        for name, damage in self.stats["damage"].items():
            faction_damage[self.generals[name].faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self) -> list[str]:
        return [name for name in self.generals if self._remaining_hp(name) <= 0]

    def print_battle_start(self) -> None:
        print("=" * 57)
        print("吞食天地 - 赤壁戰役 | 蜀吳聯軍 vs 曹操魏軍")
        print("=" * 57)

        for faction in ["蜀", "吳", "魏"]:
            print(f"\n[{faction}軍]")
            members = [g for g in self.get_battle_order() if g.faction == faction]
            for g in members:
                hp_ratio = max(0, self._remaining_hp(g.name)) / g.hp
                blocks = int(hp_ratio * 10)
                bar = "#" * blocks + "." * (10 - blocks)
                leader = " (軍師)" if g.is_leader else ""
                print(f"  {g.name:6} HP[{bar}] 攻{g.atk:2} 防{g.def_:2} 速{g.spd:2}{leader}")

    def print_damage_report(self) -> None:
        print("\n" + "=" * 57)
        print("赤壁戰役 - 傷害統計報告")
        print("=" * 57)

        print("\n[傷害輸出排名 Top 5]")
        for index, (name, damage) in enumerate(self.get_damage_ranking(), start=1):
            bar_count = min(20, max(1, damage // 3))
            bar = "#" * bar_count + "." * (20 - bar_count)
            print(f"  {index}. {name:6} {bar} {damage:3} HP")

        print("\n[勢力傷害統計]")
        faction_stats = self.get_faction_stats()
        total = sum(faction_stats.values()) or 1
        for faction in ["蜀", "吳", "魏"]:
            dmg = faction_stats.get(faction, 0)
            pct = dmg * 100 / total
            print(f"  {faction} -> {dmg:3} HP ({pct:5.1f}%)")

    def run_full_battle(self) -> None:
        self.print_battle_start()
        print("\n開始三波戰鬥...\n")
        self.simulate_battle()
        print("戰役完成。")
        self.print_damage_report()


if __name__ == "__main__":
    game = ChibiBattle()
    game.load_generals("generals.txt")
    game.run_full_battle()
