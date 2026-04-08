"""
Phase 6: GUI - 輸入處理
InputHandler 類別實作
"""

import pygame
from typing import List, Dict, Optional
from game.models import Hand


class InputHandler:
    """輸入處理器"""
    
    def __init__(self):
        """初始化輸入處理器"""
        self.selected_indices: List[int] = []
        self.buttons: Dict[str, pygame.Rect] = {}
    
    def handle_event(self, event: pygame.event.EventType, game) -> bool:
        """
        處理事件
        :param event: pygame 事件
        :param game: 遊戲對象
        :return: 事件是否已處理
        """
        if event.type == pygame.QUIT:
            return False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_click(event.pos, game)
            return True
        
        elif event.type == pygame.KEYDOWN:
            self.handle_key(event.key, game)
            return True
        
        return True
    
    def handle_click(self, pos: tuple, game) -> None:
        """
        處理點擊
        :param pos: 點擊座標
        :param game: 遊戲對象
        """
        x, y = pos
        
        # 檢查按鈕點擊
        if 'play' in self.buttons and self.buttons['play'].collidepoint(x, y):
            self.try_play(game)
        elif 'pass' in self.buttons and self.buttons['pass'].collidepoint(x, y):
            self.try_pass(game)
        
        # 檢查牌牌點擊（選擇/取消選擇）
        if hasattr(game, '_hand_rects'):
            for i, rect in enumerate(game._hand_rects):
                if rect.collidepoint(x, y):
                    if i in self.selected_indices:
                        self.selected_indices.remove(i)
                    else:
                        self.selected_indices.append(i)
    
    def handle_key(self, key: int, game) -> None:
        """
        處理鍵盤輸入
        :param key: 鍵盤按鍵
        :param game: 遊戲對象
        """
        if key == pygame.K_RETURN:
            self.try_play(game)
        elif key == pygame.K_p:
            self.try_pass(game)
        elif key == pygame.K_ESCAPE:
            self.selected_indices.clear()
    
    def try_play(self, game) -> bool:
        """
        嘗試出牌
        :param game: 遊戲對象
        :return: 是否成功出牌
        """
        if not self.selected_indices:
            return False
        
        player = game.get_current_player()
        cards = [player.hand[i] for i in self.selected_indices]
        
        if game.play(player, cards):
            self.selected_indices.clear()
            return True
        
        return False
    
    def try_pass(self, game) -> bool:
        """
        嘗試過牌
        :param game: 遊戲對象
        :return: 是否成功過牌
        """
        player = game.get_current_player()
        
        if game.pass_turn(player):
            self.selected_indices.clear()
            return True
        
        return False
    
    def clear_selection(self) -> None:
        """清空選擇"""
        self.selected_indices.clear()
