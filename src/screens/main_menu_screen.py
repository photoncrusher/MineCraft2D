import sys
from .screen import Screen
from pygame.locals import *
import pygame.mixer as mixer
from src.animate import *
import pygame_gui
from src.screens.user_interfaces import *

class MainMenuScreen(Screen):
    def __init__(self, main):
        super().__init__(main)
        self.width = constants.WIDTH
        self.heigth = constants.HEIGTH
        self.name = constants.NAME
        self.background_color = constants.BACKGROUND_COLOR
        self.background_audio = constants.BACKGROUND_AUDIO
        self.font = constants.FONT
        self.selected_color = constants.SELECTED_COLOR
        self.unselected_color = constants.UNSELECTED_COLOR
        self.tilte_font_size = constants.TILTE_FONT_SIZE
        self.option_font_size = constants.OPTION_FONT_SIZE
        self.background_img = get_animated(constants.ANIMATED_IMG)
        self.credit = constants.CREDIT_IMG
        self.stage = 0
        self.selected = 'start'

    # DEFINE THE TEXT FORMAT OF MENU
    def text_format(self, message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)
        return newText

    def get_event(self,event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = "start"
            elif event.key == pygame.K_DOWN:
                self.selected = "quit"
            elif event.key == pygame.K_ESCAPE:
                return 'main_ui'
            if event.key == pygame.K_RETURN:
                if self.selected == "start":
                    mixer.stop()
                    self.main.screen = self.main.IN_GAME_SCREEN
                    return 'not_main_ui'
                if self.selected == "quit":
                    pygame.quit()
                    quit()

    def show(self):
        # SET THE DISPLAY SURFACE AND CAPTION
        DISPLAYSURF = self.main.window
        manager = pygame_gui.UIManager((self.width, self.heigth))
        clock = pygame.time.Clock()

        # SET THE BACKGROUND IMAGE IN HOMESCREEN
        background = self.background_img
        index = 0.0

        # SET THE BACKGROUND AUDIO
        mixer.set_num_channels(3)
        mixer.Channel(1).play(mixer.Sound(self.background_audio), loops=-1)

        # SET LOCAL VARIABLE FOR MENU STATUS
        ui = UserInterface(manager, self)
        ui.create_ui_01(manager,'SMALL_BOX_UI')
        main_ui = True
        while True:
            selected = self.selected
            time_delta = clock.tick(60) / 1000.0

            # CLICK X TO EXIT EVENT GET
            for event in pygame.event.get():
                if self.get_event(event) == 'main_ui':
                    main_ui = True
                if self.get_event(event) == 'not_main_ui':
                    main_ui = False
                if ui.get_event(event) == 'CHANGE_STAGE':
                    return
                manager.process_events(event)
            manager.update(time_delta)

            # DRAW DISPLAY SURFACE: BACKGOUND COLOR, BACKGROUND IMAGE OF HOMESCREEN
            DISPLAYSURF.fill(self.background_color)
            DISPLAYSURF.blit(background[int(index)], (0, 0))
            index = (index + 0.2) % len(background)

            # OPTIONS OF MAIN MENU
            if selected == "start":
                text_start = self.text_format("START", self.font, self.option_font_size, self.selected_color)
            else:
                text_start = self.text_format("START", self.font, self.option_font_size, self.unselected_color)
            if selected == "quit":
                text_quit = self.text_format("QUIT", self.font, self.option_font_size, self.selected_color)
            else:
                text_quit = self.text_format("QUIT", self.font, self.option_font_size, self.unselected_color)

            # DRAW THEM (OPTIONS)
            title = self.text_format(self.name, self.font, self.tilte_font_size, self.background_color)
            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()
            DISPLAYSURF.blit(title, (self.width / 2 - (title_rect[2] / 2), self.heigth / 9))
            DISPLAYSURF.blit(text_start, (self.width / 2 - (start_rect[2] / 2), self.heigth / 2))
            DISPLAYSURF.blit(text_quit, (self.width / 2 - (quit_rect[2] / 2), self.heigth * 3 / 5))
            if not main_ui:
                ui.draw(DISPLAYSURF, manager)

            # UPDATE (MUST CALL AT END OF LOOP)
            pygame.display.update()
