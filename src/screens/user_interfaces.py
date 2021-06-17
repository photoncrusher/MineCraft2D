# ALL USER INTERFACE METHOD HERE
from src.screens.main_menu_screen import *


# CLASS UserInterface
class UserInterface:
    def __init__(self, manager, seed, menu):
        self.manager = manager
        self.selected = 'start'
        self.start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 450), (100, 50)),
                                                      text='START',
                                                      manager=manager)
        self.seed_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 400), (200, 50)),
                                                                 manager=manager)
        self.seed_text_box.text = seed
        self.menu = menu
        pass

    def get_event(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.start_btn:
                    self.menu.main.seed = self.seed_text_box.text
                    self.menu.main.screen = self.menu.main.IN_GAME_SCREEN
                    print('Start game with seed:', self.seed_text_box.text)
                    mixer.stop()
                    return

    def create_ui_01(self, manager, variance):
        if variance == 'SMALL_BOX_UI':
            self.start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 450), (100, 50)),
                                                          text='START',
                                                          manager=manager)
            self.seed_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 400), (200, 50)),
                                                                     manager=manager)
