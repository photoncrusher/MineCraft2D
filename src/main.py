import pygame
from pygame.locals import *
import os
from .screens import *
from . import constants as const
from . import state
from src import prepare


def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.set_num_channels(8)
    # Load data
    prepare.load_sound()

    # Setup window
    pygame.display.set_caption(const.WINDOW_TITLE)
    pygame.display.set_icon(prepare.GRASS_BLOCK_IMG)
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Init screens
    splash_screen = SplashScreen()
    main_menu = MainMenuScreen()
    in_game = InGameScreen()
    start_options_screen = StartOptionScreen()
    select_world_screen = SelectWorldScreen()
    option_screen = OptionScreen()
    test_screen = TestScreen()

    # Running
    while 1:
        if state.screen == const.SPLASH_SCREEN:
            splash_screen.show()
        elif state.screen == const.MAIN_MENU_SCREEN:
            main_menu.show()
        elif state.screen == const.IN_GAME_SCREEN:
            in_game.show()
        elif state.screen == const.START_OPTIONS_SCREEN:
            start_options_screen.show()
        elif state.screen == const.SELECT_WORLD_SCREEN:
            select_world_screen.show()
        elif state.screen == const.OPTION_SCREEN:
            option_screen.show()
        elif state.screen == const.TEST_SCREEN:
            test_screen.show()

if __name__ == '__main__':
    main()