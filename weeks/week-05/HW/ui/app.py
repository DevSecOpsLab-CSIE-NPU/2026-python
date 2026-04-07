"""P6: Application - Main Big Two game application"""

import pygame
from typing import List, Optional
from game.game import BigTwoGame
from game.models import Card
from .render import Renderer
from .input import InputHandler


class BigTwoApp:
    """Main application for Big Two game"""

    def __init__(self, player_names: Optional[List[str]] = None, 
                 ai_players: Optional[List[int]] = None,
                 fps: int = 60):
        """
        Initialize the Big Two application.
        
        Args:
            player_names: Names for 4 players
            ai_players: List of AI player IDs (0-3)
            fps: Frames per second for game loop
        """
        pygame.init()

        self.game = BigTwoGame(player_names, ai_players or [1, 2, 3])
        self.renderer = Renderer(1200, 800)
        self.input_handler = InputHandler()
        
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = False
        self.human_player_id = 0  # Player 0 is the human
        self.waiting_for_input = False

    def run(self):
        """Run the main game loop"""
        self.running = True
        self.game.start_game()

        while self.running:
            self._handle_input()
            self._update_game()
            self._render()
            self.clock.tick(self.fps)

        pygame.quit()

    def _handle_input(self):
        """Handle user input"""
        events = self.input_handler.handle_events()

        if events['quit']:
            self.running = False
            return

        # Check if it's human player's turn and waiting for input
        if self.waiting_for_input and events['key_press']:
            action = self.input_handler.handle_key_press(events['key_press'])
            
            if action == 'submit':
                self._submit_play()
            elif action == 'clear':
                self.input_handler.clear_selection()
            elif action == 'pass':
                self._pass_turn()

        # Handle mouse clicks on cards
        if self.waiting_for_input and events['mouse_click']:
            player = self.game.get_current_player()
            card_index = self.renderer.get_card_at_position(
                events['mouse_click'], 
                player.hand.cards
            )
            if card_index is not None:
                self.input_handler.handle_card_click(card_index)

    def _update_game(self):
        """Update game state"""
        current_player = self.game.get_current_player()

        if self.game.is_ai_player(current_player.player_id):
            # AI's turn
            self.waiting_for_input = False
            self.game._play_turn()
        else:
            # Human's turn
            self.waiting_for_input = True

    def _render(self):
        """Render the game"""
        game_state = self.game.get_game_status()
        self.renderer.draw_game_board(game_state)

        # If human is playing, draw their hand
        if self.waiting_for_input:
            player = self.game.get_current_player()
            self.renderer.draw_player_hand(
                player.hand.cards,
                self.input_handler.selected_cards
            )

    def _submit_play(self):
        """Submit the human player's selected play"""
        player = self.game.get_current_player()
        
        if player.player_id != self.human_player_id:
            return

        selected_cards = self.input_handler.get_selected_cards(player.hand.cards)

        if not selected_cards:
            return

        if self.game.is_valid_play(player.player_id, selected_cards):
            self.game.player_play(player.player_id, selected_cards)
            self.input_handler.clear_selection()
            self.waiting_for_input = False

    def _pass_turn(self):
        """Pass the human player's turn"""
        player = self.game.get_current_player()
        
        if player.player_id == self.human_player_id:
            self.game.player_play(player.player_id, None)
            self.input_handler.clear_selection()
            self.waiting_for_input = False

    def show_game_over(self):
        """Show game over message"""
        winner = self.game.get_winner()
        if winner:
            print(f"Game Over! Winner: {winner.name}")

    def is_running(self) -> bool:
        """Check if application is running"""
        return self.running
