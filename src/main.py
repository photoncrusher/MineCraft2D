import pygame
from pygame.locals import *
import os
from .screens import SplashScreen, MainMenuScreen, InGameScreen, StartOptionScreen, SelectWorldScreen
from . import constants as const
from . import state


def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    # Load data
    # storage.load_data()

    # Setup window
    pygame.display.set_caption(const.NAME)
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Init screens
    splash_screen = SplashScreen()
    main_menu = MainMenuScreen()
    in_game = InGameScreen()
    start_options_screen = StartOptionScreen()
    select_world_screen = SelectWorldScreen()

    # Running
    while 1:
        if state.screen == const.SPLASH_SCREEN:
            splash_screen.show()
        if state.screen == const.MAIN_MENU_SCREEN:
            main_menu.show()
        elif state.screen == const.IN_GAME_SCREEN:
            in_game.show()
        elif state.screen == const.START_OPTIONS_SCREEN:
            start_options_screen.show()
        elif state.screen == const.SELECT_WORLD_SCREEN:
            select_world_screen.show()


if __name__ == '__main__':
    main()
