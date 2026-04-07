"""
Tests for Big Two Card Game Implementation

This file contains basic tests for all 6 phases.
Run with: pytest tests/test_big_two.py
"""

import pytest
import sys
sys.path.insert(0, '.')

from game.models import Card, Deck, Hand, Player, Suit
from game.classifier import CardType, HandClassifier
from game.finder import HandFinder
from game.ai import AIStrategy
from game.game import BigTwoGame


class TestP1Models:
    """Test P1: Data Models"""

    def test_card_creation(self):
        """Test creating a Card"""
        card = Card(3, Suit.SPADES)
        assert card.rank == 3
        assert card.suit == Suit.SPADES
        assert str(card) == "3S"

    def test_card_comparison(self):
        """Test card comparison"""
        card1 = Card(5, Suit.SPADES)
        card2 = Card(5, Suit.HEARTS)
        card3 = Card(6, Suit.SPADES)
        
        # Same rank, different suit: spades < hearts
        assert card1 < card2
        
        # Different rank
        assert card1 < card3

    def test_deck_creation(self):
        """Test deck initialization"""
        deck = Deck()
        assert len(deck) == 54
        deck.shuffle()
        assert len(deck) == 54

    def test_hand_operations(self):
        """Test hand operations"""
        hand = Hand()
        card1 = Card(3, Suit.SPADES)
        
        hand.add_card(card1)
        assert len(hand) == 1
        
        hand.remove_card(card1)
        assert len(hand) == 0

    def test_player_creation(self):
        """Test player initialization"""
        player = Player(0, "Test Player")
        assert player.player_id == 0
        assert player.name == "Test Player"
        assert len(player.hand) == 0


class TestP2Classifier:
    """Test P2: Hand Classification"""

    def test_single_card_classification(self):
        """Test classification of single card"""
        classifier = HandClassifier()
        card = Card(5, Suit.SPADES)
        
        result = classifier.classify([card])
        assert result is not None
        card_type, strength = result
        assert card_type == CardType.SINGLE
        assert strength == 5

    def test_pair_classification(self):
        """Test classification of pair"""
        classifier = HandClassifier()
        cards = [Card(7, Suit.SPADES), Card(7, Suit.HEARTS)]
        
        result = classifier.classify(cards)
        assert result is not None
        card_type, strength = result
        assert card_type == CardType.PAIR
        assert strength == 7

    def test_invalid_pair(self):
        """Test that different ranks don't form a pair"""
        classifier = HandClassifier()
        cards = [Card(7, Suit.SPADES), Card(8, Suit.HEARTS)]
        
        result = classifier.classify(cards)
        assert result is None

    def test_straight_classification(self):
        """Test classification of straight"""
        classifier = HandClassifier()
        cards = [
            Card(3, Suit.SPADES),
            Card(4, Suit.HEARTS),
            Card(5, Suit.DIAMONDS),
            Card(6, Suit.CLUBS),
            Card(7, Suit.SPADES)
        ]
        
        result = classifier.classify(cards)
        assert result is not None
        card_type, strength = result
        assert card_type == CardType.STRAIGHT

    def test_flush_classification(self):
        """Test classification of flush"""
        classifier = HandClassifier()
        cards = [
            Card(3, Suit.SPADES),
            Card(5, Suit.SPADES),
            Card(7, Suit.SPADES),
            Card(9, Suit.SPADES),
            Card(11, Suit.SPADES)  # J
        ]
        
        result = classifier.classify(cards)
        assert result is not None
        card_type, strength = result
        assert card_type == CardType.FLUSH


class TestP3Finder:
    """Test P3: Hand Finding"""

    def test_find_singles(self):
        """Test finding all single cards"""
        finder = HandFinder()
        hand = Hand()
        cards = [Card(3, Suit.SPADES), Card(5, Suit.HEARTS), Card(7, Suit.DIAMONDS)]
        hand.add_cards(cards)
        
        plays = finder.find_all_plays(hand)
        assert len(plays) >= 3  # At least 3 singles
        
        # All plays should be singles (1 card each)
        singles_count = sum(1 for play in plays if len(play) == 1)
        assert singles_count == 3

    def test_find_pairs(self):
        """Test finding pairs"""
        finder = HandFinder()
        hand = Hand()
        cards = [
            Card(5, Suit.SPADES),
            Card(5, Suit.HEARTS),
            Card(7, Suit.DIAMONDS)
        ]
        hand.add_cards(cards)
        
        plays = finder.find_all_plays(hand)
        # Should have 3 singles + 1 pair
        assert len(plays) >= 4

    def test_has_valid_play(self):
        """Test checking for valid plays"""
        finder = HandFinder()
        hand = Hand([Card(3, Suit.SPADES)])
        
        assert finder.has_valid_play(hand) is True


class TestP4AI:
    """Test P4: AI Strategy"""

    def test_ai_choose_play(self):
        """Test AI choosing a play"""
        strategy = AIStrategy()
        player = Player(0, "AI")
        player.hand.add_cards([
            Card(3, Suit.SPADES),
            Card(5, Suit.HEARTS),
            Card(7, Suit.DIAMONDS)
        ])
        
        play = strategy.choose_play(player)
        assert play is not None
        assert len(play) >= 1

    def test_hand_evaluation(self):
        """Test hand strength evaluation"""
        strategy = AIStrategy()
        hand = Hand([
            Card(14, Suit.SPADES),  # A
            Card(15, Suit.HEARTS),  # 2
            Card(13, Suit.DIAMONDS)  # K
        ])
        
        strength = strategy.evaluate_hand_strength(hand)
        assert 0.0 <= strength <= 1.0


class TestP5Game:
    """Test P5: Game Flow"""

    def test_game_initialization(self):
        """Test game initialization"""
        game = BigTwoGame()
        assert len(game.players) == 4
        assert game.state.name == 'INITIALIZED'

    def test_game_start(self):
        """Test starting a game"""
        game = BigTwoGame()
        game.start_game()
        
        # Check each player has 13 cards
        for player in game.players:
            assert len(player.hand) == 13

    def test_get_game_status(self):
        """Test getting game status"""
        game = BigTwoGame()
        game.start_game()
        
        status = game.get_game_status()
        assert 'state' in status
        assert 'current_player' in status
        assert 'players' in status
        assert len(status['players']) == 4

    def test_valid_play_check(self):
        """Test checking if a play is valid"""
        game = BigTwoGame()
        game.start_game()
        
        player = game.players[0]
        first_card = player.hand.cards[0]
        
        # Single card from player's hand should be valid first play
        assert game.is_valid_play(0, [first_card]) is True


class TestP6UI:
    """Test P6: UI Components"""

    def test_renderer_initialization(self):
        """Test renderer initialization"""
        try:
            from ui.render import Renderer
            # Can't fully test without display in CI
            # Just check if module loads
            assert Renderer is not None
        except ImportError:
            pytest.skip("Pygame not available")

    def test_input_handler_initialization(self):
        """Test input handler initialization"""
        from ui.input import InputHandler
        handler = InputHandler()
        assert handler.quit_requested is False
        assert len(handler.selected_cards) == 0

    def test_input_handler_selection(self):
        """Test card selection"""
        from ui.input import InputHandler
        handler = InputHandler()
        
        handler.select_card(0)
        assert 0 in handler.selected_cards
        
        handler.select_card(0)
        assert 0 not in handler.selected_cards  # Toggle


def run_all_tests():
    """Run all tests"""
    if __name__ == "__main__":
        pytest.main([__file__, "-v"])


if __name__ == "__main__":
    run_all_tests()
