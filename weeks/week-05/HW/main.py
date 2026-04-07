"""
Big Two Card Game - Complete Implementation

This implementation includes all 6 phases:
- P1: Data Models (Card, Deck, Hand, Player)
- P2: Hand Classification (CardType, HandClassifier)
- P3: Hand Finding (HandFinder)
- P4: AI Strategy (AIStrategy)
- P5: Game Flow (BigTwoGame)
- P6: GUI (Pygame UI with Renderer, InputHandler, BigTwoApp)
"""

from ui.app import BigTwoApp


def main():
    """Run the Big Two card game"""
    # Create game with player names
    player_names = [
        "You",           # Player 0 (Human)
        "AI Player 1",   # Player 1 (AI)
        "AI Player 2",   # Player 2 (AI)
        "AI Player 3"    # Player 3 (AI)
    ]
    
    # Players 1, 2, 3 are AI controlled (0 is human)
    ai_players = [1, 2, 3]

    # Create and run the application
    app = BigTwoApp(player_names=player_names, ai_players=ai_players, fps=60)
    app.run()


if __name__ == "__main__":
    main()
