"""
Phase 6: GUI - 主應用
BigTwoApp 類別實作
"""

import pygame
import sys
from typing import Optional
from game.game import BigTwoGame
from game.classifier import HandClassifier
from ui.render import Renderer
from ui.input import InputHandler


class BigTwoApp:
    """大貳遊戲 GUI 應用"""
    
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 900
    FPS = 60
    
    def __init__(self):
        """初始化應用"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Big Two Card Game")
        
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler()
        
        self.game = BigTwoGame()
        self.game.setup()
        
        self._hand_rects = []
        self.running = True
    
    def run(self) -> None:
        """主循環"""
        while self.running:
            # 處理事件
            if not self.handle_events():
                break
            
            # AI 轉
            if not self.game.is_game_over():
                player = self.game.get_current_player()
                if player.is_ai:
                    self.game.ai_turn()
            
            # 渲染
            self.render()
            
            # 控制 FPS
            self.clock.tick(self.FPS)
        
        pygame.quit()
        sys.exit()
    
    def handle_events(self) -> bool:
        """
        處理事件
        :return: 是否應該繼續運行
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if self.game.is_game_over():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    elif event.key == pygame.K_r:
                        self.game = BigTwoGame()
                        self.game.setup()
                        self.input_handler.clear_selection()
                continue
            
            # 只有人類玩家可以操作
            if not self.game.get_current_player().is_ai:
                self.input_handler.handle_event(event, self)
        
        return True
    
    def render(self) -> None:
        """渲染遊戲畫面"""
        # 清空屏幕
        self.screen.fill(self.renderer.COLORS['background'])
        
        if self.game.is_game_over():
            # 遊戲結束
            self.renderer.draw_game_over(self.game.winner.name)
            self.renderer.draw_button("Press R to restart or ESC to quit", 400, 500, 600, 50)
        else:
            # 繪製玩家信息和手牌
            self._draw_players()
            
            # 繪製上家出牌信息
            self._draw_last_play()
            
            # 繪製當前玩家的手牌
            self._draw_current_player_hand()
            
            # 繪製按鈕
            self._draw_buttons()
        
        pygame.display.flip()
    
    def _draw_players(self) -> None:
        """繪製所有玩家的信息和 AI 的背面牌"""
        positions = [
            (50, 700),      # Player 1 (bottom)
            (50, 50),       # AI 2 (top)
            (1200, 50),     # AI 3 (right)
            (1200, 700),    # AI 4 (bottom-right)
        ]
        
        for i, player in enumerate(self.game.players):
            x, y = positions[i]
            
            # 繪製玩家信息
            is_current = i == self.game.current_player
            self.renderer.draw_player_info(
                player.name,
                is_current,
                player.is_ai,
                len(player.hand),
                x,
                y
            )
            
            # AI 玩家顯示背面牌
            if player.is_ai and player != self.game.players[0]:
                for j in range(len(player.hand)):
                    card_x = x + j * 20
                    rect = pygame.Rect(card_x, y + 40, self.renderer.CARD_WIDTH, self.renderer.CARD_HEIGHT)
                    pygame.draw.rect(self.screen, self.renderer.COLORS['card_back'], rect)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
    
    def _draw_last_play(self) -> None:
        """繪製上家出牌信息"""
        if self.game.last_play:
            cards, player_name = self.game.last_play
            self.renderer.draw_last_play(cards, player_name, 450, 350)
    
    def _draw_current_player_hand(self) -> None:
        """繪製當前玩家的手牌"""
        player = self.game.get_current_player()
        
        if not player.is_ai:
            # 人類玩家，顯示手牌並允許選擇
            player.hand.sort_desc()
            self._hand_rects = self.renderer.draw_hand(
                player.hand,
                50,
                750,
                self.input_handler.selected_indices
            )
    
    def _draw_buttons(self) -> None:
        """繪製按鈕"""
        player = self.game.get_current_player()
        
        if not player.is_ai:
            # 出牌按鈕
            self.input_handler.buttons['play'] = self.renderer.draw_button(
                "Play (Enter)",
                400,
                650,
                150,
                40
            )
            
            # 過牌按鈕
            self.input_handler.buttons['pass'] = self.renderer.draw_button(
                "Pass (P)",
                600,
                650,
                150,
                40
            )
