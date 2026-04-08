"""
Phase 6: GUI - 渲染器
Renderer 類別實作
"""

import pygame
from typing import List, Dict, Tuple, Optional
from game.models import Card, Hand
from game.classifier import HandClassifier


class Renderer:
    """Pygame 渲染器"""
    
    COLORS = {
        'background': (45, 45, 45),
        'card_back': (74, 144, 217),
        'spade_club': (255, 255, 255),
        'heart_diamond': (231, 76, 60),
        'player': (46, 204, 113),
        'ai': (149, 165, 166),
        'selected': (241, 196, 15),
        'button': (52, 152, 219),
        'button_hover': (70, 180, 240),
        'text': (255, 255, 255),
    }
    
    CARD_WIDTH = 60
    CARD_HEIGHT = 90
    
    def __init__(self, screen: pygame.Surface):
        """
        初始化渲染器
        :param screen: pygame 陸面
        """
        self.screen = screen
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
    
    def draw_card(
        self,
        card: Card,
        x: int,
        y: int,
        selected: bool = False
    ) -> pygame.Rect:
        """
        繪製單張牌
        :param card: 牌
        :param x: x 座標
        :param y: y 座標
        :param selected: 是否被選中
        :return: 牌的矩形邊界
        """
        rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)
        
        # 繪製背景
        color = self.COLORS['selected'] if selected else (200, 200, 200)
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
        
        # 繪製花色和數字
        suit_symbol = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}[card.suit]
        rank_symbol = {
            3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T',
            11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'
        }[card.rank]
        
        # 花色和數字顏色
        if card.suit in [2, 3]:  # 紅心或黑桃
            text_color = self.COLORS['heart_diamond'] if card.suit == 2 else self.COLORS['spade_club']
        else:  # 方塊或梅花
            text_color = self.COLORS['heart_diamond'] if card.suit == 1 else self.COLORS['spade_club']
        
        # 繪製文字
        text = self.font_small.render(f"{suit_symbol}{rank_symbol}", True, text_color)
        text_rect = text.get_rect(center=rect.center)
        self.screen.blit(text, text_rect)
        
        return rect
    
    def draw_hand(
        self,
        hand: Hand,
        x: int,
        y: int,
        selected_indices: List[int]
    ) -> List[pygame.Rect]:
        """
        繪製手牌（重疊顯示）
        :param hand: 手牌
        :param x: x 座標
        :param y: y 座標
        :param selected_indices: 被選中的牌的索引
        :return: 矩形邊界列表
        """
        rects = []
        spacing = 50  # 牌之間的間距
        
        for i, card in enumerate(hand):
            card_x = x + i * spacing
            selected = i in selected_indices
            rect = self.draw_card(card, card_x, y, selected)
            rects.append(rect)
        
        return rects
    
    def draw_player_info(
        self,
        name: str,
        is_current: bool,
        is_ai: bool,
        card_count: int,
        x: int,
        y: int
    ) -> None:
        """
        繪製玩家信息
        :param name: 玩家名稱
        :param is_current: 是否是當前玩家
        :param is_ai: 是否是 AI
        :param card_count: 剩餘牌數
        :param x: x 座標
        :param y: y 座標
        """
        # 玩家名稱和卡數
        color = self.COLORS['selected'] if is_current else self.COLORS['ai' if is_ai else 'player']
        text = self.font_small.render(f"{name} ({card_count})", True, color)
        self.screen.blit(text, (x, y))
    
    def draw_last_play(
        self,
        cards: List[Card],
        player_name: str,
        x: int,
        y: int
    ) -> None:
        """
        繪製上家出牌
        :param cards: 上家的牌
        :param player_name: 玩家名稱
        :param x: x 座標
        :param y: y 座標
        """
        # 繪製玩家名稱
        text = self.font_small.render(f"{player_name} played:", True, self.COLORS['text'])
        self.screen.blit(text, (x, y))
        
        # 繪製牌
        for i, card in enumerate(cards):
            self.draw_card(card, x + i * 40, y + 30)
    
    def draw_button(
        self,
        text: str,
        x: int,
        y: int,
        width: int = 100,
        height: int = 40,
        hovered: bool = False
    ) -> pygame.Rect:
        """
        繪製按鈕
        :param text: 按鈕文字
        :param x: x 座標
        :param y: y 座標
        :param width: 寬度
        :param height: 高度
        :param hovered: 是否被懸停
        :return: 按鈕的矩形邊界
        """
        rect = pygame.Rect(x, y, width, height)
        color = self.COLORS['button_hover'] if hovered else self.COLORS['button']
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
        
        button_text = self.font_small.render(text, True, self.COLORS['text'])
        text_rect = button_text.get_rect(center=rect.center)
        self.screen.blit(button_text, text_rect)
        
        return rect
    
    def draw_game_over(self, winner_name: str) -> None:
        """
        繪製遊戲結束訊息
        :param winner_name: 獲勝者名稱
        """
        text = self.font_large.render(f"{winner_name} wins!", True, self.COLORS['selected'])
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        
        # 繪製半透明背景
        s = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        self.screen.blit(s, (0, 0))
        
        self.screen.blit(text, text_rect)
