from chibi_battle import ChibiBattle


def main():
    game = ChibiBattle()
    game.load_generals("generals.txt")
    game.simulate_battle()

    print("=== 赤壁戰役簡化報告 ===")
    print("Top 5 傷害：")
    for idx, (name, dmg) in enumerate(game.get_damage_ranking(), start=1):
        print(f"{idx}. {name}: {dmg}")

    print("\n勢力總傷害：")
    for faction, value in game.get_faction_stats().items():
        print(f"{faction}: {value}")

    print("\n戰敗武將：", ", ".join(game.get_defeated_generals()) or "無")


if __name__ == "__main__":
    main()
