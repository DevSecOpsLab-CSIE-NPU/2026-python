try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

from typing import List, Dict

from ui.render import Renderer, CARD_WIDTH, CARD_HEIGHT


class InputHandler:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer
        self.selected_indices: List[int] = []

    def handle_event(self, event, game) -> bool:
        if not PYGAME_AVAILABLE:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.handle_click(event.pos, game)
        if event.type == pygame.KEYDOWN:
            return self.handle_key(event.key, game)
        return False

    def handle_click(self, pos, game) -> bool:
        if not PYGAME_AVAILABLE:
            return False
        x, y = pos
        # Check buttons
        buttons = self._get_buttons()
        for name, rect in buttons.items():
            if rect.collidepoint(pos):
                if name == 'Play':
                    return self.try_play(game)
                elif name == 'Pass':
                    player = game.get_current_player()
                    result = game.pass_(player)
                    self.selected_indices = []
                    if result:
                        game.next_turn()
                    return result
        # Check card selection (human player area)
        player = game.get_current_player()
        if not player.is_ai:
            overlap = 35
            base_x, base_y = 50, 550
            for i in range(len(player.hand) - 1, -1, -1):
                cx = base_x + i * overlap
                if cx <= x <= cx + CARD_WIDTH and base_y <= y <= base_y + CARD_HEIGHT:
                    if i in self.selected_indices:
                        self.selected_indices.remove(i)
                    else:
                        self.selected_indices.append(i)
                    return True
        return False

    def handle_key(self, key, game) -> bool:
        if not PYGAME_AVAILABLE:
            return False
        if key == pygame.K_RETURN:
            return self.try_play(game)
        if key == pygame.K_p:
            player = game.get_current_player()
            result = game.pass_(player)
            self.selected_indices = []
            if result:
                game.next_turn()
            return result
        return False

    def try_play(self, game) -> bool:
        player = game.get_current_player()
        if player.is_ai or not self.selected_indices:
            return False
        cards = [player.hand[i] for i in sorted(self.selected_indices)]
        result = game.play(player, cards)
        if result:
            self.selected_indices = []
            game.next_turn()
        return result

    def _get_buttons(self) -> dict:
        if not PYGAME_AVAILABLE:
            return {}
        return {
            'Play': pygame.Rect(50, 500, 80, 35),
            'Pass': pygame.Rect(150, 500, 80, 35),
        }
