import pygame
from game import BigTwoGame
from render import Renderer, HAND_Y, BUTTON_Y
from input import InputHandler

class BigTwoApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("憭扯?")
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler(self.renderer)
        self.game = BigTwoGame()
        self.game.setup()
        # 撱箇???
        self.game.buttons = {
            "?箇?": pygame.Rect(600, BUTTON_Y, 80, 40),
            "PASS": pygame.Rect(690, BUTTON_Y, 80, 40),
        }

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.render()
            pygame.display.flip()
            clock.tick(30)
            if not self.game.is_game_over():
                player = self.game.get_current_player()
                if player.is_ai:
                    pygame.time.wait(400)
                    self.game.ai_turn()
                    self.input_handler.selected_indices = []
            else:
                pygame.time.wait(3000)
                break
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
        # ?怠?雿摰?
        for i, p in enumerate(self.game.players):
            y = 20 + i * 55
            self.renderer.draw_player(p, 20, y, p is player)
        # ?思?摰嗅??
        if self.game.last_play:
            cards, name = self.game.last_play
            self.renderer.draw_last_play(cards, name, 20, 200)
        # 鈭粹??拙振????+ ??
        if not player.is_ai and not self.game.is_game_over():
            self.renderer.draw_hand(player.hand, 20, HAND_Y, self.input_handler.selected_indices)
            self.renderer.draw_buttons(self.game.buttons)
        # ?蝯?
        if self.game.is_game_over():
            self.renderer.draw_winner(self.game.winner.name)
