"""
赤壁戰役簡單版。

這個版本保留同樣的輸入與輸出格式，
但把流程壓縮成較少的方法，方便手動重打。
"""

from __future__ import annotations

from pathlib import Path

from chibi_battle import ChibiBattle


def build_game() -> ChibiBattle:
    """建立並載入一個可直接執行的戰役引擎。"""
    base_dir = Path(__file__).resolve().parent
    game = ChibiBattle()
    game.load_generals(base_dir / "generals.txt")
    game.load_battle_config(base_dir / "battles.txt")
    return game


def main() -> None:
    """
    直接執行簡單版流程。

    若只想快速看到結果，可以跑這個檔案。
    """

    game = build_game()
    game.run_full_battle(print_output=True)


if __name__ == "__main__":
    main()
