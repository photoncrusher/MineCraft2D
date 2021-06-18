import sys
from .screen import Screen
import pygame
from pygame.locals import *
import pygame.mixer as mixer
import src.constants as const
from src.animate import get_animated
from src.ui import Button, Manager


class MainMenuScreen(Screen):
    def __init__(self, main):
        super().__init__(main)
        self.background_audio = const.BACKGROUND_AUDIO
        self.background_img = get_animated(const.ANIMATED_IMG)
        self.credit = const.CREDIT_IMG

    def create_ui(self):
        self.manager = Manager((const.WIDTH, const.HEIGTH))

        # Single player button
        rect = Rect(0, 0, 200, 40)
        rect.center = (const.WIDTH / 2, const.HEIGTH / 10 * 5)
        self.single_player_btn = Button(rect, "Singleplayer", self.manager)

        # Multiplayer button
        rect = Rect(0, 0, 200, 40)
        rect.center = (const.WIDTH / 2, const.HEIGTH / 10 * 6)
        self.multiplayer_btn = Button(rect, "Multiplayer", self.manager)

        # Option button
        rect = Rect(0, 0, 200, 40)
        rect.center = (const.WIDTH / 2, const.HEIGTH / 10 * 7)
        self.option_btn = Button(rect, "Options...", self.manager)

    def show(self):
        window = self.main.window

        # SET THE BACKGROUND IMAGE IN HOMESCREEN
        background = self.background_img
        index = 0.0

        # SET THE BACKGROUND AUDIO
        mixer.set_num_channels(3)
        mixer.Channel(1).play(mixer.Sound(self.background_audio), loops=-1)

        self.create_ui()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == USEREVENT:
                    if event.user_type == const.UI_BUTTON_PRESS:
                        if event.ui_element == self.single_player_btn:
                            self.main.screen = self.main.SELECT_WORLD_SCREEN
                            mixer.stop()
                            return
                        if event.ui_element == self.multiplayer_btn:
                            print("Multiplayer coming soon...")
                        if event.ui_element == self.option_btn:
                            self.main.screen = self.main.OPTION_SCREEN
                            return

                self.manager.process_event(event)

            # Draw background
            window.blit(background[int(index)], (0, 0))
            index = (index + 0.2) % len(background)

            # Draw UI
            self.manager.draw_ui(window)

            pygame.display.update()
