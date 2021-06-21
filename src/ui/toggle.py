from typing import List

from .button import Button
import pygame
from pygame.locals import *
import src.constants as const
from src.draw import draw_inside_border
from src import prepare


class Toggle(Button):
    def __init__(self, relative_rect, text, states: List[str], manager, init_state=0):
        super().__init__(relative_rect, text, manager)
        self.states = states
        assert len(states) > 0
        self.cur_state = states[init_state]

    def set_state(self, idx):
        self.cur_state = self.states[idx]

    def get_state_idx(self):
        return self.states.index(self.cur_state)

    def next_state(self):
        idx = self.states.index(self.cur_state) + 1
        idx = idx % (len(self.states))
        self.set_state(idx)

    def process_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover:
                self.pressing = True
                pygame.mixer.Channel(1).play(self.sound)
                self.sound.play()
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.pressing:
                e = pygame.event.Event(pygame.USEREVENT, user_type=const.UI_TOGGLE_PRESS, ui_element=self)
                pygame.event.post(e)
                self.next_state()
            self.pressing = False

    def crop_and_scale_btn_img(self, img):
        width = self.rect.w / const.UI_IMG_SCALE_RATIO
        surf = pygame.Surface((width, 20))
        surf.fill((255, 0, 0))
        btn_img = img
        surf.blit(btn_img, (0, 0), Rect(0, 0, width - 2, 20))
        surf.blit(btn_img, (width - 2, 0), Rect(198, 0, 2, 20))
        return pygame.transform.scale(surf, (int(width * const.UI_IMG_SCALE_RATIO), 40))

    def render(self):
        surface = pygame.Surface((self.rect.w, self.rect.h))

        # Blit background
        if self.pressing:
            img = self.press_img
        elif self.hover:
            img = self.hover_img
        else:
            img = self.img
        surface.blit(img, (0, 0))

        # Draw text
        text = self.font.render(f'{self.text}: {self.cur_state}', True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = (self.rect.w / 2, self.rect.h / 2 - 3)
        surface.blit(text, rect)
        return surface
