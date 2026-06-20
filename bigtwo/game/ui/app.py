import pygame
from game.game import BigTwoGame
from game.ui.render import Renderer
from game.ui.input import InputHandler

class BigTwoApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Big Two")
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler(self.renderer)
        self.game = BigTwoGame()
        self.game.setup()
        self.buttons = {}

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.handle_events()
            self.render()
            pygame.display.flip()
            clock.tick(30)
            if not self.game.is_game_over():
                player = self.game.get_current_player()
                if player.is_ai:
                    pygame.time.wait(500)
                    self.game.ai_turn()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            self.input_handler.handle_event(event, self.game)

    def render(self):
        self.screen.fill(self.renderer.COLORS["background"])
        player = self.game.get_current_player()
        for i, p in enumerate(self.game.players):
            y = 20 + i * 60 if i < 3 else 480
            self.renderer.draw_player(p, 20, y, p is player)
        if self.game.last_play:
            cards, name = self.game.last_play
            self.renderer.draw_last_play(cards, name, 20, 200)
        if not player.is_ai and not self.game.is_game_over():
            self.renderer.draw_hand(player.hand, 20, 500, self.input_handler.selected_indices)
        if self.game.is_game_over():
            self.renderer.draw_winner(self.game.winner.name)
