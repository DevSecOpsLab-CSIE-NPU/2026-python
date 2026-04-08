"""
Phase 5: 遊戲流程
BigTwoGame 類別實作
"""

from typing import List, Optional, Tuple
from game.models import Card, Deck, Hand, Player
from game.classifier import HandClassifier
from game.finder import HandFinder
from game.ai import AIStrategy


class BigTwoGame:
    """大貳遊戲類別"""
    
    def __init__(self):
        """初始化遊戲"""
        self.deck = Deck()
        self.players: List[Player] = []
        self.current_player = 0
        self.last_play: Optional[Tuple[List[Card], str]] = None
        self.pass_count = 0
        self.winner: Optional[Player] = None
        self.round_number = 0
    
    def setup(self) -> None:
        """
        初始化遊戲
        - 建立牌堆、洗牌
        - 建立4位玩家（1人1 AI）
        - 發13張牌給每位玩家
        - 找3♣決定先手
        - 初始化遊戲狀態
        """
        # 建立玩家
        self.players = [
            Player("Player 1", is_ai=False),
            Player("AI 2", is_ai=True),
            Player("AI 3", is_ai=True),
            Player("AI 4", is_ai=True),
        ]
        
        # 洗牌並發牌
        self.deck.shuffle()
        for player in self.players:
            player.take_cards(self.deck.deal(13))
        
        # 找3♣決定先手
        self.current_player = 0
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs():
                self.current_player = i
                break
        
        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1
    
    def play(self, player: Player, cards: List[Card]) -> bool:
        """
        玩家出牌
        :param player: 玩家
        :param cards: 要出的牌
        :return: 出牌是否成功
        """
        # 檢查是否是當前玩家
        if self.players[self.current_player] != player:
            return False
        
        # 檢查合法性
        if not self._is_valid_play(cards):
            return False
        
        # 移除手牌
        player.play_cards(cards)
        
        # 設定last_play
        self.last_play = (cards, player.name)
        
        # 重置pass_count
        self.pass_count = 0
        
        # 檢查獲勝
        self.check_winner()
        
        # 輪到下位
        self.next_turn()
        
        return True
    
    def pass_turn(self, player: Player) -> bool:
        """
        玩家過牌
        :param player: 玩家
        :return: 過牌是否成功
        """
        # 檢查是否是當前玩家
        if self.players[self.current_player] != player:
            return False
        
        # 只有上家有牌卻不是第一回合才能過
        if self.last_play is None:
            return False
        
        self.pass_count += 1
        self.check_round_reset()
        
        self.next_turn()
        
        return True
    
    def next_turn(self) -> None:
        """輪到下一位玩家"""
        self.current_player = (self.current_player + 1) % 4
    
    def _is_valid_play(self, cards: List[Card]) -> bool:
        """
        檢查出牌是否合法
        :param cards: 要出的牌
        :return: 是否合法
        """
        return HandClassifier.can_play(self.last_play, cards)
    
    def check_round_reset(self) -> None:
        """檢查是否需要重置回合"""
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
    
    def check_winner(self) -> Optional[Player]:
        """
        檢查是否有獲勝者
        :return: 獲勝的玩家或None
        """
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player
        return None
    
    def is_game_over(self) -> bool:
        """檢查遊戲是否結束"""
        return self.winner is not None
    
    def get_current_player(self) -> Player:
        """獲取當前玩家"""
        return self.players[self.current_player]
    
    def ai_turn(self) -> bool:
        """
        AI 玩家自動執行一回合
        :return: 是否成功執行
        """
        player = self.get_current_player()
        
        if not player.is_ai:
            return False
        
        # 獲取所有合法出牌
        valid_plays = HandFinder.get_all_valid_plays(player.hand, self.last_play)
        
        if not valid_plays:
            # 沒有合法出牌，過牌
            self.pass_turn(player)
        else:
            # 選擇最佳出牌
            best_play = AIStrategy.select_best(valid_plays, player.hand)
            if best_play:
                self.play(player, best_play)
        
        return True
    
    def get_valid_plays(self, player: Player) -> List[List[Card]]:
        """
        獲取玩家的所有合法出牌
        :param player: 玩家
        :return: 所有合法出牌
        """
        if player != self.get_current_player():
            return []
        
        return HandFinder.get_all_valid_plays(player.hand, self.last_play)
