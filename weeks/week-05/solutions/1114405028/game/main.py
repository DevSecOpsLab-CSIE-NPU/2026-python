"""Command-line entrypoint for the BigTwo game."""

from .game import BigTwoGame


def main():
    game = BigTwoGame()
    game.setup()
    print("BigTwo game initialized")


if __name__ == '__main__':
    main()
