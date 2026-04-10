from pathlib import Path

from chibi_battle import ChibiBattle


def main() -> None:
    base = Path(__file__).parent
    game = ChibiBattle()
    game.load_generals(str(base / "generals.txt"))

    # Easy mode: run one wave quickly and print short summary.
    game.simulate_wave(1)
    ranking = game.get_damage_ranking()

    print("Easy Mode - One Wave Result")
    if not ranking:
        print("No damage yet")
        return

    for idx, (name, dmg) in enumerate(ranking, start=1):
        print(f"{idx}. {name}: {dmg}")


if __name__ == "__main__":
    main()
