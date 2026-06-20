import pygame

class InputHandler:
    def __init__(self, renderer):
        self.renderer = renderer
        self.selected_indices = []

    def handle_event(self, event, game):
        if event.type == pygame.KEYDOWN:
            return self.handle_key(event.key, game)
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.handle_click(event.pos, game)
        return False

    def handle_click(self, pos, game):
        if game.is_game_over():
            return False
        buttons = game.buttons if hasattr(game, 'buttons') else {}
        for label, rect in buttons.items():
            if rect.collidepoint(pos):
                return self._button_action(label, game)
        return False

    def _button_action(self, label, game):
        player = game.get_current_player()
        if player.is_ai:
            return False
        if label == "Play" and self.selected_indices:
            cards = [player.hand[i] for i in self.selected_indices]
            if game.play(player, cards):
                self.selected_indices = []
                return True
        elif label == "Pass":
            game.pass_(player)
            self.selected_indices = []
            return True
        return False

    def handle_key(self, key, game):
        if game.is_game_over():
            return False
        player = game.get_current_player()
        if player.is_ai:
            return False
        if key == pygame.K_RETURN and self.selected_indices:
            cards = [player.hand[i] for i in self.selected_indices]
            if game.play(player, cards):
                self.selected_indices = []
                return True
        elif key == pygame.K_p:
            game.pass_(player)
            self.selected_indices = []
            return True
        return False
