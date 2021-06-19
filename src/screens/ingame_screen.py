import pygame
from pygame.locals import *
import sys
from .screen import Screen
import src.constants as const
from engine import *
from src.ui import Manager, Button, Label


class InGameScreen(Screen):
    def __init__(self, main):
        super().__init__(main)
        self.width = WIDTH
        self.heigth = HEIGTH
        self.day_sky = pygame.transform.scale(pygame.image.load(SKY).convert(), (WIDTH, HEIGTH))
        self.manager = Manager((const.WIDTH, const.HEIGTH))
        self.create_pause_ui()

    def create_pause_ui(self):
        self.label = Label("Game Menu", self.manager)
        self.label.rect.center = (const.WIDTH / 2, const.HEIGTH / 8)

        gap = 10
        self.back_to_game_btn = Button(Rect(0, 0, 300, 40), "Back to Game", self.manager)
        self.back_to_game_btn.rect.midtop = self.label.rect.midbottom
        self.back_to_game_btn.rect.move_ip(0, 4 * gap)

        self.option_btn = Button(Rect(0, 0, 300, 40), "Options...", self.manager)
        self.option_btn.rect.midtop = self.back_to_game_btn.rect.midbottom
        self.option_btn.rect.move_ip(0, gap)

        self.save_and_quit_btn = Button(Rect(0, 0, 300, 40), "Save and Quit to Title", self.manager)
        self.save_and_quit_btn.rect.midtop = self.option_btn.rect.midbottom
        self.save_and_quit_btn.rect.move_ip(0, gap)

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
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pause = not pause
                if event.type == USEREVENT:
                    if event.user_type == const.UI_BUTTON_PRESS:
                        if event.ui_element == self.back_to_game_btn:
                            pause = False
                        if event.ui_element == self.option_btn:
                            print("Coming soon...")
                        if event.ui_element == self.save_and_quit_btn:
                            print("Not save yet")
                            self.main.screen = self.main.MAIN_MENU_SCREEN
                            return
                if not pause:
                    game.get_event(event)
                else:
                    self.manager.process_event(event)

            window.fill((255, 255, 255))
            window.blit(self.day_sky, (0, 0))

            x_y = game.draw(window)
            text1 = myfont.render('x: ' + str(round(x_y[0] / 20, 2)) + ', y: ' + str(round(x_y[1] / 20, 2)), True,
                                  (0, 0, 0))
            text3 = myfont.render('stat: ' + str(x_y[3]), True, (255, 0, 0))
            window.blit(text1, (30, 30))
            window.blit(text2, (30, 60))
            window.blit(text3, (30, 90))

            if pause:
                surf = pygame.Surface((const.WIDTH, const.HEIGTH))
                surf.set_alpha(200)
                rect = surf.get_rect(center=window.get_rect().center)
                window.blit(surf, rect)
                self.manager.draw_ui(window)

            pygame.display.update()
