from itertools import combinations
from typing import List, Optional
from .models import Card
from .classifier import HandClassifier

class HandFinder:
    """
    [P3] 高效牌組掃描器：為玩家提示與 AI 提供所有合法的出牌組合
    """
    @staticmethod
    def get_all_valid_plays(hand: List[Card], last_play: Optional[List[Card]] = None, must_include: Optional[Card] = None) -> List[List[Card]]:
        valid_plays = []
        # 如果有上家出牌，只能出相同張數；否則可以出 1, 2, 3, 5 張
        search_sizes = [len(last_play)] if last_play else [1, 2, 3, 5]
        
        for size in search_sizes:
            # 如果手牌張數不夠，直接跳過避免錯誤
            if len(hand) < size:
                continue
                
            # C(13, n) 組合掃描
            for combo in combinations(hand, size):
                combo_list = list(combo)
                
                # 第一局第一手限制：必須包含梅花 3
                if must_include and must_include not in combo_list:
                    continue
                    
                # 驗證牌型與大小合法性
                if not last_play:
                    # 自由出牌：只要牌型合法即可
                    if HandClassifier.classify(combo_list):
                        valid_plays.append(combo_list)
                else:
                    # 接牌：必須比上家大
                    if HandClassifier.compare(combo_list, last_play) > 0:
                        valid_plays.append(combo_list)
                        
        return valid_plays