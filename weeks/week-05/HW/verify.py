#!/usr/bin/env python
"""Quick verification script for Big Two implementation"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("Big Two Card Game - Implementation Verification")
print("=" * 60)

# Test P1: Models
print("\n[P1] Testing Models...")
try:
    from game.models import Card, Deck, Hand, Player, Suit
    print("  ✓ Imports successful")
    
    # Create a card
    card = Card(5, Suit.SPADES)
    print(f"  ✓ Card creation: {card}")
    
    # Create a deck
    deck = Deck()
    print(f"  ✓ Deck creation: {len(deck)} cards")
    
    # Create a hand and player
    hand = Hand()
    player = Player(0, "Test Player")
    print(f"  ✓ Hand and Player creation successful")
    
except Exception as e:
    print(f"  ✗ Error: {e}")
    sys.exit(1)

# Test P2: Classifier
print("\n[P2] Testing Hand Classifier...")
try:
    from game.classifier import CardType, HandClassifier
    print("  ✓ Imports successful")
    
    classifier = HandClassifier()
    
    # Test single
    single_result = classifier.classify([Card(5, Suit.SPADES)])
    print(f"  ✓ Single card classification: {single_result[0].name}")
    
    # Test pair
    pair_result = classifier.classify([Card(7, Suit.SPADES), Card(7, Suit.HEARTS)])
    print(f"  ✓ Pair classification: {pair_result[0].name}")
    
except Exception as e:
    print(f"  ✗ Error: {e}")
    sys.exit(1)

# Test P3: Finder
print("\n[P3] Testing Hand Finder...")
try:
    from game.finder import HandFinder
    print("  ✓ Imports successful")
    
    finder = HandFinder()
    hand = Hand()
    hand.add_card(Card(3, Suit.SPADES))
    hand.add_card(Card(5, Suit.HEARTS))
    
    plays = finder.find_all_plays(hand)
    print(f"  ✓ Found {len(plays)} possible plays")
    
except Exception as e:
    print(f"  ✗ Error: {e}")
    sys.exit(1)

# Test P4: AI
print("\n[P4] Testing AI Strategy...")
try:
    from game.ai import AIStrategy
    print("  ✓ Imports successful")
    
    strategy = AIStrategy()
    player = Player(0, "AI Player")
    player.hand.add_card(Card(5, Suit.SPADES))
    player.hand.add_card(Card(7, Suit.HEARTS))
    
    play = strategy.choose_play(player)
    strength = strategy.evaluate_hand_strength(player.hand)
    print(f"  ✓ AI strategy works (strength: {strength:.2f})")
    
except Exception as e:
    print(f"  ✗ Error: {e}")
    sys.exit(1)

# Test P5: Game
print("\n[P5] Testing Game Flow...")
try:
    from game.game import BigTwoGame
    print("  ✓ Imports successful")
    
    game = BigTwoGame(
        player_names=["You", "AI1", "AI2", "AI3"],
        ai_players=[1, 2, 3]
    )
    game.start_game()
    
    status = game.get_game_status()
    print(f"  ✓ Game initialized: {len(game.players)} players")
    print(f"  ✓ Game status: {status['state']}")
    print(f"  ✓ Current player: {game.get_current_player().name}")
    
except Exception as e:
    print(f"  ✗ Error: {e}")
    sys.exit(1)

# Test P6: UI (basic)
print("\n[P6] Testing UI Components...")
try:
    from ui.input import InputHandler
    print("  ✓ InputHandler import successful")
    
    handler = InputHandler()
    handler.select_card(0)
    print(f"  ✓ InputHandler works (selected: {handler.selected_cards})")
    
    # Note: Renderer and App require Pygame display
    print("  ℹ Pygame components require display (skipped)")
    
except Exception as e:
    print(f"  ✗ Error: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ All verification tests passed!")
print("=" * 60)
print("\nProject structure:")
print("  • game/    - P1-P5 Core game logic")
print("  • ui/      - P6 User interface")
print("  • tests/   - Unit test suite")
print("  • main.py  - Entry point (requires pygame)")
print("\nTo run the game, install pygame and run:")
print("  pip install pygame")
print("  python main.py")
