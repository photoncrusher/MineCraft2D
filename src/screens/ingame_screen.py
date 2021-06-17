import pygame
from pygame.locals import *
import sys
import time
from .screen import Screen
import src.constants as const


class InGameScreen(Screen):
    def __init__(self, main):
        super().__init__(main)

    def show(self):
        window = self.main.window
        myfont = pygame.font.Font(const.FONT, 30)
        text1 = myfont.render('In game screen, ESC: back to main menu', True, (0, 0, 0))
        text2 = myfont.render(f'Seed: {self.main.seed}', True, (255, 0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main.screen = self.main.MAIN_MENU_SCREEN
                        return

            window.fill((255, 255, 255))
            window.blit(text1, (50, 50))
            window.blit(text2, (50, 150))
            pygame.display.update()
