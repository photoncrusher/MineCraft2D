import pygame
from screens import SplashScreen, MainMenuScreen, InGameScreen
import constants
import os


class Main:
    def __init__(self):
        # Init
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        # Setup window
        self.window = pygame.display.set_mode((constants.WIDTH, constants.HEIGTH))
        pygame.display.set_caption(constants.NAME)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Setup screens
        self.splash_screen = SplashScreen(self)
        self.main_menu = MainMenuScreen(self)
        self.in_game = InGameScreen(self)

        # Set start screen
        self.screen = Main.SPLASH_SCREEN

        # State variables
        self.seed = "Default seed"

    SPLASH_SCREEN = 0
    MAIN_MENU_SCREEN = 1
    IN_GAME_SCREEN = 2
    PAUSE_GAME_SCREEN = 3

    def run(self):
        while 1:
            if self.screen == Main.SPLASH_SCREEN:
                self.splash_screen.show()
            if self.screen == Main.MAIN_MENU_SCREEN:
                self.main_menu.show()
            elif self.screen == Main.IN_GAME_SCREEN:
                self.in_game.show()
            elif self.screen == Main.PAUSE_GAME_SCREEN:
                pass


if __name__ == '__main__':
    Main().run()
