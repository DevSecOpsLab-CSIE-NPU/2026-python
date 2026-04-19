from chibi_battle import ChibiBattle


def main() -> None:
    game = ChibiBattle()
    game.load_generals("generals.txt")
    game.load_battle_config("battles.txt")
    game.simulate_battle()

    print("[簡化版] 赤壁戰役結果")
    print("傷害排名:")
    for idx, (name, damage) in enumerate(game.get_damage_ranking(), 1):
        print(f"{idx}. {name} -> {damage}")

    print("\n勢力傷害:")
    for faction, damage in game.get_faction_stats().items():
        print(f"{faction}: {damage}")

    defeated = game.get_defeated_generals()
    print(f"\n戰敗將領: {', '.join(defeated) if defeated else '無'}")


if __name__ == "__main__":
    main()
