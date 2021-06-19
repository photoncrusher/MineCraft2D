import pygame
from pygame.locals import *
import sys
import time
from .screen import Screen
import src.constants as const
from src.constants import *
from engine import *


class InGameScreen(Screen):
    def __init__(self, main):
        super().__init__(main)
        self.width = WIDTH
        self.heigth = HEIGTH
        self.day_sky = pygame.transform.scale(pygame.image.load(SKY).convert(),(WIDTH,HEIGTH))

    def show(self):
        game = GameEngine(self.main.seed)
        window = self.main.window
        myfont = pygame.font.Font(const.FONT, const.DEFAULT_FONT_SIZE)
        text2 = myfont.render(f'Seed: {self.main.seed}', True, (255, 0, 0))
        pause = False

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                game.get_event(event)
            window.fill((255, 255, 255))
            window.blit(self.day_sky,(0,0))

            # if pause:
            #     ui.draw(window, manager)
            x_y = game.draw(window)
            text1 = myfont.render('x: ' + str(round(x_y[0]/20, 2)) + ', y: ' + str(round(x_y[1]/20, 2)), True, (0, 0, 0))
            text3 = myfont.render('stat: '+str(x_y[3]), True, (255, 0, 0))
            window.blit(text1, (30, 30))
            window.blit(text2, (30, 60))
            window.blit(text3, (30, 90))

            pygame.display.update()
