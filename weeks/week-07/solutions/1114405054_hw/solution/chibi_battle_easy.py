from pathlib import Path

from chibi_battle import ChibiBattle


class EasyChibiBattle(ChibiBattle):
    """簡化版入口。"""

    def quick_start(self):
        root = Path(__file__).resolve().parent.parent
        self.load_generals(str(root / "generals.txt"))
        self.load_battle_config(str(root / "battles.txt"))
        self.run_full_battle()


if __name__ == "__main__":
    EasyChibiBattle().quick_start()
