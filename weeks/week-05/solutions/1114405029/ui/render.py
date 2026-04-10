import pygame
import os

class Renderer:
    def __init__(self):
        self.SCREEN_SIZE = (1000, 700)
        self.CARD_W, self.CARD_H = 75, 110
        
        pygame.font.init()
        try:
            self.font_card = pygame.font.SysFont("arial", 26, bold=True)
            self.font_ui = pygame.font.SysFont("arial", 18, bold=True)
            self.font_msg = pygame.font.SysFont("arial", 36, bold=True)
            self.font_title = pygame.font.SysFont("arial", 60, bold=True)
        except:
            self.font_card = pygame.font.Font(None, 26)
            self.font_ui = pygame.font.Font(None, 18)
            self.font_msg = pygame.font.Font(None, 36)
            self.font_title = pygame.font.Font(None, 60)

        self.COLORS = {
            "bg_dark": (20, 25, 20),
            "table_felt": (39, 119, 62),
            "table_border": (25, 25, 25),
            "card_white": (250, 250, 250),
            "card_border": (150, 150, 150),
            "shadow": (15, 15, 15),
            "suit_black": (30, 30, 30),
            "suit_red": (215, 40, 40),
            "gold": (255, 215, 0),
            "active_ring": (46, 204, 113)
        }
        self.floating_msg = {"text": "", "timer": 0, "color": (255, 255, 255)}

        self.assets = {}
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        try:
            menu_path = os.path.join(base_dir, "assets", "backgrounds", "menu.jpg")
            table_path = os.path.join(base_dir, "assets", "backgrounds", "table.jpg")
            self.assets['bg_menu'] = pygame.transform.scale(pygame.image.load(menu_path), self.SCREEN_SIZE)
            self.assets['bg_table'] = pygame.transform.scale(pygame.image.load(table_path), self.SCREEN_SIZE)
        except:
            pass 

        self.avatars = []
        for i in range(1, 5):
            try:
                path = os.path.join(base_dir, "assets", "avatars", f"p{i}.png")
                img = pygame.transform.smoothscale(pygame.image.load(path), (100, 100))
                self.avatars.append(img)
            except:
                self.avatars.append(None)
                
        self.small_avatars = [pygame.transform.smoothscale(img, (80, 80)) if img else None for img in self.avatars]

    def show_message(self, text, color=(255, 50, 50), duration=90):
        self.floating_msg = {"text": text, "timer": duration, "color": color}

    def draw_menu(self, screen, selected_idx, player_gold):
        if 'bg_menu' in self.assets:
            screen.blit(self.assets['bg_menu'], (0, 0))
            overlay = pygame.Surface(self.SCREEN_SIZE, pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            screen.blit(overlay, (0, 0))
        else:
            screen.fill((30, 40, 50))

        title = self.font_title.render("BIG TWO: CASINO", True, (255, 255, 255))
        screen.blit(title, (self.SCREEN_SIZE[0]//2 - title.get_width()//2, 80))
        
        # 破產提示顯示
        if player_gold <= 0:
            gold_txt = self.font_msg.render("BANKRUPT! Please restart the game.", True, (255, 50, 50))
        else:
            gold_txt = self.font_msg.render(f"Your Gold: ${player_gold}", True, self.COLORS["gold"])
        screen.blit(gold_txt, (self.SCREEN_SIZE[0]//2 - gold_txt.get_width()//2, 160))

        char_names = ["Robo", "Bunny", "Pony", "Neko"]
        start_x = 200
        spacing = 160
        char_hitboxes = []
        
        for i in range(4):
            x = start_x + i * spacing
            y = 300
            rect = pygame.Rect(x, y, 100, 140)
            char_hitboxes.append(rect)
            
            if i == selected_idx:
                pygame.draw.rect(screen, self.COLORS["active_ring"], rect.inflate(10, 10), border_radius=10)
            
            if self.avatars[i]:
                screen.blit(self.avatars[i], (x, y))
            else:
                pygame.draw.circle(screen, (100, 100, 100), (x+50, y+50), 50)
                
            name = self.font_ui.render(char_names[i], True, (255, 255, 255))
            screen.blit(name, (x + 50 - name.get_width()//2, y + 110))

        # 如果破產，START 按鈕變灰
        start_btn = pygame.Rect(self.SCREEN_SIZE[0]//2 - 100, 520, 200, 60)
        btn_color = (100, 100, 100) if player_gold <= 0 else (46, 204, 113)
        pygame.draw.rect(screen, btn_color, start_btn, border_radius=10)
        pygame.draw.rect(screen, (255, 255, 255), start_btn, width=3, border_radius=10)
        start_txt = self.font_msg.render("START", True, (255, 255, 255))
        screen.blit(start_txt, (start_btn.centerx - start_txt.get_width()//2, start_btn.centery - start_txt.get_height()//2))

        return char_hitboxes, start_btn

    def draw_scene(self, screen):
        # 1. 大背景
        if 'bg_table' in self.assets:
            screen.blit(self.assets['bg_table'], (0, 0))
            overlay = pygame.Surface(self.SCREEN_SIZE, pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 80))
            screen.blit(overlay, (0, 0))
        else:
            screen.fill(self.COLORS["bg_dark"])
            pygame.draw.ellipse(screen, self.COLORS["table_felt"], pygame.Rect(80, 80, 840, 480))

        # 2. 中間出牌區半透明黑框
        center_w, center_h = 420, 160
        center_rect = pygame.Rect(self.SCREEN_SIZE[0]//2 - center_w//2, self.SCREEN_SIZE[1]//2 - center_h//2 - 10, center_w, center_h)
        
        play_area_surf = pygame.Surface((center_w, center_h), pygame.SRCALPHA)
        pygame.draw.rect(play_area_surf, (0, 0, 0, 140), play_area_surf.get_rect(), border_radius=15)
        screen.blit(play_area_surf, center_rect.topleft)
        pygame.draw.rect(screen, (255, 255, 255, 100), center_rect, width=2, border_radius=15)

    def draw_table_cards(self, screen, last_play):
        if not last_play:
            text = self.font_ui.render("Waiting...", True, (150, 150, 150))
            screen.blit(text, (self.SCREEN_SIZE[0]//2 - text.get_width()//2, self.SCREEN_SIZE[1]//2 - 10))
            return
            
        spacing = 35
        total_w = (len(last_play) - 1) * spacing + self.CARD_W
        start_x = self.SCREEN_SIZE[0]//2 - total_w//2
        start_y = self.SCREEN_SIZE[1]//2 - self.CARD_H//2 - 10
        for i, card in enumerate(last_play):
            self._draw_card_entity(screen, card, start_x + i * spacing, start_y, is_selected=False)

    def draw_hud(self, screen, players, current_idx, player_avatar_indices):
        # 調整玩家Y軸，避免被手牌擋住
        positions = [
            (self.SCREEN_SIZE[0]//2, 470), 
            (100, self.SCREEN_SIZE[1]//2), 
            (self.SCREEN_SIZE[0]//2, 60), 
            (self.SCREEN_SIZE[0] - 100, self.SCREEN_SIZE[1]//2)
        ]

        for i, p in enumerate(players):
            if i >= len(positions): continue
            cx, cy = positions[i]
            is_active = (i == current_idx)
            
            if is_active:
                pygame.draw.circle(screen, self.COLORS["active_ring"], (cx, cy), 46, 0)
            
            if i < len(player_avatar_indices) and player_avatar_indices[i] is not None:
                avatar_idx = player_avatar_indices[i]
                if avatar_idx < len(self.small_avatars) and self.small_avatars[avatar_idx]:
                    screen.blit(self.small_avatars[avatar_idx], (cx - 40, cy - 40))
                else:
                    pygame.draw.circle(screen, (100, 100, 100), (cx, cy), 40, 0)
            else:
                pygame.draw.circle(screen, (100, 100, 100), (cx, cy), 40, 0)
                
            pygame.draw.circle(screen, (255, 255, 255), (cx, cy), 40, 3)

            name_txt = self.font_ui.render(p.name, True, (255, 255, 255))
            screen.blit(name_txt, (cx - name_txt.get_width()//2, cy + 45))

            # 統一所有人的狀態框 (深灰底白框)
            info_str = f"Cards: {len(p.hand)}" if p.is_ai else f"${p.gold}"
            info_txt = self.font_ui.render(info_str, True, self.COLORS["gold"])
            
            box_w = info_txt.get_width() + 20
            box_h = info_txt.get_height() + 10
            box_rect = pygame.Rect(0, 0, box_w, box_h)
            box_rect.center = (cx, cy + 75)
            
            pygame.draw.rect(screen, (20, 20, 20), box_rect.move(2, 3), border_radius=6)
            pygame.draw.rect(screen, (60, 60, 60), box_rect, border_radius=6)
            pygame.draw.rect(screen, (255, 255, 255), box_rect, width=2, border_radius=6)
            
            screen.blit(info_txt, (box_rect.x + 10, box_rect.y + 5))

    def draw_player_hand(self, screen, hand, selected_indices):
        if not hand: return []
        max_spacing = 35
        spacing = min(max_spacing, (700 - self.CARD_W) // max(1, len(hand)))
        total_w = (len(hand) - 1) * spacing + self.CARD_W
        start_x = self.SCREEN_SIZE[0]//2 - total_w//2
        start_y = 560 

        hitboxes = []
        for i, card in enumerate(hand):
            x = start_x + i * spacing
            is_sel = i in selected_indices
            rect = self._draw_card_entity(screen, card, x, start_y, is_selected=is_sel)
            hitboxes.append(rect)
        return hitboxes

    def _draw_card_entity(self, screen, card, x, y, is_selected):
        y_pos = y - 25 if is_selected else y
        rect = pygame.Rect(x, y_pos, self.CARD_W, self.CARD_H)
        
        pygame.draw.rect(screen, self.COLORS["shadow"], rect.move(2, 3), border_radius=6)
        pygame.draw.rect(screen, self.COLORS["card_white"], rect, border_radius=6)
        pygame.draw.rect(screen, self.COLORS["card_border"], rect, width=1, border_radius=6)
        
        color = self.COLORS["suit_red"] if card.suit in [1, 2] else self.COLORS["suit_black"]
        text = self.font_card.render(str(card), True, color)
        screen.blit(text, (x + 6, y_pos + 4))
        small_text = self.font_ui.render(str(card), True, color)
        screen.blit(small_text, (x + self.CARD_W - small_text.get_width() - 6, y_pos + self.CARD_H - 24))
        return rect

    def draw_buttons(self, screen, is_auto):
        btn_play = pygame.Rect(820, 520, 130, 45)
        btn_pass = pygame.Rect(820, 580, 130, 45)
        btn_auto = pygame.Rect(820, 640, 130, 45)
        
        auto_color = (241, 196, 15) if is_auto else (149, 165, 166)
        auto_text = "AUTO: ON" if is_auto else "Auto: OFF"
        
        buttons = [(btn_play, "Play", (46, 204, 113)), (btn_pass, "Pass", (231, 76, 60)), (btn_auto, auto_text, auto_color)]
        
        for btn, text, color in buttons:
            pygame.draw.rect(screen, (20, 20, 20), btn.move(2, 3), border_radius=8)
            pygame.draw.rect(screen, color, btn, border_radius=8)
            pygame.draw.rect(screen, (255, 255, 255), btn, width=2, border_radius=8)
            txt = self.font_ui.render(text, True, (255, 255, 255) if color != (241, 196, 15) else (0,0,0))
            screen.blit(txt, txt.get_rect(center=btn.center))
            
        return btn_play, btn_pass, btn_auto

    def draw_floating_message(self, screen):
        if self.floating_msg["timer"] > 0:
            msg = self.floating_msg["text"]
            color = self.floating_msg["color"]
            text = self.font_msg.render(msg, True, color)
            shadow = self.font_msg.render(msg, True, (0, 0, 0))
            cx = self.SCREEN_SIZE[0]//2 - text.get_width()//2
            screen.blit(shadow, (cx + 2, 222))
            screen.blit(text, (cx, 220))
            self.floating_msg["timer"] -= 1