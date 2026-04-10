import pygame

class InputHandler:
    def __init__(self):
        pass

    def get_clicked_card_index(self, pos, hitboxes):
        """
        精準判定點擊了哪張牌。
        [上市細節]：必須從最後一張牌 (Z-index 最高) 往回找，避免點到被遮擋的部分。
        """
        for i in range(len(hitboxes) - 1, -1, -1):
            if hitboxes[i].collidepoint(pos):
                return i
        return None

    def is_button_clicked(self, pos, button_rect):
        return button_rect.collidepoint(pos)