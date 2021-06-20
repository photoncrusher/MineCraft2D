import sys
import pygame
from pygame.locals import *
import src.constants as const
from src.ui import Button, Label, TextBox, ListSelection, ListItem, Slider, Toggle
from src.ui.manager import Manager
from src import state
from .screen import Screen


class OptionScreen(Screen):
    def __init__(self):
        self.bg_surface = pygame.image.load(const.START_OPTION_BG_IMG).convert()
        self.create_ui()


    def create_ui(self):
        self.manager = Manager((const.WIDTH, const.HEIGHT))

        self.label = Label("Options", self.manager)
        self.label.rect.center = (const.WIDTH / 2, const.HEIGHT / 8)

        vertical_gap = 10

        # Left column
        # Music slider
        self.music_slider = Slider(Rect(0, 0, 350, 40), "Music", self.manager)
        self.music_slider.rect.topright = self.label.rect.center
        self.music_slider.rect.move_ip(-10, vertical_gap * 4)

        # Invert mouse toggle
        self.invert_mouse_toggle = Toggle(Rect(0, 0, 350, 40), "Invert mouse: OFF", self.manager)
        self.invert_mouse_toggle.rect.topleft = self.music_slider.rect.bottomleft
        self.invert_mouse_toggle.rect.move_ip(0, vertical_gap)

        # FOV slider
        self.fov_slider = Slider(Rect(0, 0, 350, 40), "FOV", self.manager)
        self.fov_slider.rect.topleft = self.invert_mouse_toggle.rect.bottomleft
        self.fov_slider.rect.move_ip(0, vertical_gap)

        # Right column
        # Sound slider
        self.sound_slider = Slider(Rect(0, 0, 350, 40), "Sound", self.manager)
        self.sound_slider.rect.topleft = self.label.rect.center
        self.sound_slider.rect.move_ip(10, vertical_gap * 4)

        # Sensitivity slider
        self.sensitivity_slider = Slider(Rect(0, 0, 350, 40), "Sensitivity", self.manager)
        self.sensitivity_slider.rect.topleft = self.sound_slider.rect.bottomleft
        self.sensitivity_slider.rect.move_ip(0, vertical_gap)

        # Difficult toggle
        self.difficult_toggle = Toggle(Rect(0, 0, 350, 40), "Difficult: Normal", self.manager)
        self.difficult_toggle.rect.topleft = self.sensitivity_slider.rect.bottomleft
        self.difficult_toggle.rect.move_ip(0, vertical_gap)

        # Bottom row
        # Video setting btn
        self.video_setting_btn = Button(Rect(0, 0, 350, 40), "Video settings...", self.manager)
        self.video_setting_btn.rect.center = (const.WIDTH / 2, const.HEIGHT / 8 * 5)

        # Controls btn
        self.controls_btn = Button(Rect(0, 0, 350, 40), "Controls...", self.manager)
        self.controls_btn.rect.topleft = self.video_setting_btn.rect.bottomleft
        self.controls_btn.rect.move_ip(0, vertical_gap)

        # Done btn
        self.done_btn = Button(Rect(0, 0, 350, 40), "Done", self.manager)
        self.done_btn.rect.topleft = self.controls_btn.rect.bottomleft
        self.done_btn.rect.move_ip(0, 4 * vertical_gap)

    def set_setting_value(self):
        self.music_slider.set_progress(state.music_volume)
        self.sound_slider.set_progress(state.sound_volume)
        # self.invert_mouse_toggle.set...
        self.sensitivity_slider.set_progress(state.sensitivity)
        self.fov_slider.set_progress(state.fov)
        # self.difficult_toggle.set...

    def save_setting_value(self):
        state.music_volume = self.music_slider.progress
        state.sound_volume = self.sound_slider.progress
        # state.invert_mouse = False
        state.sensitivity = self.sensitivity_slider.progress
        state.fov = self.fov_slider.progress
        # state.difficult = "Normal"

    def show(self):
        window = state.window
        self.set_setting_value()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == USEREVENT:
                    if event.user_type == const.UI_BUTTON_PRESS:
                        if event.ui_element == self.done_btn:
                            self.save_setting_value()
                            state.screen = const.MAIN_MENU_SCREEN
                            return

                self.manager.process_event(event)

            window.blit(self.bg_surface, (0, 0))
            self.manager.draw_ui(window)
            pygame.display.update()
