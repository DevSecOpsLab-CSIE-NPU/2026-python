"""
Phase 5: 遊戲流程 - BigTwoGame 類別
"""
from typing import Optional, Tuple, List
from .models import Card, Deck, Hand, Player
from .classifier import HandClassifier
from .finder import HandFinder
from .ai import AIStrategy


class BigTwoGame:
    """Big Two 遊戲類別"""
    
    def __init__(self, num_human: int = 1):
        """
        初始化遊戲
        
        Args:
            num_human: 人類玩家數（默認1個）
        """
        self.deck: Optional[Deck] = None
        self.players: List[Player] = []
        self.current_player = 0
        self.last_play: Optional[Tuple[List[Card], int]] = None  # (cards, player_index)
        self.pass_count = 0
        self.winner: Optional[Player] = None
        self.round_number = 1
        self.num_human = num_human
        
        # 初始化玩家
        for i in range(4):
            is_ai = i >= num_human
            name = f"Human {i+1}" if not is_ai else f"AI {i+1-num_human}"
            self.players.append(Player(name, is_ai))
    
    def setup(self) -> None:
        """初始化遊戲"""
        # 建立牌堆
        self.deck = Deck()
        self.deck.shuffle()
        
        # 發牌：每位玩家13張
        for _ in range(13):
            for player in self.players:
                cards = self.deck.deal(1)
                player.take_cards(cards)
        
        # 找有3♣的玩家作為先手
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs() is not None:
                self.current_player = i
                break
    
    def get_current_player(self) -> Player:
        """取得當前玩家"""
        return self.players[self.current_player]
    
    def _is_valid_play(self, cards: List[Card]) -> bool:
        """
        檢查出牌是否有效
        
        Args:
            cards: 要出的牌
            
        Returns:
            是否有效
        """
        # 取得上家的牌
        last_play = self.last_play[0] if self.last_play else None
        return HandClassifier.can_play(last_play, cards)
    
    def play(self, player: Player, cards: List[Card]) -> bool:
        """
        玩家出牌
        
        Args:
            player: 出牌玩家
            cards: 出牌
            
        Returns:
            是否成功
        """
        # 檢查是否輪到該玩家
        if self.get_current_player() is not player:
            return False
        
        # 檢查牌是否在手上
        for card in cards:
            if card not in player.hand:
                return False
        
        # 檢查出牌合法性
        if not self._is_valid_play(cards):
            return False
        
        # 移除手牌
        player.play_cards(cards)
        
        # 設定上家的牌
        self.last_play = (cards, self.current_player)
        
        # 重置過牌計數
        self.pass_count = 0
        
        # 下一位
        self.next_turn()
        
        # 檢查獲勝
        if self.check_winner() is not None:
            return True
        
        return True
    
    def pass_(self, player: Player) -> bool:
        """
        玩家過牌
        
        Args:
            player: 過牌玩家
            
        Returns:
            是否成功
        """
        # 檢查是否輪到該玩家
        if self.get_current_player() is not player:
            return False
        
        # 增加過牌計數
        self.pass_count += 1
        
        # 檢查是否需要重置
        self.check_round_reset()
        
        # 下一位
        self.next_turn()
        
        return True
    
    def next_turn(self) -> None:
        """輪到下一位玩家"""
        self.current_player = (self.current_player + 1) % 4
    
    def check_round_reset(self) -> None:
        """檢查是否需要重置回合"""
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
    
    def check_winner(self) -> Optional[Player]:
        """檢查是否有獲勝者"""
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player
        return None
    
    def is_game_over(self) -> bool:
        """遊戲是否結束"""
        return self.winner is not None
    
    def ai_turn(self) -> bool:
        """
        AI 自動回合
        
        Returns:
            是否成功
        """
        player = self.get_current_player()
        if not player.is_ai:
            return False
        
        # 取得所有合法出牌
        last_play = self.last_play[0] if self.last_play else None
        valid_plays = HandFinder.get_all_valid_plays(player.hand, last_play)
        
        # 選擇最佳出牌
        best_play = AIStrategy.select_best(valid_plays, player.hand, last_play is None)
        
        if best_play:
            return self.play(player, best_play)
        else:
            return self.pass_(player)
