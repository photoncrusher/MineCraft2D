from .ui_element import UIElement
import pygame
from pygame.locals import *
import src.constants as const
from src.draw import draw_inside_border


class Button(UIElement):
    def __init__(self, relative_rect, text, manager, bg_color=None, hover_color=None, press_color=None):
        super().__init__(relative_rect, manager)
        self.text = text
        self.font = pygame.font.Font(const.FONT, const.DEFAULT_FONT_SIZE)
        self.bg_color = bg_color or (0, 0, 0)
        self.hover_color = hover_color or const.BTN_HOVER_COLOR
        self.press_color = press_color or const.BTN_PRESSED_COLOR
        self.hover = False
        self.pressing = False

    def process_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover:
                self.pressing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.pressing:
                e = pygame.event.Event(pygame.USEREVENT, user_type=const.UI_BUTTON_PRESS, ui_element=self)
                pygame.event.post(e)
            self.pressing = False

    def render(self):
        surface = pygame.Surface((self.rect.w, self.rect.h))
        if self.pressing:
            color = self.press_color
        elif self.hover:
            color = self.hover_color
        else:
            color = self.bg_color

        # Fill background
        pygame.draw.rect(surface, color, surface.get_rect(), width=0, border_radius=0)

        draw_inside_border(surface, 2, const.WHITE)

        # Draw text
        text = self.font.render(self.text, True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = (self.rect.w / 2, self.rect.h / 2)
        surface.blit(text, rect)
        return surface
