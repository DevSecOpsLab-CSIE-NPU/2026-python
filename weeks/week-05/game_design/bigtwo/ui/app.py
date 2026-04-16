"""Big Two Card Game - Main Application"""

import pygame
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui.render import Renderer
from ui.input import InputHandler
from game.game import BigTwoGame


class BigTwoApp:
    """Main application for Big Two GUI."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 650))
        pygame.display.set_caption("Big Two - 大老二")
        self.clock = pygame.time.Clock()

        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler(self.renderer)
        self.game = BigTwoGame()

        self.buttons = {
            "Play": pygame.Rect(500, 480, 80, 35),
            "Pass": pygame.Rect(590, 480, 80, 35),
        }

        self.game.setup()
        self.run()

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    if not self.game.is_game_over():
                        self.input_handler.handle_event(event, self.game)

            if not self.game.is_game_over():
                current = self.game.get_current_player()
                if current.is_ai:
                    self.game.ai_turn()
                    pygame.time.wait(500)
                    self.game.next_turn()

            self.render()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def render(self) -> None:
        self.screen.fill(self.renderer.COLORS["background"])

        player_positions = [
            (50, 50, False),
            (700, 200, True),
            (50, 200, True),
            (700, 50, True),
        ]

        for i, (x, y, face_up) in enumerate(player_positions):
            self.renderer.draw_player(
                self.game.players[i],
                x,
                y,
                i == self.game.current_player,
                len(self.game.players[i].hand),
                face_up,
            )

        current = self.game.get_current_player()
        if self.game.last_player is not None:
            last_player = self.game.players[self.game.last_player]
            self.renderer.draw_last_play(
                self.game.last_play, f"Last: {last_player.name}", 300, 300
            )
        else:
            label = self.renderer.font.render(
                "No cards played yet", True, self.renderer.COLORS["text"]
            )
            self.screen.blit(label, (300, 300))

        if not current.is_ai and not self.game.is_game_over():
            self.renderer.draw_hand(
                current.hand, 100, 500, self.input_handler.selected_indices
            )

            for name, rect in self.buttons.items():
                color = (
                    self.renderer.COLORS["button_hover"]
                    if rect.collidepoint(pygame.mouse.get_pos())
                    else self.renderer.COLORS["button"]
                )
                pygame.draw.rect(self.screen, color, rect, border_radius=5)
                text_surf = self.renderer.font.render(
                    name, True, self.renderer.COLORS["text"]
                )
                text_rect = text_surf.get_rect(center=rect.center)
                self.screen.blit(text_surf, text_rect)

            info = f"Current: {current.name} - Press Enter to Play, P to Pass"
        else:
            if current.is_ai:
                info = f"Current: {current.name} (AI thinking...)"
            else:
                info = f"Current: {current.name}"

        info_surf = self.renderer.font.render(info, True, self.renderer.COLORS["text"])
        self.screen.blit(info_surf, (200, 610))

        if self.game.is_game_over():
            self.renderer.draw_game_over(self.game.winner)
