"""Phase 6: Main application."""

try:
    import pygame
except ImportError:
    pygame = None

from game.game import BigTwoGame
from ui.render import Renderer
from ui.input import InputHandler


class BigTwoApp:
    """Big Two GUI 應用程式。"""

    def __init__(self) -> None:
        """初始化應用程式。"""
        if pygame is None:
            raise ImportError("pygame not installed. Run: pip install pygame")

        pygame.init()

        self.screen_width = 1024
        self.screen_height = 768
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Big Two Card Game")

        self.renderer = Renderer()
        self.input_handler = InputHandler()
        self.game = BigTwoGame()
        self.game.setup()

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) -> None:
        """執行遊戲主迴圈。"""
        if pygame is None:
            print("pygame not available")
            return

        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self) -> None:
        """處理事件。"""
        for event in pygame.event.get():
            if self.input_handler.handle_event(event, self.game):
                self.running = False

            if self.game.is_game_over():
                break

    def update(self) -> None:
        """更新遊戲狀態。"""
        if self.game.is_game_over():
            return

        player = self.game.get_current_player()

        if player.is_ai:
            self.game.ai_turn()
            self.game.next_turn()

    def render(self) -> None:
        """渲染遊戲畫面。"""
        # 背景
        self.screen.fill(self.renderer.COLORS['background'])

        # 繪製玩家資訊
        for i, player in enumerate(self.game.players):
            x = 50
            y = 100 + i * 150

            is_current = (i == self.game.current_player)
            self.renderer.draw_player_info(
                self.screen, player.name, len(player.hand),
                x, y, is_current, player.is_ai
            )

        # 繪製上家出牌
        if self.game.last_play is not None and self.game.last_player_name is not None:
            font = pygame.font.Font(None, 16)
            text = font.render(f"Last play by {self.game.last_player_name}", True,
                             self.renderer.COLORS['text'])
            self.screen.blit(text, (400, 50))

            for i, card in enumerate(self.game.last_play):
                x = 400 + i * 70
                y = 80
                self.renderer.draw_card(self.screen, card, x, y)

        # 繪製人類玩家手牌
        if not self.game.get_current_player().is_ai:
            player = self.game.get_current_player()
            player.hand.sort_desc()

            for i, card in enumerate(player.hand):
                x = 50 + i * 70
                y = 600
                selected = i in self.input_handler.selected_indices
                self.renderer.draw_card(self.screen, card, x, y, selected)

        # 遊戲結束訊息
        if self.game.is_game_over():
            font = pygame.font.Font(None, 48)
            text = font.render(f"Winner: {self.game.winner.name}!", True,
                             self.renderer.COLORS['selected'])
            text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(text, text_rect)

        pygame.display.flip()
