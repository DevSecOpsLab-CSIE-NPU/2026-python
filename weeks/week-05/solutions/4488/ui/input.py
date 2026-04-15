"""Phase 6: Input handler."""

try:
    import pygame
except ImportError:
    pygame = None

from typing import List, Optional, Tuple, Dict, Any


class InputHandler:
    """輸入事件處理。"""

    def __init__(self) -> None:
        """初始化輸入處理器。"""
        self.selected_indices: List[int] = []
        self.buttons: Dict[str, Tuple[int, int, int, int]] = {}

    def handle_event(self, event: Any, game: Any) -> bool:
        """處理事件。
        
        Args:
            event: pygame 事件
            game: 遊戲物件
            
        Returns:
            是否需要退出
        """
        if pygame is None:
            return False

        if event.type == pygame.QUIT:
            return True

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_click(event.pos, game)

        if event.type == pygame.KEYDOWN:
            self.handle_key(event.key, game)

        return False

    def handle_click(self, pos: Tuple[int, int], game: Any) -> bool:
        """處理滑鼠點擊。
        
        Args:
            pos: 點擊座標
            game: 遊戲物件
            
        Returns:
            是否成功
        """
        # 簡單實作，通常需要檢查牌位置和按鈕位置
        return False

    def handle_key(self, key: int, game: Any) -> bool:
        """處理鍵盤輸入。
        
        Args:
            key: 鍵碼
            game: 遊戲物件
            
        Returns:
            是否成功
        """
        if pygame is None:
            return False

        if key == pygame.K_RETURN:
            # Enter: 嘗試出牌
            return self.try_play(game)

        if key == pygame.K_p:
            # P: 過牌
            return self.handle_pass(game)

        return False

    def try_play(self, game: Any) -> bool:
        """嘗試出牌。
        
        Args:
            game: 遊戲物件
            
        Returns:
            是否成功
        """
        if not self.selected_indices:
            return False

        player = game.get_current_player()
        selected_cards = [player.hand[i] for i in self.selected_indices]

        if game.play(player, selected_cards):
            self.selected_indices = []
            return True

        return False

    def handle_pass(self, game: Any) -> bool:
        """處理過牌。
        
        Args:
            game: 遊戲物件
            
        Returns:
            是否成功
        """
        player = game.get_current_player()
        return game.pass_(player)
