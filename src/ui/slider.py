from .ui_element import UIElement
import pygame
from pygame.locals import *
import src.constants as const
from src import prepare


class Slider(UIElement):
    def __init__(self, relative_rect, text, manager):
        super().__init__(relative_rect, manager)
        self.text = text
        self.font = pygame.font.Font(const.FONT, const.DEFAULT_FONT_SIZE)

        # State
        self.hover = False
        self.pressing = False
        self.progress = 0  # 0..1
        self.indicator_relative_pos_x = 0
        self.delta_x = 0  # save mouse.x - indicator.x when drag

        # Indicator image
        self.indicator_width = 20
        self.indicator_img = self.crop_by_width_and_scale_btn_img(self.indicator_width, prepare.btn_img)
        self.indicator_hover_img = self.crop_by_width_and_scale_btn_img(self.indicator_width, prepare.hover_btn_img)
        self.indicator_press_img = self.crop_by_width_and_scale_btn_img(self.indicator_width, prepare.press_btn_img)

        # Background image
        self.background_img = self.crop_by_width_and_scale_btn_img(self.rect.width, prepare.disable_btn_img)

    def process_event(self, event):
        pos_x = self.indicator_relative_pos_x + self.rect.x
        pos_y = self.rect.y
        indicator_rect = Rect(pos_x, pos_y, self.indicator_width, self.rect.h)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if indicator_rect.collidepoint((mouse_x, mouse_y)):
            self.hover = True
        else:
            self.hover = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover:
                self.pressing = True
                self.delta_x = mouse_x - indicator_rect.x
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.pressing:
                e = pygame.event.Event(pygame.USEREVENT, user_type=const.UI_BUTTON_PRESS, ui_element=self)
                pygame.event.post(e)
            self.pressing = False

        if self.pressing:
            self.set_indicator_relative_pos_x(mouse_x - self.delta_x - self.rect.x)

    def crop_by_width_and_scale_btn_img(self, width, img):
        width = width / const.UI_IMG_SCALE_RATIO
        surf = pygame.Surface((width, 20))
        surf.fill((255, 0, 0))
        btn_img = img
        surf.blit(btn_img, (0, 0), Rect(0, 0, width - 2, 20))
        surf.blit(btn_img, (width - 2, 0), Rect(198, 0, 2, 20))
        return pygame.transform.scale(surf, (int(width * const.UI_IMG_SCALE_RATIO), 40))

    def get_indicator_relative_pos_x(self):
        max_x = self.rect.w - self.indicator_width
        x = self.progress * max_x
        return x

    def set_indicator_relative_pos_x(self, relative_pos_x):
        max_x = self.rect.w - self.indicator_width
        relative_pos_x = min(relative_pos_x, max_x)
        relative_pos_x = max(relative_pos_x, 0)
        self.indicator_relative_pos_x = relative_pos_x
        self.progress = self.get_progress()

    def get_progress(self):
        max_x = self.rect.w - self.indicator_width
        return self.indicator_relative_pos_x / max_x

    def set_progress(self, progress):
        self.progress = progress
        self.indicator_relative_pos_x = self.get_indicator_relative_pos_x()

    def render(self):
        surface = pygame.Surface((self.rect.w, self.rect.h))

        # Blit background
        surface.blit(self.background_img, (0, 0))

        # Blit indicator
        if self.pressing:
            indicator_img = self.indicator_press_img
        elif self.hover:
            indicator_img = self.indicator_hover_img
        else:
            indicator_img = self.indicator_img
        surface.blit(indicator_img, (self.indicator_relative_pos_x, 0))

        # Draw text
        text = self.font.render(f"{self.text}: {self.progress * 100:.0f}%", True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = (self.rect.w / 2, self.rect.h / 2 - 3)
        surface.blit(text, rect)
        return surface
