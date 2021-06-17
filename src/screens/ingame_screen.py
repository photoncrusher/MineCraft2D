import pygame
from pygame.locals import *
import sys
import time
from .screen import Screen
import src.constants as const
from src.screens.user_interfaces import *
import pygame_gui
from src.constants import *
from engine import *

class InGameScreen(Screen):
    def __init__(self, main):
        super().__init__(main)
        self.width = WIDTH
        self.heigth = HEIGTH

    def show(self):
        game = GameEngine(self.main.seed)
        manager = pygame_gui.UIManager((self.width, self.heigth))
        ui = UserInterface(manager, self)
        ui.create_ui_01(manager,'PAUSE_GAME_UI')
        window = self.main.window
        myfont = pygame.font.Font(const.FONT, 30)
        text2 = myfont.render(f'Seed: {self.main.seed}', True, (255, 0, 0))
        pause = False
        clock = pygame.time.Clock()
        x = game.x
        y = game.y
        moveLeft = False
        moveRight = False
        limit_x = WIDTH/20

        while True:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or moveLeft or moveRight:
                    if event.key == pygame.K_ESCAPE:
                        self.main.screen = self.main.MAIN_MENU_SCREEN
                        return
                    if event.key == pygame.K_RETURN:
                        pause = True
                    if event.key == pygame.K_LEFT:
                        moveLeft = True
                    if event.key ==pygame.K_RIGHT:
                        moveRight = True
                if event.type == pygame.KEYUP:
                    moveRight = False
                    moveLeft = False
                manager.process_events(event)
            if moveRight:
                x = x + WIDTH/360
                limit_x = limit_x + 1/6
            if moveLeft:
                x = x - WIDTH/360
                limit_x = limit_x - 1/6
            manager.update(time_delta)
            window.fill((255, 255, 255))
            window.blit(text2, (50, 150))
            if pause:
                ui.draw(window, manager)
            y = game.draw(window,x,y)[1]
            x_n = game.draw(window,x,y)[0]
            text1 = myfont.render('x: '+str(round(x_n,2)) + ', y: ' + str(round(y,2)), True, (0, 0, 0))
            window.blit(text1, (50, 50))

            pygame.display.update()
