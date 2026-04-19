from __future__ import annotations

from game.game import BigTwoGame


def format_cards(cards):
    return " ".join(str(c) for c in sorted(cards))


def parse_indices(text: str, hand_size: int) -> list[int] | None:
    parts = text.strip().split()
    if not parts:
        return None

    try:
        indices = sorted(set(int(x) for x in parts))
    except ValueError:
        return None

    if any(i < 0 or i >= hand_size for i in indices):
        return None

    return indices


def show_state(game: BigTwoGame) -> None:
    print("\n" + "=" * 60)
    print(f"Round {game.round_number} | Current: {game.get_current_player().name}")
    if game.last_play is None:
        print("Last play: (none)")
    else:
        cards, name = game.last_play
        print(f"Last play: {name} -> {format_cards(cards)}")

    for p in game.players:
        if p.is_ai:
            print(f"{p.name}: {len(p.hand)} cards")
        else:
            hand_text = " ".join(f"[{i}:{card}]" for i, card in enumerate(p.hand.cards))
            print(f"{p.name}: {hand_text}")


def run_cli() -> None:
    game = BigTwoGame()
    game.setup()

    print("Big Two CLI")
    print("Input indices like: 0 1 2")
    print("Input p to pass")

    while not game.is_game_over():
        player = game.get_current_player()
        show_state(game)

        if player.is_ai:
            played = game.ai_turn()
            if played and game.last_play is not None and game.last_play[1] == player.name:
                print(f"{player.name} plays {format_cards(game.last_play[0])}")
            else:
                print(f"{player.name} passes")
        else:
            cmd = input("Your move > ").strip().lower()
            if cmd == "p":
                if not game.pass_(player):
                    print("You cannot pass now.")
                    continue
                print("You pass.")
            else:
                indices = parse_indices(cmd, len(player.hand))
                if indices is None:
                    print("Invalid input.")
                    continue

                cards = [player.hand.cards[i] for i in indices]
                if not game.play(player, cards):
                    print("Invalid play.")
                    continue
                print(f"You play {format_cards(cards)}")

        game.check_round_reset()
        game.winner = game.check_winner()
        if game.is_game_over():
            break
        game.next_turn()

    print("\nGame Over!")
    if game.winner is not None:
        print(f"Winner: {game.winner.name}")


if __name__ == "__main__":
    run_cli()
