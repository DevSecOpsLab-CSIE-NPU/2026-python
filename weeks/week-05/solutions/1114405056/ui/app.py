try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

from game.game import BigTwoGame
from ui.render import Renderer, COLORS
from ui.input import InputHandler

SCREEN_W = 800
SCREEN_H = 650


class BigTwoApp:
    def __init__(self):
        self.game = BigTwoGame()
        self.game.setup()
        self.renderer = None
        self.input_handler = None
        self.screen = None

        if PYGAME_AVAILABLE:
            pygame.init()
            self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
            pygame.display.set_caption("Big Two (大老二)")
            self.renderer = Renderer(self.screen)
            self.input_handler = InputHandler(self.renderer)

    def run(self):
        if not PYGAME_AVAILABLE:
            print("pygame not installed. Run: pip install pygame")
            return

        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if not self.game.is_game_over():
                    self.input_handler.handle_event(event, self.game)

            if not self.game.is_game_over():
                current = self.game.get_current_player()
                if current.is_ai:
                    self.game.ai_turn()
                    self.game.next_turn()

            self.render()
            pygame.display.flip()

        pygame.quit()

    def render(self):
        self.screen.fill(COLORS['background'])

        # Draw AI players
        ai_positions = [(300, 50), (50, 250), (550, 250)]
        ai_players = [p for p in self.game.players if p.is_ai]
        for i, player in enumerate(ai_players):
            px, py = ai_positions[i]
            is_current = self.game.players[self.game.current_player] == player
            self.renderer.draw_player(player, px, py, is_current)
            self.renderer.draw_hand(player.hand, px, py + 25,
                                    selected_indices=[], face_up=False)

        # Draw human player
        human = self.game.players[0]
        is_current = self.game.current_player == 0
        self.renderer.draw_player(human, 50, 530, is_current)
        selected = self.input_handler.selected_indices if self.input_handler else []
        self.renderer.draw_hand(human.hand, 50, 550, selected_indices=selected, face_up=True)

        # Draw buttons
        if self.input_handler:
            self.renderer.draw_buttons(self.input_handler._get_buttons(), 50, 500)

        # Draw last play
        if self.game.last_play:
            cards, pname = self.game.last_play
            self.renderer.draw_last_play(cards, pname, 300, 300)

        # Game over message
        if self.game.is_game_over():
            font = pygame.font.SysFont('Arial', 36, bold=True)
            msg = f"{self.game.winner.name} wins!"
            text = font.render(msg, True, (255, 215, 0))
            self.screen.blit(text, (SCREEN_W // 2 - text.get_width() // 2,
                                    SCREEN_H // 2 - 20))
