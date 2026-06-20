import pygame

class Renderer:
    COLORS = {
        "background": (45, 45, 45),
        "card_back": (74, 144, 217),
        "spade_club": (200, 200, 200),
        "heart_diamond": (231, 76, 60),
        "player": (46, 204, 113),
        "ai": (149, 165, 166),
        "selected": (241, 196, 15),
        "button": (52, 152, 219),
        "button_hover": (41, 128, 185),
    }
    CARD_WIDTH = 60
    CARD_HEIGHT = 90

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 28)
        self.small_font = pygame.font.SysFont("Arial", 20)

    def draw_card(self, card, x, y, selected=False):
        rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)
        is_red = card.suit in (1, 2)
        bg = self.COLORS["heart_diamond"] if is_red else self.COLORS["spade_club"]
        if selected:
            pygame.draw.rect(self.screen, self.COLORS["selected"], rect, border_radius=6)
            pygame.draw.rect(self.screen, bg, (x + 3, y + 3, self.CARD_WIDTH - 6, self.CARD_HEIGHT - 6), border_radius=4)
        else:
            pygame.draw.rect(self.screen, bg, rect, border_radius=6)
        pygame.draw.rect(self.screen, (180, 180, 180), rect, 2, border_radius=6)
        txt = self.small_font.render(repr(card), True, (0, 0, 0))
        self.screen.blit(txt, (x + 6, y + 6))

    def draw_hand(self, hand, x, y, selected_indices):
        for i, card in enumerate(hand):
            sx = x + i * (self.CARD_WIDTH + 8)
            self.draw_card(card, sx, y, i in selected_indices)

    def draw_player(self, player, x, y, is_current):
        color = self.COLORS["player"] if not player.is_ai else self.COLORS["ai"]
        border = (255, 255, 0) if is_current else color
        txt = self.font.render(f"{player.name} ({len(player.hand)})", True, border)
        self.screen.blit(txt, (x, y))

    def draw_last_play(self, cards, player_name, x, y):
        if cards:
            txt = self.small_font.render(f"上家 {player_name}:", True, (200, 200, 200))
            self.screen.blit(txt, (x, y))
            for i, c in enumerate(cards):
                self.draw_card(c, x + 120 + i * (self.CARD_WIDTH + 5), y)

    def draw_buttons(self, buttons):
        for label, rect in buttons.items():
            pygame.draw.rect(self.screen, self.COLORS["button"], rect, border_radius=8)
            txt = self.font.render(label, True, (255, 255, 255))
            tx = rect.x + (rect.width - txt.get_width()) // 2
            ty = rect.y + (rect.height - txt.get_height()) // 2
            self.screen.blit(txt, (tx, ty))

    def draw_winner(self, player_name):
        bg = pygame.Rect(200, 260, 400, 80)
        pygame.draw.rect(self.screen, (0, 0, 0), bg, border_radius=10)
        txt = self.font.render(f"贏家: {player_name} !", True, (255, 215, 0))
        self.screen.blit(txt, (400 - txt.get_width() // 2, 290))
