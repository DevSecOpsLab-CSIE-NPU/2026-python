# Big Two (Game Design Practice)

This project is a Phase 1-6 implementation for week-05 game design.

## Structure

- game/models.py: Card, Deck, Hand, Player
- game/classifier.py: CardType, HandClassifier
- game/finder.py: HandFinder
- game/ai.py: AIStrategy
- game/game.py: BigTwoGame flow control
- ui/: lightweight UI placeholders for app integration
- tests/: unit tests for phases 1-5

## Run tests

Use unittest from project root:

python -m unittest discover -s tests -v

## Play game (CLI)

python main.py

This starts an interactive command-line game (1 human + 3 AI).
