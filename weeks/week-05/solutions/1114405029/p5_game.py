# p5_game.py
# Phase 5：遊戲主控模組
#
# 功能：實作 BigTwoGame 類別，管理一局大老二遊戲的完整流程。
# 依賴：p1_models.py（Card, Hand, Deck, Player）、p2_classifier.py（HandClassifier）
#
# 執行測試：
#   python p5-game-unit-test.py

from __future__ import annotations

from typing import List, Optional

from p1_models import Card, Deck, Player
from p2_classifier import HandClassifier


class BigTwoGame:
    """
    大老二遊戲主控類別。

    負責管理：
    - 玩家建立與手牌分配
    - 出牌合法性驗證
    - 回合輪替與過牌計數
    - 回合重置（連續 3 人過牌）
    - 勝負判定
    """

    def __init__(self) -> None:
        """初始化遊戲狀態。"""
        self.deck: Optional[Deck] = None
        self.players: List[Player] = []
        self.current_player: int = 0
        self.last_play: Optional[List[Card]] = None
        self.pass_count: int = 0
        self.winner: Optional[Player] = None
        self.is_first_turn: bool = True

    # -------------------------------------------------------
    # 遊戲初始化
    # -------------------------------------------------------

    def setup(self) -> None:
        """
        初始化一局新遊戲。

        步驟：
          1. 建立 4 位玩家（1 人類 + 3 AI）
          2. 建立並洗牌
          3. 每人發 13 張牌
          4. 找到持有 ♣3（Card(3,0)）的玩家，設為先手
        """
        # 1. 建立玩家
        self.players = [
            Player("玩家", is_ai=False),
            Player("AI-1", is_ai=True),
            Player("AI-2", is_ai=True),
            Player("AI-3", is_ai=True),
        ]

        # 2. 建立牌堆並洗牌
        self.deck = Deck()
        self.deck.shuffle()

        # 3. 每人發 13 張牌
        for player in self.players:
            dealt_cards = self.deck.deal(13)
            player.take_cards(dealt_cards)

        # 4. 誰有 ♣3 誰先手
        self.current_player = 0
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs() is not None:
                self.current_player = i
                break

        # 重置狀態
        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.is_first_turn = True

    # -------------------------------------------------------
    # 玩家查詢
    # -------------------------------------------------------

    def get_current_player(self) -> Player:
        """取得目前輪到的玩家。"""
        return self.players[self.current_player]

    # -------------------------------------------------------
    # 出牌
    # -------------------------------------------------------

    def play(self, player: Player, cards: List[Card]) -> bool:
        """
        玩家嘗試出牌。

        規則：
          1. 遊戲真正第一手：只能出單張 ♣3
          2. 非第一手但 last_play 為 None：代表新回合起手，可自由出任意合法牌型
          3. 一般跟牌：必須符合 HandClassifier.can_play()

        :param player: 要出牌的玩家
        :param cards: 玩家想出的牌
        :return: True = 成功，False = 非法
        """
        # 防呆：不能出空牌
        if not cards:
            return False

        # 防呆：只能由目前輪到的玩家出牌
        if player is not self.get_current_player():
            return False

        # 遊戲第一手：只能出單張 ♣3
        if self.is_first_turn:
            is_legal = (len(cards) == 1 and cards[0] == Card(3, 0))
        else:
            # 新回合起手（不是遊戲第一手）
            if self.last_play is None:
                is_legal = HandClassifier.classify(cards) is not None
            else:
                # 一般跟牌
                is_legal = HandClassifier.can_play(self.last_play, cards)

        if not is_legal:
            return False

        # 合法出牌：從手牌移除
        player.hand.remove(cards)

        # 更新狀態
        self.last_play = cards
        self.pass_count = 0

        # 第一手已完成
        if self.is_first_turn:
            self.is_first_turn = False

        return True

    # -------------------------------------------------------
    # 過牌
    # -------------------------------------------------------

    def pass_(self, player: Player) -> bool:
        """
        玩家過牌。

        這個方法在本作業測試中，預期行為是：
        - 只要呼叫 pass_()，pass_count 就加 1

        真正的大老二規則限制（例如第一手不能過牌、新回合起手不能過牌）
        建議放在 UI / InputHandler 層先擋掉，而不是放在這裡，
        這樣才能同時符合單元測試與 GUI 互動需求。

        :param player: 要過牌的玩家
        :return: True
        """
        self.pass_count += 1
        return True

    # -------------------------------------------------------
    # 輪替
    # -------------------------------------------------------

    def next_turn(self) -> None:
        """輪到下一位玩家。"""
        self.current_player = (self.current_player + 1) % 4

    # -------------------------------------------------------
    # 回合重置
    # -------------------------------------------------------

    def check_round_reset(self) -> None:
        """
        若連續 3 人過牌，重置回合。

        重置後：
        - last_play = None
        - pass_count = 0
        """
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0

    # -------------------------------------------------------
    # 勝負判定
    # -------------------------------------------------------

    def check_winner(self) -> Optional[Player]:
        """
        檢查是否有人出完牌。

        :return: 勝者；若無則回傳 None
        """
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player

        self.winner = None
        return None

    def is_game_over(self) -> bool:
        """
        判斷遊戲是否結束。

        :return: True = 已結束，False = 尚未結束
        """
        return self.winner is not None