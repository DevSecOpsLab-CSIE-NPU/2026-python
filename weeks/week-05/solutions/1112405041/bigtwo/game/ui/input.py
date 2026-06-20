import pygame

class InputHandler:
    def __init__(self, renderer):
        self.renderer = renderer
        self.selected_indices = []

    def handle_event(self, event, game):
        p = game.get_current_player()
        if p.is_ai or game.is_game_over():
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.handle_click(event.pos, game)
        if event.type == pygame.KEYDOWN:
            return self.handle_key(event.key, game)
        return False

    def handle_click(self, pos, game):
        player = game.get_current_player()
        if player.is_ai or game.is_game_over():
            return False
        # 檢查按鈕
        for label, rect in game.buttons.items():
            if rect.collidepoint(pos):
                return self._button_action(label, game)
        # 檢查選牌
        hand_y = 500
        for i in range(len(player.hand)):
            rx = 20 + i * (self.renderer.CARD_WIDTH + 8)
            ry = hand_y
            rect = pygame.Rect(rx, ry, self.renderer.CARD_WIDTH, self.renderer.CARD_HEIGHT)
            if rect.collidepoint(pos):
                if i in self.selected_indices:
                    self.selected_indices.remove(i)
                else:
                    self.selected_indices.append(i)
                return True
        return False

    def _button_action(self, label, game):
        player = game.get_current_player()
        if label == "出牌" and self.selected_indices:
            cards = [player.hand[i] for i in sorted(self.selected_indices)]
            if game.play(player, cards):
                self.selected_indices = []
                return True
        elif label == "PASS":
            game.pass_(player)
            self.selected_indices = []
            return True
        return False

    def handle_key(self, key, game):
        player = game.get_current_player()
        if key == pygame.K_RETURN and self.selected_indices:
            cards = [player.hand[i] for i in sorted(self.selected_indices)]
            if game.play(player, cards):
                self.selected_indices = []
                return True
        elif key == pygame.K_p:
            game.pass_(player)
            self.selected_indices = []
            return True
        return False
