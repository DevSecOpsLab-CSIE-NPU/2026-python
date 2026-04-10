import pygame
from game.game import BigTwoGame
from ui.render import Renderer
from ui.input import InputHandler
from game.models import Player

class BigTwoApp:
    def __init__(self):
        pygame.init()
        self.renderer = Renderer()
        self.screen = pygame.display.set_mode(self.renderer.SCREEN_SIZE)
        pygame.display.set_caption("BIG TWO: CASINO")
        
        self.input = InputHandler()
        self.running = True
        
        self.global_gold = 1000  
        self.char_names = ["Robo", "Bunny", "Pony", "Neko"]
        
        self.state = "MENU"
        self.menu_selected_char = 0 
        
        self.game = None
        self.player_avatar_indices = []
        self.selected_indices = set()
        self.hitboxes = []
        self.btn_play = None
        self.btn_pass = None
        self.btn_auto = None
        self.menu_char_hitboxes = []
        self.menu_start_btn = None
        
        self.is_auto_playing = False 
        self.ai_thinking = False
        self.ai_timer = 0

    def start_new_game(self):
        self.game = BigTwoGame()
        
        human_name = self.char_names[self.menu_selected_char]
        self.player_avatar_indices = [self.menu_selected_char] 
        
        ai_names = [name for i, name in enumerate(self.char_names) if i != self.menu_selected_char]
        ai_indices = [i for i in range(4) if i != self.menu_selected_char]
        
        self.game.players = [Player(human_name, is_ai=False)]
        for i in range(3):
            self.game.players.append(Player(ai_names[i], is_ai=True))
            self.player_avatar_indices.append(ai_indices[i])
            
        self.game.players[0].gold = self.global_gold
        
        self.game.setup()
        self.is_auto_playing = False
        self.selected_indices.clear()
        self.state = "GAME"

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.update_logic()
            self.render()
            clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                
                if self.state == "MENU":
                    for i, rect in enumerate(self.menu_char_hitboxes):
                        if rect.collidepoint(pos):
                            self.menu_selected_char = i
                    
                    # [修改] 只有錢大於 0 時才能按 START
                    if self.menu_start_btn and self.menu_start_btn.collidepoint(pos):
                        if self.global_gold > 0:
                            self.start_new_game()
                        
                elif self.state == "GAME":
                    if self.game.winner:
                        self.global_gold = self.game.players[0].gold 
                        self.state = "MENU"
                        continue

                    current_p = self.game.get_current_player()
                    is_human_turn = not current_p.is_ai
                    
                    if self.btn_auto and self.input.is_button_clicked(pos, self.btn_auto):
                        self.is_auto_playing = not self.is_auto_playing
                        self.selected_indices.clear()

                    if is_human_turn and not self.is_auto_playing:
                        clicked_idx = self.input.get_clicked_card_index(pos, self.hitboxes)
                        if clicked_idx is not None:
                            if clicked_idx in self.selected_indices:
                                self.selected_indices.remove(clicked_idx)
                            else:
                                self.selected_indices.add(clicked_idx)
                                
                        elif self.btn_play and self.input.is_button_clicked(pos, self.btn_play):
                            self.try_play_cards()
                        elif self.btn_pass and self.input.is_button_clicked(pos, self.btn_pass):
                            self.try_pass_turn()

    def try_play_cards(self):
        p = self.game.get_current_player()
        selected_cards = [p.hand[i] for i in sorted(self.selected_indices)]
        
        if not selected_cards:
            self.renderer.show_message("Select cards first!", (255, 200, 50))
            return
            
        success = self.game.play_turn(selected_cards)
        if success:
            self.selected_indices.clear()
        else:
            self.renderer.show_message("Invalid Play!", (255, 50, 50))

    def try_pass_turn(self):
        success = self.game.play_turn([])
        if success:
            self.selected_indices.clear()
            self.renderer.show_message("Pass!", (200, 200, 200), 45)
        else:
            self.renderer.show_message("Cannot Pass now!", (255, 50, 50))

    def update_logic(self):
        if self.state != "GAME" or self.game.winner:
            if self.game and self.game.winner:
                self.renderer.show_message(f"Game Over! Winner: {self.game.winner.name} (Click to exit)", (50, 255, 50), 9999)
            return

        current_p = self.game.get_current_player()
        
        if current_p.is_ai or self.is_auto_playing:
            if not self.ai_thinking:
                self.ai_thinking = True
                self.ai_timer = pygame.time.get_ticks()
            
            if pygame.time.get_ticks() - self.ai_timer > 1000:
                was_ai = current_p.is_ai
                current_p.is_ai = True
                self.game.run_ai_turn()
                current_p.is_ai = was_ai 
                
                self.ai_thinking = False

    def render(self):
        if self.state == "MENU":
            self.menu_char_hitboxes, self.menu_start_btn = self.renderer.draw_menu(self.screen, self.menu_selected_char, self.global_gold)
            
        elif self.state == "GAME":
            self.renderer.draw_scene(self.screen)
            self.renderer.draw_table_cards(self.screen, self.game.last_play)
            self.renderer.draw_hud(self.screen, self.game.players, self.game.current_idx, self.player_avatar_indices)
            
            current_p = self.game.get_current_player()
            if not current_p.is_ai and not self.is_auto_playing:
                self.hitboxes = self.renderer.draw_player_hand(self.screen, self.game.players[0].hand, self.selected_indices)
            else:
                self.renderer.draw_player_hand(self.screen, self.game.players[0].hand, self.selected_indices)
                self.hitboxes = []
                
            self.btn_play, self.btn_pass, self.btn_auto = self.renderer.draw_buttons(self.screen, self.is_auto_playing)
            self.renderer.draw_floating_message(self.screen)
            
        pygame.display.flip()