"""P6: Input Handler - User input processing"""

import pygame
from typing import List, Optional, Tuple
from game.models import Card


class InputHandler:
    """Handles user input for Big Two game"""

    def __init__(self):
        self.selected_cards: List[int] = []  # Indices of selected cards
        self.quit_requested = False

    def handle_events(self) -> dict:
        """
        Process pygame events.
        
        Returns:
            Dictionary with event information
        """
        events = {
            'quit': False,
            'mouse_click': None,
            'key_press': None,
        }

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                events['quit'] = True
                self.quit_requested = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    events['mouse_click'] = event.pos

            elif event.type == pygame.KEYDOWN:
                events['key_press'] = event.key

        return events

    def select_card(self, card_index: int):
        """Select or deselect a card"""
        if card_index in self.selected_cards:
            self.selected_cards.remove(card_index)
        else:
            self.selected_cards.append(card_index)

    def get_selected_cards(self, hand: List[Card]) -> List[Card]:
        """Get the selected cards from hand"""
        selected = []
        for idx in sorted(self.selected_cards):
            if 0 <= idx < len(hand):
                selected.append(hand[idx])
        return selected

    def clear_selection(self):
        """Clear the current selection"""
        self.selected_cards = []

    def handle_card_click(self, card_index: Optional[int]):
        """Handle clicking on a card"""
        if card_index is not None:
            self.select_card(card_index)

    def handle_key_press(self, key: int) -> Optional[str]:
        """
        Handle key press events.
        
        Returns:
            Action string or None
        """
        if key == pygame.K_SPACE:
            return 'submit'
        elif key == pygame.K_c:
            return 'clear'
        elif key == pygame.K_p:
            return 'pass'
        elif key == pygame.K_ESCAPE:
            return 'quit'
        elif key == pygame.K_r:
            return 'reset'
        
        return None

    def check_quit(self) -> bool:
        """Check if quit was requested"""
        return self.quit_requested

    def get_button_clicks(self, buttons: List[Tuple[pygame.Rect, str]]) -> Optional[str]:
        """
        Check if any button was clicked.
        
        Args:
            buttons: List of (pygame.Rect, button_name) tuples
            
        Returns:
            Button name if clicked, None otherwise
        """
        events = self.handle_events()
        if events['mouse_click']:
            x, y = events['mouse_click']
            for rect, button_name in buttons:
                if rect.collidepoint(x, y):
                    return button_name
        
        return None
